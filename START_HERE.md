# Start here — Praveen

## What is ready

This folder contains your current website code and the information another assistant needs to continue. It does not automatically connect to the live website or inherit this ChatGPT conversation.

## What you need to do next

The private GitHub repository has been created at https://github.com/praveensaini007/24energy-marketplace-dashboard.

1. Clone this repository in Antigravity.
2. Run `python bootstrap.py` to expand the complete source ZIP into the project root.
3. Follow docs/LOCAL_SETUP.md for dependencies, local database and local test login.
4. Commit and push expanded source after validation. The archived docs' earlier GitHub-access blocker describes the pre-upload snapshot; replace that status with the confirmed repository URL in HANDOVER.md.
5. Continue the documented branch and handover routine. Live hosting and live report data remain separate.

## First prompt for Antigravity

> Continue development of the existing 24 ENERGY Marketplace Dashboard. Read AGENTS.md, docs/HANDOVER.md, docs/BUSINESS_RULES.md, docs/LOCAL_SETUP.md and docs/DATA_AND_HOSTING.md first. Preserve the current application and calculation rules. Establish the documented local preview, report which checks actually pass, and tell me any blocked setup steps. Do not replace authentication, expose the app publicly, migrate production data or deploy to a different provider as part of local setup. After each task, update HANDOVER.md with changes, tests, remaining work and the latest commit. Product costs are included in our settlement targets; do not ask for or deduct separate product costs.

## How to switch assistants

Save → update handover → test → commit → push. The other assistant pulls the same branch and reads the handover. A GitHub commit saves code; publishing the live website is a separate action until deployment integration exists.

The app remains here: https://energy-marketplace-pnl.sainipraveen051.chatgpt.site
