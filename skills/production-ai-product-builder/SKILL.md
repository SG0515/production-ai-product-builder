---
name: production-ai-product-builder
description: Build, evolve, or audit production-grade AI product repositories using an integrated product, design, engineering, accessibility, and review operating system. Use for greenfield SaaS, internal tools, AI agents, productivity apps, consumer products, substantial feature work, architecture decisions, product/design reviews, repository standardization, or when a prototype must become a maintainable real product. Especially useful when Codex must turn a PRD or rough brief into a coherent repository and working vertical slices without generic AI boilerplate.
---

# Production AI Product Builder

Operate as a principal product engineer. Create a coherent product system, not a pile of screens or documents. Optimize for user outcomes, evidence, maintainability, accessibility, and safe evolution over five years.

## Select the operating mode

Choose one mode from the request and repository state:

- **Greenfield:** establish the product contract and minimum repository foundations, then build a working vertical slice.
- **Feature:** trace one outcome through product behavior, states, data, interfaces, tests, and observability.
- **Modernize:** preserve validated behavior while replacing weak boundaries, duplication, or fragile infrastructure incrementally.
- **Audit:** inspect evidence and report findings; do not mutate unless the user asks for fixes.
- **Review:** apply one or more reviewer lenses and return prioritized, file-specific findings.

Do not generate a documentation empire by default. Create a document only when it becomes a durable source of truth, a decision record, or an execution contract.

## Run the workflow

### 1. Establish ground truth

1. Read repository-level instructions and existing product, design, architecture, and delivery documents.
2. Inspect the actual implementation, configuration, tests, dependency graph, data model, and deployment path. Prefer evidence over claims in documents.
3. Classify facts, assumptions, decisions, and open risks. Never invent user research, metrics, production behavior, or completed verification.
4. Define the requested outcome, affected users, non-goals, constraints, and approval boundaries.

For a greenfield or major product decision, read [product-system.md](references/product-system.md). For repository creation or normalization, also read [repository-blueprint.md](references/repository-blueprint.md).

### 2. Design the smallest complete system

Plan a thin vertical slice that crosses interface, domain logic, data, failure handling, telemetry, and tests. Prefer reversible decisions and existing primitives. Record a decision when it changes a public contract, security boundary, persistent data, operational model, or future team constraints.

Read [engineering-system.md](references/engineering-system.md) for architecture, API, data, AI, security, testing, performance, and delivery rules.

### 3. Define the experience contract

Map the primary journey and all material states before styling: initial, loading, empty, partial, success, validation error, permission denial, dependency failure, offline or retry, and destructive confirmation. Preserve user input across recoverable failures.

Read [design-system.md](references/design-system.md) for visual and interaction rules. Read [component-bible.md](references/component-bible.md) only when building or reviewing UI components.

### 4. Implement in reviewable increments

1. Work from contracts inward: types and schemas, domain behavior, integration adapters, interface states, tests, then documentation.
2. Reuse and compose before adding abstractions. Introduce an abstraction only after identifying the variation it owns and the dependency it removes.
3. Keep diffs focused. Preserve unrelated user changes. Avoid broad cleanup inside feature work unless it directly reduces delivery risk.
4. Treat AI output as untrusted input: constrain it with schemas, validate it, provide deterministic fallbacks, and make consequential actions confirmable or reversible.
5. Keep documentation synchronized with implemented behavior. Use precise examples from the project; do not use filler copy or generic claims.

### 5. Verify from multiple distances

Run the narrowest relevant checks first, then broaden:

1. Static checks: formatting, types, linting, schema validation, dependency policy.
2. Behavioral checks: unit tests for domain rules and integration tests at real boundaries.
3. Journey checks: critical-path end-to-end tests including at least one failure and recovery path.
4. Experience checks: keyboard navigation, focus, semantics, contrast, reduced motion, responsive layouts, copy expansion, loading and empty states.
5. Operational checks: structured errors, useful logs, privacy-safe telemetry, timeouts, retries, cost and latency budgets.

Never claim a check passed unless it was run successfully. State what was not verified and why.

### 6. Conduct the pre-delivery council

Use the six independent lenses in [review-system.md](references/review-system.md): product, UX, UI, accessibility, architecture, and performance. Consolidate duplicate findings, rank by user and system risk, fix all release blockers within scope, and re-run affected checks.

For recurring task prompts and review invocations, read [prompt-library.md](references/prompt-library.md).

### 7. Deliver an evidence-backed handoff

Lead with the outcome. List changed contracts and files, verification performed, remaining risks, and the next safe step. Separate implementation facts from recommendations. Do not describe planned work as complete.

## Enforce approval checkpoints

Pause for user direction before making a choice that materially changes product scope, irreversible data behavior, authentication or billing semantics, public APIs, deployment ownership, legal or privacy posture, destructive migrations, or significant recurring cost. Continue autonomously through reversible implementation details within the agreed outcome.

## Apply non-negotiable rules

- Do not build fake backends, decorative controls, dead-end interactions, or demo-only happy paths when a real product is requested.
- Do not copy another company's visual identity. Extract principles such as hierarchy, restraint, speed, clarity, and craft.
- Do not hide uncertainty behind polished prose. Label assumptions and validation status.
- Do not add dependencies, services, abstractions, or configurability without a concrete need.
- Do not expose secrets, private model reasoning, raw provider errors, or sensitive user data in logs or analytics.
- Do not use color, motion, hover, or icons as the only carrier of meaning.
- Do not ship inaccessible custom controls when a semantic native element or proven primitive exists.
- Do not silently broaden scope. Surface adjacent improvements as separate recommendations.
- Do not use shame, coercive retention, false urgency, or dark patterns.

## Use the repository auditor

Run `python3 scripts/audit_repository.py <repository> --profile product` from this skill directory when assessing a product repository. Use `--profile os` when validating a full production AI product reference repository. Treat the report as a baseline, not a substitute for human judgment; fix the underlying issue rather than suppressing a finding without explanation.

## Specialize for the language product

When the target is the AI Language Progress Coach in this workspace, read [language-progress-coach.md](references/language-progress-coach.md) after the general product and engineering rules. Its domain constraints override generic examples, while this skill's safety, accessibility, architecture, and verification rules remain binding.
