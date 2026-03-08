# Contributing to ClaudeGuardian

Thanks for your interest in contributing.

## Quick setup

1. Fork and clone the repository.
2. Create a branch: `git checkout -b feat/your-change`.
3. Install dependencies:

```bash
pip install -r requirements-dev.txt
```

4. Run checks before opening a PR:

```bash
pytest
ruff check .
black --check .
```

## Coding guidelines

- Keep changes focused and small.
- Add tests for behavior changes.
- Prefer clear naming and straightforward logic.
- Do not commit secrets (API keys, tokens, credentials).

## Pull requests

- Use the PR template.
- Explain the problem and your solution approach.
- Link related issues when available.

## Reporting bugs

Use the bug report issue template with reproducible steps and logs.