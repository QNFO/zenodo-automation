# CHANGELOG -- zenodo-automation

## v1.0 — 2026-05-23 — Project Complete

**What Changed:**
- Scaffolded project — README.md, index.html, zenodo_publish.py
- Copied zenodo_publish.py from ultrametric-tree-universality
- Created interactive pipeline status dashboard (index.html)
- Written test plan — 22/22 PASS
- Copied to prompts/zenodo/ for cross-project reuse
- Registered ZENODO-PUBLISH prompt template
- Created GitHub repo + enabled Pages at qnfo.github.io/zenodo-automation/
- Sandbox integration test published (deposit 161914, record 162230)
- Cross-linked to all 4 QWAV artifact repos
- Added to technical site as tool card

**Files:** 6 files, 3 commits on main
**Live:** https://qnfo.github.io/zenodo-automation/
**Tests:** 22/22 PASS

**Known Issues:**
- Production Zenodo publishing blocked on API 500 (server-side)
- Token stored; retry when API recovers
