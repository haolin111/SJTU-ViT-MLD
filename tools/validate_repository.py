"""Static packaging checks only; never execute scientific notebook cells."""

import ast
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[A-Z0-9]{16}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"(?:password|api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"][^'\"]{8,}['\"]", re.I),
]


def main():
    errors = []
    license_file = ROOT / "LICENSE"
    if not license_file.is_file():
        errors.append("MIT LICENSE file is missing.")
    elif not license_file.read_text().startswith("MIT License\n\nCopyright (c) 2026 Haolin Xu\n"):
        errors.append("LICENSE does not match the confirmed license and copyright holder.")
    manifest = json.loads((ROOT / "provenance.json").read_text())
    expected = {item["path"] for item in manifest["notebooks"]}
    found = {p.relative_to(ROOT).as_posix() for p in (ROOT / "notebooks").rglob("*.ipynb")}
    if expected != found or len(found) != 14:
        errors.append("Notebook inventory differs from the 14-file candidate manifest.")
    keys = set(json.loads((ROOT / "config.example.json").read_text())["paths"])
    used_keys = set()
    code_cells = 0
    for item in manifest["notebooks"]:
        path = ROOT / item["path"]
        if not path.is_file():
            continue
        content = path.read_bytes()
        if hashlib.sha256(content).hexdigest() != item["candidate_sha256"]:
            errors.append(f"{path.name}: checksum differs from the packaged candidate.")
        notebook = json.loads(content)
        split_figure = path.stem in {"figure8", "figure9"}
        exports = []
        if split_figure:
            final_cell = 6 if path.stem == "figure8" else 5
            if item["source_filename"] != "figure8.ipynb" or item.get("source_cell_indices") != [0, 1, 2, 3, 4, final_cell]:
                errors.append(f"{path.name}: split must use only the final combined figure8.ipynb source.")
        if notebook["metadata"]["kernelspec"]["name"] != "python3":
            errors.append(f"{path.name}: unexpected custom kernel.")
        for i, cell in enumerate(notebook["cells"]):
            source = "".join(cell["source"])
            if cell.get("attachments") or cell.get("outputs") or cell.get("execution_count") is not None:
                errors.append(f"{path.name} cell {i}: stored output/count/attachment.")
            if any(pattern.search(source) for pattern in PATTERNS):
                errors.append(f"{path.name} cell {i}: possible credential; value withheld.")
            if "/home/" in source or "../../../" in source:
                errors.append(f"{path.name} cell {i}: residual original data path.")
            if cell["cell_type"] != "code":
                continue
            code_cells += 1
            try:
                tree = ast.parse(source)
            except SyntaxError as exc:
                errors.append(f"{path.name} cell {i}: syntax error at line {exc.lineno}.")
                continue
            for node in ast.walk(tree):
                if split_figure and isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "savefig":
                    if node.args:
                        exports.extend(
                            child.value for child in ast.walk(node.args[0])
                            if isinstance(child, ast.Constant) and isinstance(child.value, str) and child.value.endswith(".png")
                        )
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "configured_path":
                    if len(node.args) != 1 or not isinstance(node.args[0], ast.Constant):
                        errors.append(f"{path.name} cell {i}: unrecognized configuration call.")
                    else:
                        used_keys.add(node.args[0].value)
        if split_figure and exports != [f"{path.stem}.png"]:
            errors.append(f"{path.name}: expected exactly its own figure export.")
    if used_keys - keys:
        errors.append(f"Configuration keys missing: {sorted(used_keys - keys)}")
    if keys - used_keys:
        errors.append(f"Configuration keys unused: {sorted(keys - used_keys)}")
    prohibited = {".nc", ".cdf", ".csv", ".h5", ".hdf5", ".ckpt", ".pt", ".pth", ".ttf", ".otf", ".docx"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in prohibited:
            errors.append(f"Non-code payload present: {path.relative_to(ROOT)}")
    for path in [ROOT / "plot_config.py", *sorted((ROOT / "tools").glob("*.py"))]:
        try:
            ast.parse(path.read_text(), filename=str(path))
        except SyntaxError as exc:
            errors.append(f"{path.name}: syntax error at line {exc.lineno}.")
    if errors:
        print("FAILED\n" + "\n".join(errors))
        return 1
    print(f"PASS: {len(found)} notebooks, {code_cells} code cells, {len(used_keys)} configuration keys.")
    print("JSON, syntax, hashes, outputs, paths, common-secret patterns, and payload checks passed.")
    print("Notebooks were not executed. Numerical and visual reproduction remains unverified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
