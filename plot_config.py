"""Resolve local paths without changing notebook analysis settings."""

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_FILE = Path(
    os.environ.get("SJTU_VIT_PLOT_CONFIG", str(ROOT / "config.json"))
).expanduser()
if not CONFIG_FILE.is_absolute():
    CONFIG_FILE = ROOT / CONFIG_FILE


def configured_path(key):
    """Return a configured absolute path (or glob) as a string."""
    if not CONFIG_FILE.is_file():
        raise FileNotFoundError(
            f"Create and edit {ROOT / 'config.json'} from config.example.json, "
            "or set SJTU_VIT_PLOT_CONFIG."
        )
    with CONFIG_FILE.open(encoding="utf-8") as handle:
        paths = json.load(handle)["paths"]
    value = paths[key]
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Configuration path {key!r} must be a nonempty string.")
    path = Path(os.path.expandvars(value)).expanduser()
    if not path.is_absolute():
        path = ROOT / path
    if key in {"output_dir", "work_dir"}:
        path.mkdir(parents=True, exist_ok=True)
    return str(path)
