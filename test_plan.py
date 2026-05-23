#!/usr/bin/env python3
"""Test plan for zenodo-automation spinoff."""
import os, sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
passed = 0
failed = 0

def check(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print(f"  [PASS] {name}")
    else:
        failed += 1
        print(f"  [FAIL] {name} {detail}")

print("=" * 60)
print("TEST PLAN: zenodo-automation")
print("=" * 60)

# 1. File structure
print("\n--- 1. File Structure ---")
for f in ['README.md', 'index.html', 'zenodo_publish.py']:
    path = os.path.join(PROJECT_DIR, f)
    check(f"File exists: {f}", os.path.exists(path) and os.path.getsize(path) > 0)

# 2. HTML demo integrity
print("\n--- 2. Demo Page (index.html) ---")
html_path = os.path.join(PROJECT_DIR, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()
check("Has DOCTYPE", html.strip().startswith('<!DOCTYPE html>'))
check("Has closing </html>", html.strip().endswith('</html>'))
check("Has Zenodo title", 'Zenodo Automation' in html)
check("Has pipeline status", 'Pipeline Status' in html)
check("Has QWAV link", 'qnfo.github.io/QWAV' in html)

# 3. Script integrity
print("\n--- 3. Script (zenodo_publish.py) ---")
script_path = os.path.join(PROJECT_DIR, 'zenodo_publish.py')
with open(script_path, 'r', encoding='utf-8') as f:
    script = f.read()
check("Has create_deposition function", 'def create_deposition' in script)
check("Has publish_deposition function", 'def publish_deposition' in script)
check("Has upload_file function", 'def upload_file' in script)
check("Has token handling", 'ZENODO_TOKEN' in script)
check("Has sandbox support", 'SANDBOX' in script or 'sandbox' in script)
check("Has --sandbox flag", '--sandbox' in script)
check("Has --title flag", '--title' in script)
check("Has --author flag", '--author' in script)
check("Has --file flag", '--file' in script)

# 4. Token persistence
print("\n--- 4. Token Persistence ---")
token_path = os.path.join(os.environ["USERPROFILE"], ".zenodo_token")
check("Token file exists", os.path.exists(token_path))
if os.path.exists(token_path):
    with open(token_path, 'r') as f:
        token = f.read().strip()
    check("Token is non-empty", len(token) > 0)
    check("Token length is 60 chars", len(token) == 60)

# 5. Git state
print("\n--- 5. Git State ---")
check("Git repo exists", os.path.exists(os.path.join(PROJECT_DIR, '.git')))

# 6. prompts/zenodo copy
print("\n--- 6. Prompts Copy ---")
prompts_path = r"G:\My Drive\prompts\zenodo\zenodo_publish.py"
check("Copy exists in prompts/zenodo/", os.path.exists(prompts_path))

# Summary
print("\n" + "=" * 60)
total = passed + failed
print(f"RESULTS: {passed}/{total} passed, {failed}/{total} failed")
if failed == 0:
    print("ALL TESTS PASSED")
else:
    print(f"WARNING: {failed} test(s) failed")
print("=" * 60)

sys.exit(0 if failed == 0 else 1)
