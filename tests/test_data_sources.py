"""
Tests for JalJeevan data sources and core pipeline logic.
Run with: pytest tests/ -v
"""
import os
import csv
import json
import pathlib
import pytest

DATA_DIR = pathlib.Path(__file__).parent.parent / "data"
OUTPUT_DIR = pathlib.Path(__file__).parent.parent / "output"
NGT_DIR = DATA_DIR / "ngt_orders"


# ── Data file existence ────────────────────────────────────────────────────────

class TestDataFiles:
    def test_dolphin_csv_exists(self):
        assert (DATA_DIR / "live_dolphin.csv").exists(), "live_dolphin.csv not found"

    def test_mining_csv_exists(self):
        assert (DATA_DIR / "live_mining.csv").exists(), "live_mining.csv not found"

    def test_ngt_orders_directory_exists(self):
        assert NGT_DIR.is_dir(), "ngt_orders/ directory not found"

    def test_ngt_orders_not_empty(self):
        txt_files = list(NGT_DIR.glob("*.txt"))
        assert len(txt_files) > 0, "No .txt legal orders found in ngt_orders/"


# ── CSV schema validation ──────────────────────────────────────────────────────

class TestDolphinCSVSchema:
    REQUIRED_FIELDS = {"zone", "timestamp", "dolphin_count"}

    def test_dolphin_csv_has_required_columns(self):
        with open(DATA_DIR / "live_dolphin.csv", newline="") as f:
            reader = csv.DictReader(f)
            headers = set(reader.fieldnames or [])
        missing = self.REQUIRED_FIELDS - headers
        assert not missing, f"Missing columns in live_dolphin.csv: {missing}"

    def test_dolphin_csv_has_data_rows(self):
        with open(DATA_DIR / "live_dolphin.csv", newline="") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) > 0, "live_dolphin.csv has no data rows"


class TestMiningCSVSchema:
    REQUIRED_FIELDS = {"zone", "timestamp", "confidence"}

    def test_mining_csv_has_required_columns(self):
        with open(DATA_DIR / "live_mining.csv", newline="") as f:
            reader = csv.DictReader(f)
            headers = set(reader.fieldnames or [])
        missing = self.REQUIRED_FIELDS - headers
        assert not missing, f"Missing columns in live_mining.csv: {missing}"

    def test_mining_confidence_in_range(self):
        with open(DATA_DIR / "live_mining.csv", newline="") as f:
            for row in csv.DictReader(f):
                conf = float(row["confidence"])
                assert 0.0 <= conf <= 1.0, f"Confidence out of range: {conf}"


# ── Config validation ──────────────────────────────────────────────────────────

class TestConfig:
    def test_config_importable(self):
        import sys
        sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
        import config  # noqa: F401

    def test_config_has_zones(self):
        import sys
        sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
        import config
        assert hasattr(config, "ZONES") or hasattr(config, "ZONE_IDS") or hasattr(config, "zones"), \
            "config.py must define ZONES or similar zone list"


# ── Output files ───────────────────────────────────────────────────────────────

class TestOutputFiles:
    def test_output_directory_exists(self):
        assert OUTPUT_DIR.is_dir(), "output/ directory not found — run pipeline first"

    @pytest.mark.skipif(
        not (OUTPUT_DIR / "stats.jsonl").exists(),
        reason="stats.jsonl not generated yet — run pipeline first",
    )
    def test_stats_jsonl_valid_json(self):
        with open(OUTPUT_DIR / "stats.jsonl") as f:
            for line in f:
                line = line.strip()
                if line:
                    obj = json.loads(line)
                    assert "zone" in obj, "stats.jsonl row missing 'zone' field"

    @pytest.mark.skipif(
        not (OUTPUT_DIR / "alerts.jsonl").exists(),
        reason="alerts.jsonl not generated yet — run pipeline first",
    )
    def test_alerts_jsonl_valid_json(self):
        with open(OUTPUT_DIR / "alerts.jsonl") as f:
            for line in f:
                line = line.strip()
                if line:
                    json.loads(line)  # just check parseable
