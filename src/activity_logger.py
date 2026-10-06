"""Generate a small, reproducible daily development activity record."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVITY_FILE = ROOT / "daily" / "activity.json"


def build_record(now: datetime | None = None) -> dict[str, object]:
    """Build a UTC activity record without external services."""
    current = now or datetime.now(timezone.utc)
    return {
        "date": current.date().isoformat(),
        "timestamp_utc": current.isoformat(timespec="seconds"),
        "language": "Python",
        "automation": "GitHub Actions",
        "status": "generated",
    }


def write_record(record: dict[str, object]) -> None:
    """Append today's record unless it is already present."""
    ACTIVITY_FILE.parent.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, object]] = []
    if ACTIVITY_FILE.exists():
        records = json.loads(ACTIVITY_FILE.read_text(encoding="utf-8"))

    if not any(item.get("date") == record["date"] for item in records):
        records.append(record)

    ACTIVITY_FILE.write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    write_record(build_record())
    print(f"Updated {ACTIVITY_FILE}")
