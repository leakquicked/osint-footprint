# OSINT Footprint

Identify manually supplied public-reference strings without scraping.

## Usage
```bash
python osint_footprint.py sample.txt
python osint_footprint.py sample.txt --output report.json
```

Python 3.10+, standard library only. The tool reads a local UTF-8 text file and emits JSON findings. It makes no network requests and does not modify input files.

## Rules
- `email` — info severity heuristic.
- `url` — info severity heuristic.
- `handle` — info severity heuristic.

Findings are leads for human review, not proof of compromise. Use only data you own or are authorized to inspect. Do not publish personal or confidential data.

## Tests
Run `python -m unittest discover -s tests -v`.
