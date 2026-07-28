# Engineering system

## 1. Architecture principles

- Organize around stable domain responsibilities, not framework fashions.
- Keep policy and business rules independent from transport, storage, model providers, and UI frameworks.
- Make dependencies point inward toward domain contracts.
- Prefer a modular monolith until independent scaling, ownership, reliability, or security needs justify distribution.
- Use explicit schemas at every process, network, persistence, and AI boundary.
- Make invalid states hard to represent and consequential transitions auditable.
- Choose boring, supported technology when it satisfies the constraint.

Document decisions that alter public interfaces, persistence, trust boundaries, deployment topology, operational ownership, or long-lived constraints. A decision record includes context, options, decision, consequences, and reversal path.

## 2. Implementation workflow

1. Trace the target behavior through UI, domain, storage, integrations, and operations.
2. Define contracts and failure semantics before adapters.
3. Implement the smallest end-to-end slice behind a safe migration or feature boundary when needed.
4. Test domain rules without infrastructure and boundaries with representative infrastructure.
5. Instrument outcomes, failures, latency, and cost without collecting unnecessary personal data.
6. Review the diff for duplication, accidental public contracts, migration safety, and documentation drift.

Keep functions focused, names domain-specific, and modules cohesive. Prefer composition. Do not create `utils`, `helpers`, `common`, or `shared` dumping grounds; name the capability they own.

## 3. API and schema policy

- Validate inputs at the boundary and return stable, documented error semantics.
- Separate transport DTOs from domain objects when their change pressures differ.
- Use idempotency for retried writes and external side effects.
- Define pagination, sorting, filtering, time zones, units, nullability, and versioning explicitly.
- Do not leak stack traces, provider payloads, database details, or authorization rules.
- Treat backward compatibility as a product decision; provide migration windows for external consumers.

## 4. Data policy

- Collect the minimum data needed for the product promise.
- Define ownership, retention, deletion, export, and residency expectations.
- Use migrations that are observable, reversible where feasible, and safe for mixed application versions.
- Protect invariants with database constraints as well as application logic.
- Avoid destructive schema changes in the same release that stops writing the old shape.
- Back up before material migrations and verify restore procedures proportionate to risk.

## 5. Authentication and authorization

- Use established identity libraries or providers rather than custom cryptography or session protocols.
- Enforce authorization server-side on every protected resource and action.
- Model tenant, role, ownership, and impersonation boundaries explicitly.
- Rotate and scope secrets; never commit or log them.
- Use secure cookie, CSRF, redirect, origin, and token settings appropriate to the architecture.
- Make account recovery and session revocation observable and abuse-resistant.

## 6. AI subsystem policy

Treat a model as a probabilistic dependency, not the product's authority.

- Define typed input and output schemas and reject malformed output.
- Separate system policy, task instructions, retrieved context, user content, and tool results.
- Minimize and authorize tool access. Confirm high-impact actions.
- Defend against prompt injection at trust boundaries; retrieved or user-authored text is data, not policy.
- Provide timeouts, cancellation, bounded retries, rate limits, and deterministic fallbacks.
- Track model, prompt or policy version, latency, token usage, cost, validation failures, and user-visible outcomes.
- Build representative evaluation sets from real task classes and hard cases; avoid judging only fluent prose.
- Preserve user agency: expose what the system changed, why, and how to correct or undo it.
- Never display hidden chain-of-thought. Provide concise user-facing rationale or evidence instead.

## 7. Testing policy

Use a risk-shaped test portfolio:

- **Unit:** domain decisions, state transitions, parsers, calculations, and policy.
- **Contract:** APIs, events, schemas, provider adapters, and persisted formats.
- **Integration:** database behavior, authentication, queues, files, and external service boundaries.
- **End-to-end:** critical user outcomes and their highest-value failure/recovery paths.
- **Accessibility:** automated rule checks plus manual keyboard and screen-reader sampling.
- **AI evaluation:** schema validity, task success, safety, regression, latency, and cost on versioned cases.

Tests must be deterministic enough to diagnose. Avoid asserting implementation details or mocking the behavior being tested. Every fixed defect should gain a regression test when practical.

## 8. Performance and reliability

Set budgets from user experience and operating economics. Measure server and client latency percentiles, error rate, saturation, payload size, render stability, model latency, token usage, and external dependency behavior.

- Cache only with explicit freshness and invalidation semantics.
- Bound concurrency, payloads, queues, and retries.
- Use backoff with jitter and idempotency for retryable operations.
- Degrade optional capabilities before critical paths.
- Make loading honest and cancellation possible for long operations.
- Avoid premature micro-optimization; fix measured bottlenecks without compromising correctness.

## 9. Observability

Use structured events with correlation identifiers across boundaries. Logs explain failures; metrics show system health; traces show latency and dependency paths; product events show user outcomes. Redact sensitive fields by default. Alerts must map to user impact and a concrete response.

## 10. Git and delivery

- Keep commits small, coherent, and independently understandable.
- Do not mix generated artifacts, formatting churn, and behavior changes without need.
- Never rewrite or discard another person's work without explicit permission.
- Review migrations, dependency changes, public contracts, and security-sensitive code with extra scrutiny.
- Use continuous integration for formatting, types, tests, build, security and dependency checks appropriate to the stack.
- Define deployment, rollback, configuration, secrets, and environment parity before calling the system production-ready.

## 11. Forbidden engineering behavior

- Fake persistence, fake success, or hidden in-memory state in a real product path.
- Unbounded model or network calls.
- Swallowed exceptions and catch-all fallbacks that report success.
- Business logic duplicated across UI and API.
- Authorization inferred from hidden UI controls.
- Environment-specific constants committed into application logic.
- A generic abstraction added for a single speculative future use.
- Tests deleted or weakened to make a change pass.
- Dependency upgrades unrelated to the requested outcome.
