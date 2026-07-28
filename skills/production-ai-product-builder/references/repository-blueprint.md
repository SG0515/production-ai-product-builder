# Repository blueprint

Use this blueprint to create a durable product repository. Adapt it to the product and stack; do not create empty directories or generic documents merely to match the tree.

## Root contracts

- `README.md`: product promise, current status, architecture map, verified local setup, quality commands, environment model, and documentation navigation.
- `AGENTS.md`: concise instructions that change how coding agents plan, implement, verify, review, document, and seek approval in this repository.
- `CODEX.md`: include only when Codex-specific usage differs materially from `AGENTS.md`; otherwise keep one source of truth.
- `PRODUCT.md`: target user, struggle, promise, outcome metrics, scope, non-goals, core journeys, assumptions, and decision history links.
- `DESIGN.md`: experience principles, semantic tokens, layout and responsive rules, component and state contracts, accessibility, content voice, and design anti-patterns.
- `CONTRIBUTING.md`: supported workflow, quality gates, change types, decision records, review expectations, and code of conduct link.
- `LICENSE`: an explicit license selected by the repository owner. Never guess legal intent; request the choice when it has not been made.
- `CHANGELOG.md`: include only when the project publishes versions; use released facts, not a speculative roadmap.

## Durable documentation

```text
docs/
  architecture/       system context, boundaries, runtime and data flows
  decisions/          immutable architecture or product decision records
  operations/         deployment, rollback, incidents, backup and restore
  product/            research evidence, journey definitions, metrics
  security/           threat model, privacy and data lifecycle
  quality/            test strategy, accessibility and performance budgets
design-system/        tokens, foundations and implementation guidance
component-bible/      shared component contracts when the UI surface warrants it
prompt-library/       versioned task prompts and evaluation links for AI systems
review/               reviewer specifications and release review records
references/           externally sourced or stable domain references
templates/            issue, decision, test, or review templates that are actually reused
examples/             runnable, maintained examples with clear ownership
scripts/              deterministic repository tasks with help and failure semantics
.github/               workflows and contribution forms used by the project
```

Keep navigational index files only where the directory would otherwise be hard to understand. Split long documents by responsibility, not arbitrary page length. Avoid duplicated rules across `AGENTS.md`, `CODEX.md`, and nested instructions; the nearest applicable instruction should add local constraints.

## Agent instruction contract

An effective `AGENTS.md` is compact and operational. Include:

1. the product invariant and repository map;
2. commands verified in this repository;
3. planning threshold and evidence-gathering workflow;
4. implementation rules and architectural boundaries;
5. testing policy by risk;
6. UI, accessibility, performance, security, and documentation gates;
7. git and generated-file policy;
8. forbidden behaviors;
9. approval checkpoints.

Do not restate general model capabilities, include motivational prose, or list commands that do not work.

## Prompt library contract

Treat prompts as versioned product assets when they influence behavior. Each production prompt records purpose, inputs, output schema, context policy, failure behavior, safety constraints, evaluation cases, owner, and version. Keep model-provider configuration separate from task policy. Never store secrets or private production data in example prompts.

## Configuration contract

- Pin or constrain runtime and package versions intentionally.
- Provide an example environment file containing names and safe descriptions, never live credentials.
- Validate configuration at startup with actionable errors.
- Separate local, test, staging, and production behavior explicitly.
- Keep formatting, lint, type, test, build, and security commands deterministic and CI-aligned.
- Configure dependency updates and secret scanning appropriate to the repository's exposure.

## Readiness levels

### Foundation-ready

The product contract, architecture boundary, local setup, critical path, and basic quality gates are real and consistent.

### Beta-ready

Critical journeys include recovery paths; authentication, privacy, accessibility, observability, deployment, and rollback have been exercised in a production-like environment.

### Production-ready

Reliability targets, security review, operational ownership, backups and restore, incident handling, performance budgets, data lifecycle, and user support are verified. A polished local demo is not production readiness.

## Structural review

Before completion, check:

- Can a new contributor find the product promise, architecture, and commands in five minutes?
- Is each policy owned in one obvious location?
- Do documents describe the implementation that exists?
- Are decisions separated from temporary plans?
- Are generated artifacts identifiable and reproducible?
- Can critical behavior be changed without editing unrelated modules?
- Are the test and deployment paths part of normal development rather than tribal knowledge?
