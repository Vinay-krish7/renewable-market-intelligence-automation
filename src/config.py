from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "output"

HEADLINES_PATH = OUTPUT_DIR / "headlines.json"
SUMMARY_PATH = OUTPUT_DIR / "summary.docx"
DATE_LIMIT = "May 1, 2026"
LOG_PATH = OUTPUT_DIR/"log.txt"