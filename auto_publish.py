# Automated DOI publishing with retry and auto-update
import subprocess, sys, os, time, json

TOKEN_PATH = os.path.join(os.environ["USERPROFILE"], ".zenodo_token")
PUBLICATION = r"G:\My Drive\projects\ultrametric-tree-universality\0.2.md"
PUBHUB = r"G:\My Drive\projects\ultrametric-tree-universality\pub-hub.html"
ZENODO_SCRIPT = r"G:\My Drive\projects\zenodo-automation\zenodo_publish.py"

if not os.path.exists(TOKEN_PATH):
    print("ERROR: Token not found")
    sys.exit(1)

def try_publish():
    TOKEN = open(TOKEN_PATH).read().strip()
    cmd = [
        sys.executable, ZENODO_SCRIPT,
        "--token", TOKEN,
        "--title", "Ultrametric Tree Universality: One Geometry, Six Domains",
        "--author", "Quni-Gudzinas, Rowan Brad",
        "--file", PUBLICATION,
        "--abstract", "Cross-domain synthesis demonstrating ultrametric tree geometry as universal mathematical structure.",
        "--keywords", "ultrametric,tree geometry,cross-domain,QWAV",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    output = result.stdout + result.stderr
    print(output[:500])
    if "PUBLISHED" in output:
        for line in output.split("\n"):
            if "doi.org" in line or "DOI:" in line:
                return line.strip()
    return None

def update_yaml(doi):
    yaml_path = PUBLICATION
    if not os.path.exists(yaml_path):
        print(f"YAML not found: {yaml_path}")
        return
    with open(yaml_path, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace("[DOI-PENDING: user must supply]", doi)
    c = c.replace("[DOI-PENDING]", doi)
    with open(yaml_path, "w", encoding="utf-8", newline="") as f:
        f.write(c)
    print(f"YAML updated: {doi}")

def update_pubhub(doi):
    with open(PUBHUB, "r", encoding="utf-8") as f:
        c = f.read()
    old = 'n:34,title:"Ultrametric Tree Universality",domain:"synth",level:"L5",doi:"[DOI-PENDING]"'
    new = f'n:34,title:"Ultrametric Tree Universality",domain:"synth",level:"L5",doi:"{doi}"'
    if old in c:
        c = c.replace(old, new)
        with open(PUBHUB, "w", encoding="utf-8", newline="") as f:
            f.write(c)
        print(f"Pub-hub updated: {doi}")
    else:
        print("Pub-hub pattern not found (may already be updated)")

MAX_RETRIES = 5
for attempt in range(1, MAX_RETRIES + 1):
    print(f"\n--- Attempt {attempt}/{MAX_RETRIES} ---")
    result = try_publish()
    if result:
        print(f"\nSUCCESS: {result}")
        doi = result.split("/")[-1] if "/" in result else result
        doi_full = f"10.5281/zenodo.{doi}" if not doi.startswith("10.") else doi
        update_yaml(doi_full)
        update_pubhub(doi_full)
        break
    else:
        if attempt < MAX_RETRIES:
            wait = 2 ** attempt
            print(f"Retrying in {wait}s...")
            time.sleep(wait)

print("\nDone.")
