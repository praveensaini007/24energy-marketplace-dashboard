"""Expand the verified source package into this repository; no network or login required."""
from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parent
with zipfile.ZipFile(ROOT/'24ENERGY-Antigravity-Handover.zip') as z:
    prefix='24energy-marketplace-dashboard/'
    manifest=json.loads(z.read(prefix+'PACKAGE_MANIFEST.json'))
    files=manifest['files']
    allowed={'README.md','AGENTS.md','START_HERE.md'}
    prepared=[]
    for entry in files:
        name=entry['path']; dest=(ROOT/name).resolve()
        if not dest.is_relative_to(ROOT) or name.startswith('/'):
            raise SystemExit('Unsafe package path: '+name)
        data=z.read(prefix+name)
        if hashlib.sha256(data).hexdigest()!=entry['sha256']:
            raise SystemExit('Integrity mismatch: '+name)
        if dest.exists() and dest.read_bytes()!=data and name not in allowed:
            raise SystemExit('Local change would be overwritten: '+name+'; save your work first.')
        prepared.append((dest,data))
    for dest,data in prepared:
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    (ROOT/'PACKAGE_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
print('Source expanded and hashes verified. Read docs/LOCAL_SETUP.md next.')
print('After validation, commit and push the expanded source files so future clones need no bootstrap.')
