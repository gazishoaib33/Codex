# Codex Repository Overview

This repository now includes a **starter CLI** and a few **sample coding problems**
implemented in Python. Use it as a base to grow a real project (CLI, API, web app,
or learning playground).

## General Structure (Current State)

```
.
├─ src/
│  ├─ codex_cli.py         # CLI entry point
│  └─ problems/            # Example problem solutions
│     ├─ __init__.py
│     ├─ math.py
│     └─ strings.py
├─ docs/                   # Documentation (expand over time)
├─ .gitkeep
└─ README.md
```

## Important Things to Know

- The CLI is intentionally small and easy to extend.
- Problem solutions live in `src/problems` and are registered in
  `src/problems/__init__.py`.
- Each problem is a plain function that can be called from the CLI.

## How to Run the CLI

From the repository root:

```bash
python src/codex_cli.py list
python src/codex_cli.py run sum_of_multiples --payload '{"limit": 10}'
python src/codex_cli.py run is_palindrome --payload '{"text": "Never odd or even"}'
python src/codex_cli.py run word_frequencies --payload '{"text": "Hello hello world"}'
```

## Problems Included (Examples You Can Extend)

- **sum_of_multiples(limit, multiples=(3,5))**: sums all numbers below `limit`
  divisible by any given multiples.
- **is_palindrome(text)**: checks if text is a palindrome, ignoring punctuation.
- **word_frequencies(text)**: counts lowercase word frequencies.

## Suggested Next Steps

1. Add more problems under `src/problems/` (sorting, arrays, DP, graphs).
2. Add tests under `tests/` to validate each problem solution.
3. Turn the CLI into a package with `pyproject.toml`.
4. Add GitHub Actions for linting and tests.

## GitHub Project Ideas (What You Can Build With Codex)

### 1) Personal Developer Dashboard
- A small web app that tracks GitHub activity, open PRs, and TODOs.
- Add issues: dashboard layout, GitHub API integration, auth, UI theming.

### 2) CLI Productivity Toolkit
- A CLI that creates project templates or manages TODOs from the terminal.
- Add issues: CLI command structure, config file format, tests, release pipeline.

### 3) Study Tracker / Learning Journal
- A lightweight app to log learning sessions and generate weekly summaries.
- Add issues: data model, storage layer, summary report generator, UI or CLI.

### 4) Microservice Starter Kit
- A reference template with logging, health checks, Docker, and CI.
- Add issues: base service skeleton, health endpoint, dockerfile, CI workflow.

### 5) Code Snippet Library
- A small app to store and tag code snippets with search.
- Add issues: CRUD endpoints, tagging system, search UX, import/export.

## Starter GitHub Issues You Can Create Now

- **Define project scope**: Choose 1 idea and write a short product brief.
- **Add new problems**: Implement 3 more coding problems with docstrings.
- **Set up tests**: Add a minimal `pytest` suite for the problems.
- **Add CI**: GitHub Actions workflow for lint/test.
- **Write CONTRIBUTING.md**: How to run, test, and contribute.
