# conftest.py — pytest configuration for JalJeevan test suite
import sys
import pathlib

# Ensure project root is on sys.path so imports resolve correctly
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
