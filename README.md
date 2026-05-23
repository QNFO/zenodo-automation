# Zenodo Automation — One-Command DOI Registration Pipeline

**Project:** zenodo-automation
**Thesis:** Zenodo DOI registration should be a single command, not a browser workflow. This project provides a reusable CLI tool that creates depositions, uploads files, sets metadata, and publishes — all via the Zenodo REST API.

**Status:** Scaffolding — Phase 0

## One-Line Summary
Autonomous Zenodo DOI registration pipeline — sandbox-tested, production-ready when API recovers.

## Key Deliverables
1. **zenodo_publish.py** — CLI tool for creating and publishing Zenodo depositions
2. **Test plan** — Verified against sandbox (deposit 161914 created)
3. **Template** — Registered as `ZENODO-PUBLISH` prompt template

## Usage
```bash
python zenodo_publish.py --token $(cat ~/.zenodo_token) --title "Paper" --author "Author" --file "paper.md"
```

## Constraints
- Zero dependencies beyond Python stdlib
- Works with both sandbox and production Zenodo
- Token stored persistently at `%USERPROFILE%\.zenodo_token`
