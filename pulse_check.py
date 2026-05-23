#!/usr/bin/env python3
"""Pipeline health check - verifies all Zenodo pipeline components."""
import os, sys, urllib.request, urllib.error

print("ZENODO PIPELINE HEALTH CHECK")
print("=" * 60)

checks = 0
passed = 0

def check(name, condition):
    global checks, passed
    checks += 1
    if condition:
        passed += 1
        print(f"  [OK] {name}")
    else:
        print(f"  [FAIL] {name}")

# 1. File check
print("\n--- Files ---")
for f in ["zenodo_publish.py", "auto_publish.py", "pubhub_updater.py", "pulse_check.py", "test_plan.py"]:
    fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)
    check(f, os.path.exists(fp))

# 2. Token
print("\n--- Token ---")
token_path = os.path.join(os.environ["USERPROFILE"], ".zenodo_token")
check("Token file exists", os.path.exists(token_path))
if os.path.exists(token_path):
    with open(token_path) as f:
        token = f.read().strip()
    check("Token is 60 chars", len(token) == 60)

# 3. Sandbox
print("\n--- Zenodo Sandbox ---")
try:
    TOKEN = open(token_path).read().strip()
    req = urllib.request.Request("https://sandbox.zenodo.org/api/deposit/depositions?size=1")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    r = urllib.request.urlopen(req, timeout=10)
    check("Sandbox API accessible", True)
except Exception as e:
    check(f"Sandbox API ({e})", False)

# 4. Production
print("\n--- Zenodo Production ---")
try:
    req = urllib.request.Request("https://zenodo.org/api/deposit/depositions?size=1")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    r = urllib.request.urlopen(req, timeout=10)
    check("Production API accessible", True)
except urllib.error.HTTPError as e:
    check(f"Production API ({e.code})", False)
except Exception as e:
    check(f"Production API ({e})", False)

# 5. Artifacts
print("\n--- Artifacts ---")
artifacts = [
    ("Error Confinement", "https://qnfo.github.io/ultrametric-error-confinement/"),
    ("Convergence Explorer", "https://qnfo.github.io/ultrametric-convergence/"),
    ("Tree Distance", "https://qnfo.github.io/tree-distance/"),
    ("Hardware Visualizer", "https://qnfo.github.io/hardware-pathway/"),
    ("Technical Hub", "https://qnfo.github.io/QWAV/"),
    ("Zenodo Automation", "https://qnfo.github.io/zenodo-automation/"),
]
for name, url in artifacts:
    try:
        r = urllib.request.urlopen(urllib.request.Request(url), timeout=8)
        check(f"{name} (HTTP {r.status})", r.status == 200)
    except:
        check(f"{name}", False)

print(f"\n{'='*60}")
print(f"Pipeline: {passed}/{checks} checks passed")
if passed == checks:
    print("All systems operational.")
else:
    print(f"WARNING: {checks-passed} check(s) failed.")
