# Deep Web Search Agents

CMPE 255 group project by the 4 Musketeers: an AI-powered deep research
application that will plan multi-step web searches, gather and verify evidence,
and generate cited reports. Phase 0 provides the dependency-light project
foundation only; search and analysis behavior will be added in later phases.

## Local setup

Python 3.10 or newer is required. No API keys or external services are needed
for Phase 0.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install -e ".[dev]"
cp .env.example .env
python -m deep_search_agents
```

The application prints a local readiness status. Run the tests with:

```bash
python -m unittest discover -s tests
# or, after installing the development extra:
pytest
```

## Project layout

```text
src/deep_search_agents/
  search/       future search planning and retrieval
  evidence/     future evidence analysis and verification
  evaluation/   future baseline comparison and evaluation
  ui/           local command-line entry point
tests/          smoke tests
```

Phase 0 deliberately does not implement web search, LLM calls, report
generation, or evaluation logic.
