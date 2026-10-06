from src.metrics import summarize


def test_summarize_counts_unique_days_and_languages() -> None:
    records = [
        {"date": "2026-10-06", "language": "Python"},
        {"date": "2026-10-06", "language": "Python"},
        {"date": "2026-10-07", "language": "Python"},
    ]

    assert summarize(records) == {
        "total_entries": 3,
        "unique_days": 2,
        "languages": ["Python"],
    }
