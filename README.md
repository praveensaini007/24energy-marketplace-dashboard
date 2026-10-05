# 24 ENERGY Marketplace Dashboard — private handover

This repository contains the full source snapshot and documentation for the existing 24 ENERGY marketplace analytics website.

**Source is packaged in `24ENERGY-Antigravity-Handover.zip` to preserve its directory structure through the browser upload.** It has not yet been committed as expanded source folders. The packaged GitHub checks workflow becomes active only after the expanded files are committed and pushed.

## Continue in Antigravity

1. Clone this private repository and open its folder in Antigravity.
2. Run `python bootstrap.py` (Windows also supports `py bootstrap.py`). This verifies file hashes and expands the source into the repository root. It does not contact any service or alter the live website.
3. Read `START_HERE.md`, `AGENTS.md`, `docs/HANDOVER.md` and `docs/LOCAL_SETUP.md`.
4. Install locked dependencies, initialize the separate local database and use local test sign-in as documented.
5. Commit and push the expanded files after validation. Then use normal branches and pull requests for future edits.

If Python is unavailable, extract the ZIP and copy the CONTENTS of its `24energy-marketplace-dashboard` folder into this repository root.

## First Antigravity prompt

Continue this existing application. First unpack the verified source using bootstrap.py if app/ does not exist. Read AGENTS.md, docs/HANDOVER.md, docs/BUSINESS_RULES.md, docs/LOCAL_SETUP.md and docs/DATA_AND_HOSTING.md. Preserve the existing code and settlement-based calculations. Establish local development, record checks actually passed, and commit the expanded source. Do not migrate hosting or remove authentication. Update the handover document after every task.

## What is verified

TypeScript, marketplace/performance/GMV checks and a portable Linux build passed. A fresh Windows install, GitHub CI and local browser sign-in on the user's computer have not yet been verified.

## What remains separate

The live site stays on Sites. GitHub pushes do not automatically publish it. Latest live uploads and production database/object storage are NOT included in this code snapshot. The ZIP includes confidential historical business seed data; keep this repository private.

Live website: https://energy-marketplace-pnl.sainipraveen051.chatgpt.site
Last deployed application source: `61c8d8c76ad1e69108a239b7532e461d72562954`.
