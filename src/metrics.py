"""Simple metrics derived from the daily activity dataset."""

from __future__ import annotations


def summarize(records: list[dict[str, object]]) -> dict[str, object]:
    """Return basic, deterministic project metrics."""
    dates = {str(record["date"]) for record in records if "date" in record}
    languages = sorted({str(record["language"]) for record in records if "language" in record})
    return {
        "total_entries": len(records),
        "unique_days": len(dates),
        "languages": languages,
    }
