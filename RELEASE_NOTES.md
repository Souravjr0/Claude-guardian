# Release Notes

## v0.1.0 - 2026-03-08

### Highlights

- Initial ClaudeGuardian project scaffold
- Red-team prompt generation and injection test flow
- Hallucination heuristic checker and safety scoring utility
- FastAPI dashboard endpoints for status and score
- Professional repository polish pack:
  - Python CI workflow
  - Issue and PR templates
  - Contributing, security, code of conduct, roadmap, and changelog docs
  - Unit test suite with pytest
  - Lint/format tooling via ruff and black

### Notes

- Live model execution requires `ANTHROPIC_API_KEY` in `.env`.
- `main.py` will fail authentication until a valid API key is configured.