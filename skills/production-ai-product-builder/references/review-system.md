# Review system

Run each relevant reviewer independently before consolidation. Review implemented evidence, not intent. A reviewer should not redesign the whole product when a focused fix resolves the issue.

## Severity

- **P0 — Release blocker:** likely data loss, security or privacy breach, inaccessible critical path, systemic outage, or product behavior that can materially harm users.
- **P1 — Major:** critical journey failure, serious confusion, broken recovery, substantial performance regression, or architecture defect that makes the feature unsafe to evolve.
- **P2 — Moderate:** meaningful friction, inconsistency, maintainability debt, or edge-case failure with a contained workaround.
- **P3 — Minor:** polish or local clarity issue with low user and system impact.

Every finding must include severity, evidence location, affected user or system behavior, why it matters, and the smallest credible remediation. Do not report preferences as defects.

## Product reviewer

**Mission:** verify that the system solves the declared user problem and measures real value.

Check promise-to-behavior alignment, target user clarity, outcome evidence, non-goals, onboarding time to value, retention utility, ethical defaults, metric validity, and whether AI is necessary and appropriately controlled.

## UX reviewer

**Mission:** verify that users can understand, complete, recover from, and return to the primary journey.

Check information architecture, task sequence, cognitive load, system feedback, error recovery, input preservation, empty and interrupted states, progressive disclosure, language clarity, and continuity across viewport or session changes.

## UI reviewer

**Mission:** verify visual hierarchy, consistency, responsive behavior, and interaction-state completeness.

Check tokens, typography, spacing rhythm, alignment, affordance, density, responsive reflow, long content, icon consistency, state styling, and whether decoration competes with the primary task.

## Accessibility reviewer

**Mission:** verify equitable operation of the complete critical path.

Check semantics, names and relationships, keyboard order, visible focus, overlay focus management, announcements, contrast, reflow, zoom, target size, reduced motion, alternatives for sensory content, error identification, and time limits. Include manual checks; automation alone is insufficient.

## Architecture reviewer

**Mission:** verify correct boundaries, reliable failure behavior, safe data handling, and future changeability.

Check domain ownership, dependency direction, duplicated rules, schema validation, authorization, migration compatibility, idempotency, AI trust boundaries, secret handling, observability, dependency justification, tests at real boundaries, and rollback path.

## Performance reviewer

**Mission:** verify that the product remains responsive, resource-efficient, and predictable under realistic conditions.

Check client bundle and rendering, payloads, caching semantics, database access, concurrency, network waterfalls, model token and latency budgets, cancellation, retry amplification, external dependency degradation, Core Web Vitals where applicable, and performance measurement on representative devices and data.

## Output format

Return findings first, ordered by severity:

```text
[P1] Short actionable title
Evidence: file, line, route, state, trace, or reproducible action
Impact: affected user/system behavior
Reason: why this violates the product or engineering contract
Fix: smallest credible remediation
Verification: check that would prove the fix
```

Then state:

- assumptions and review gaps;
- checks performed;
- a concise release recommendation: block, conditional, or ready.

If there are no actionable findings, say so and identify residual untested risk. Do not manufacture findings to fill a template.
