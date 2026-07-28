# Prompt library

Use these as task frames, not as substitutes for repository evidence. Replace bracketed context with real project facts before use.

## UI implementation

“Implement the [journey/state] using the repository's existing design primitives. First inventory reusable components and tokens. Cover loading, empty, partial, success, validation, dependency failure, keyboard, reduced-motion, responsive, and long-copy behavior. Do not add a new primitive unless an existing one cannot satisfy the documented contract. Verify the critical interaction, not only the render.”

## Frontend and React

“Trace [feature] from route and server state to interaction and telemetry. Keep domain decisions outside presentational components, derive rather than duplicate state, preserve input across recoverable errors, and avoid client JavaScript where server rendering is sufficient. Add focused tests for the highest-risk transition and failure path.”

## Next.js

“Implement [feature] using the repository's selected Next.js routing and data model. Make server/client boundaries explicit, keep secrets and authorization on the server, define caching and revalidation semantics, handle streaming or pending UI without layout instability, and verify build plus the critical route behavior.”

## TypeScript

“Model [domain behavior] with explicit types and boundary validation. Avoid `any`, unchecked assertions, ambiguous nullable states, and transport types leaking into the domain. Prove exhaustive transition handling with focused tests.”

## Backend and API

“Design [capability] as a domain contract before selecting transport details. Specify authenticated actor, authorization rule, validated request, response, stable errors, idempotency, concurrency behavior, observability, and data lifecycle. Implement the smallest complete path with contract and integration tests.”

## Database

“Evolve the data model for [behavior]. State invariants, ownership, query patterns, indexes, retention, deletion, and migration compatibility. Use a staged migration for destructive or shape-changing work, verify representative queries, and document rollback or forward-fix behavior.”

## Authentication

“Implement or review [auth flow] using established security primitives. Threat-model account discovery, session theft, CSRF, redirect abuse, brute force, recovery, tenant crossing, and privilege escalation. Enforce authorization server-side and add negative tests.”

## AI capability

“Define [AI behavior] as a constrained subsystem. Specify the user outcome, input and output schemas, trusted and untrusted context, tool permissions, confirmation threshold, timeout, retry, fallback, observability, cost budget, and evaluation cases. Do not let generated text become executable policy or UI code.”

## Testing

“Build a risk-based test plan for [change]. Map each material failure to the cheapest reliable test layer. Prioritize domain invariants, real boundaries, authorization negatives, recovery, accessibility, and one critical end-to-end journey. Avoid redundant tests and assertions tied to implementation detail.”

## Performance

“Profile [journey] using representative data and device constraints. Report the dominant latency, rendering, payload, query, memory, or model-cost contributors with evidence. Propose the smallest changes that meet an explicit budget and describe regression checks.”

## Accessibility

“Review the complete [journey] for semantic structure, keyboard order, visible focus, names and relationships, errors, announcements, contrast, zoom/reflow, target size, reduced motion, and screen-reader operation. Return reproducible findings with severity and verification.”

## Refactoring

“Refactor [area] to remove [specific change friction or defect] while preserving documented behavior. Characterize current behavior, identify the boundary to improve, make incremental changes, and keep the diff free of unrelated cleanup. Demonstrate preservation with tests and explain the tradeoff.”

## Debugging

“Diagnose [symptom] from a minimal reproduction and observed evidence. Separate cause from correlated noise, trace state and boundaries, and identify the smallest falsifiable hypotheses. Report the root cause and proof; implement a fix only if requested.”

## Architecture review

“Review [system/change] for domain ownership, dependency direction, public contracts, persistence, trust boundaries, failure behavior, observability, operability, and reversibility. Return prioritized findings grounded in files, flows, or traces. Distinguish current defects from optional future improvements.”

## Product review

“Review [feature/PRD] against the target user, struggle, promise, non-goals, first meaningful outcome, evidence, recovery, trust, and measurement. Identify assumptions presented as facts and features that do not advance the outcome. Recommend the smallest complete learning loop.”

## Design review

“Review [surface] for hierarchy, information density, state completeness, responsive behavior, content clarity, token consistency, accessibility, and fit with the user journey. Do not score aesthetic preference. Return evidence-backed issues and a small set of coherent improvements.”

## Code review

“Review this diff for user-visible regressions, incorrect domain behavior, unsafe data or authorization changes, weak failure handling, concurrency issues, accessibility regressions, missing risk-shaped tests, and unnecessary complexity. Findings first, ordered by severity, with exact evidence and remediation.”
