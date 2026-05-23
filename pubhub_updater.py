# Standalone pub-hub DOI updater
import sys, os

PUBHUB = r"G:\My Drive\projects\zenodo-automation\pub-hub.html"

def update_doi(doi, title_hint):
    if not os.path.exists(PUBHUB):
        print(f"ERROR: {PUBHUB} not found")
        return False
    with open(PUBHUB, "r", encoding="utf-8") as f:
        c = f.read()
    if doi in c:
        print(f"DOI {doi} already present")
        return True
    # Find the matching publication by title hint
    idx = c.find(title_hint)
    if idx < 0:
        print(f"Publication not found: {title_hint}")
        return False
    # Find the doi field near this publication
    doi_start = c.find('doi:"', idx - 200)
    if doi_start < 0 or doi_start > idx + 500:
        print("DOI field not found near publication")
        return False
    doi_end = c.find('"', doi_start + 5)
    old_doi = c[doi_start + 5:doi_end]
    c = c[:doi_start + 5] + doi + c[doi_end:]
    with open(PUBHUB, "w", encoding="utf-8", newline="") as f:
        f.write(c)
    print(f"Updated: {old_doi} -> {doi}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pubhub_updater.py <DOI>")
        sys.exit(1)
    update_doi(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")
