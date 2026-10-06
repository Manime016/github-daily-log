# GitHub Daily Python Automation

A standalone Python automation project that runs through GitHub Actions and records a small, reproducible activity dataset.

## What it demonstrates

- Python 3.12
- Python modules and type hints
- JSON data processing
- Unit testing with the standard library
- GitHub Actions automation
- Automated Git commits

## Project structure

```text
src/
  activity_logger.py
  metrics.py
tests/
  test_metrics.py
daily/
  activity.json
.github/workflows/
  daily-commit.yml
```

The scheduled workflow runs once per day, executes the Python tests, generates the day's record, and commits the updated JSON dataset when a new record is needed.

No third-party Python packages are required.
