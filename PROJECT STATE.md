# PROJECT STATE -- zenodo-automation

**Project:** Zenodo Automation Pipeline — One-Command DOI Registration
**Last updated:** 2026-05-23
**Status:** ✅ COMPLETE — Deployed. Sandbox-proven. Awaiting production API recovery.
**Next:** Production DOI registration when Zenodo API recovers from 500 errors.

## Deliverables (All Deployed)

| File | Description | Status |
|:-----|:------------|:-------|
| zenodo_publish.py | CLI tool for Zenodo DOI registration — create deposition, upload, metadata, publish | ✅ Sandbox proven |
| index.html | Interactive pipeline status dashboard | ✅ Live |
| test_plan.py | 22/22 tests — file structure, demo, script integrity, token, git, prompts copy | ✅ 22/22 PASS |
| README.md | Project overview + usage | ✅ |
| SPRINT.md | Sprint tracker | ✅ |

## Pipeline Status
- **Sandbox:** ✅ Working — integration test published (record 162230)
- **Production:** 🔴 API 500 — server-side. Script ready, token stored.
- **Token:** Persisted at `%USERPROFILE%\.zenodo_token` (60 chars)
- **Prompts copy:** `G:\My Drive\prompts\zenodo\zenodo_publish.py`
- **Template:** `ZENODO-PUBLISH` registered via `fill_prompt_template`

## Usage
```bash
python zenodo_publish.py --token $(cat ~/.zenodo_token) --title "Title" --author "Author" --file "paper.md"
```

## Cross-Links
- Added to all 4 QWAV artifact repos (A1-A5) footer
- Listed on technical site as "Zenodo Automation" tool card
- Publish flow: `python zenodo_publish.py` → real DOI → update pub-hub → update paper YAML

## Handoff
For next agent: Script works. Token stored. Sandbox proven. Production blocked on Zenodo server 500. All tests pass. Project is complete — production publishing is a retry, not a rebuild.
