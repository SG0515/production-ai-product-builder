# Production AI Product Builder

A Codex skill for building, evolving, and auditing maintainable production-grade AI products. It combines product judgment, UX and design-system rules, software architecture, AI safety boundaries, accessibility, performance, testing, and release review in one reusable operating workflow.

## What it provides

- A principal-level workflow for greenfield products, major features, modernization, audits, and reviews.
- Product, design, engineering, component, and repository standards loaded only when needed.
- Six release-review lenses: product, UX, UI, accessibility, architecture, and performance.
- Specialized rules for the AI Language Progress Coach.
- A deterministic repository auditor for required product foundations and unfinished content.

## Repository layout

```text
skills/production-ai-product-builder/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/audit_repository.py
```

The GitHub documentation lives at the repository root so the skill package itself stays compliant and contains only execution resources.

## Install for Codex

Clone this repository, then copy the skill directory into your Codex skills directory:

```bash
git clone https://github.com/SG0515/production-ai-product-builder.git
cp -R production-ai-product-builder/skills/production-ai-product-builder ~/.codex/skills/
```

Start a new Codex task so the installed skill is discovered.

## Invoke

```text
$production-ai-product-builder Turn this PRD into a production-ready implementation plan and repository.
```

The skill can also trigger implicitly for substantial AI product builds, architecture work, repository standardization, or production-readiness audits.

## Validate

Use Codex's skill validator against the skill directory. To audit a product repository with the bundled baseline checker:

```bash
python3 skills/production-ai-product-builder/scripts/audit_repository.py /path/to/repository --profile product
```

Use `--profile os` when validating a full production AI product reference repository.
