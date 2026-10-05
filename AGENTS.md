# Instructions for every development assistant

Read README.md, docs/HANDOVER.md and docs/BUSINESS_RULES.md before editing. The latest explicit user request overrides earlier documentation. Preserve existing work; inspect git status first. Do not rebuild this app from scratch.

- Desired settlement targets already include product cost and desired margin. Current business comparisons use settlement surplus/shortfall, not another product-cost deduction.
- Preserve return definitions, weighted rates, pack multiplication, import deduplication and account-expense allocation. Tests for financial changes must cover missing inputs and double deductions.
- Keep seller isolation. Never accept client-supplied identity headers as verified identity on independently hosted production servers. Sites supplies them through its trusted gateway.
- Keep this repository private. Do not commit credentials, cookies, production DB dumps, R2 backups or source write tokens. Existing data/ files contain confidential seed data.
- Use the pnpm lockfile. Preserve dependency versions unless the task needs a change. Do not replace the stack or add unrelated modules.
- Use a task branch and update docs/HANDOVER.md before stopping. Record actual checks, failures, blocked actions and deployment status separately. Do not claim a GitHub push updates the Sites website.
- Production is still Sites. Do not change .openai/hosting.json project identity, authentication or hosting without an explicitly requested migration.
- Do not run two assistants against the same uncommitted files. Pull/review changes before starting the next task.
- Calculator/ASP work remains deferred. Native integrations for other marketplace report formats require representative files; use the standard template until then.

Validation: `pnpm exec tsc --noEmit`; `node scripts/verify-marketplace.mjs`; `node scripts/verify-performance.mjs`; `node scripts/verify-gmv.mjs`; `pnpm run build`. Run relevant checks after changes; avoid needless repetitions.
