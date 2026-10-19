"""Test the small configuration helper without scientific dependencies."""

import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load_helper(config_file):
    with patch.dict(os.environ, {"SJTU_VIT_PLOT_CONFIG": str(config_file)}):
        spec = importlib.util.spec_from_file_location("plot_config_test", ROOT / "plot_config.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    return module


class PathConfigTest(unittest.TestCase):
    def test_missing_configuration(self):
        with tempfile.TemporaryDirectory() as folder:
            helper = load_helper(Path(folder) / "missing.json")
            with self.assertRaises(FileNotFoundError):
                helper.configured_path("paired_mld_file")

    def test_relative_path_and_glob(self):
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / "config.json"
            config.write_text(json.dumps({"paths": {"oras_mld_pattern": "data/oras/*.nc"}}))
            helper = load_helper(config)
            data_existed = (ROOT / "data").exists()
            self.assertEqual(helper.configured_path("oras_mld_pattern"), str(ROOT / "data/oras/*.nc"))
            self.assertEqual((ROOT / "data").exists(), data_existed)

    def test_output_and_work_directories(self):
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / "config.json"
            paths = {key: str(Path(folder) / key) for key in ("output_dir", "work_dir")}
            config.write_text(json.dumps({"paths": paths}))
            helper = load_helper(config)
            for key, value in paths.items():
                self.assertEqual(helper.configured_path(key), value)
                self.assertTrue(Path(value).is_dir())

    def test_empty_and_missing_key(self):
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / "config.json"
            config.write_text(json.dumps({"paths": {"font_dir": ""}}))
            helper = load_helper(config)
            with self.assertRaises(ValueError):
                helper.configured_path("font_dir")
            with self.assertRaises(KeyError):
                helper.configured_path("no_such_key")


if __name__ == "__main__":
    unittest.main()
