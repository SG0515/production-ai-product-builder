# Product system

## 1. Product contract

Write a product contract before a major build:

- **User:** a behaviorally specific segment, not a demographic cloud.
- **Struggle:** the recurring situation that blocks progress today.
- **Desired progress:** the observable change the product helps create.
- **Trigger:** the moment the user is motivated to seek help.
- **Promise:** one sentence the experience must consistently keep.
- **Non-goals:** attractive adjacent problems intentionally excluded.
- **Evidence:** what would prove the user obtained value.
- **Risks:** assumptions that could invalidate desirability, usability, viability, feasibility, or responsibility.

Label every important statement as observed fact, measured result, stakeholder decision, or hypothesis. A polished hypothesis is still a hypothesis.

## 2. MVP discipline

An MVP is the smallest complete learning system, not the smallest screen count. It must let a real target user enter with a real problem, reach the promised outcome, recover from predictable failure, and leave usable evidence.

Include only capabilities that are necessary to:

1. reach the first meaningful outcome;
2. verify that the outcome happened;
3. learn about the riskiest assumption;
4. operate the experience safely.

Defer breadth, automation, personalization, settings, and edge-case flexibility until evidence justifies them. Never defer security, data integrity, basic accessibility, or a credible failure path.

## 3. Prioritization

Evaluate candidate work across:

| Dimension | Question |
|---|---|
| Outcome | Does this materially improve the promised user result? |
| Evidence | Does it test a critical assumption or improve decision quality? |
| Reach | How many target journeys are affected? |
| Risk reduction | Does it reduce safety, trust, architecture, or delivery risk? |
| Cost | What implementation and ongoing complexity does it create? |
| Reversibility | Can the decision be changed after learning? |
| Strategic fit | Does it strengthen the product's chosen advantage? |

Prefer work with high outcome or risk-reduction value and low irreversible cost. Do not hide subjective estimates inside a mathematically precise score.

## 4. Journey and state model

For each primary journey, define:

1. entry condition and user intent;
2. information required from the user;
3. system decision and its explanation;
4. primary action and expected feedback;
5. success evidence;
6. recoverable errors and preserved state;
7. exit, continuation, and re-entry behavior.

Map novice, returning, interrupted, low-data, low-confidence, and permission-constrained users when relevant. A dashboard is not a journey; it is a surface within one.

## 5. Conversion, onboarding, and retention

Reduce time to credible value. Ask only for information needed to improve the next decision. Prefer progressive profiling and editable summaries over long questionnaires. Explain why sensitive inputs are needed.

Earn retention through recurring utility:

- preserve context so users do not repeat work;
- make progress legible without inflating it;
- provide an obvious next action;
- help users recover after interruption;
- let users control reminders, memory, and automation.

Never use forced continuity, punishment, hidden cancellation, artificial scarcity, or misleading defaults.

## 6. Measurement

Select one North Star outcome with:

- a clear unit of value;
- a defined eligible population;
- a time window;
- an observable event or evidence threshold;
- guardrails for quality, safety, and gaming.

Pair it with leading indicators for activation and repeated value, diagnostic indicators for failure, and guardrails for trust, accessibility, latency, cost, and negative outcomes. Define event semantics before instrumentation. Avoid metrics that reward clicks, generated content, or time spent when these are not user value.

## 7. Feature evaluation questions

Before approving a feature, answer:

- Which user and situation is it for?
- What existing behavior does it replace or improve?
- What must be true for it to work?
- What is the simplest complete test?
- What new failure, abuse, or confusion can it create?
- What data is collected, retained, inferred, or exposed?
- What will indicate success, harm, or indifference?
- How is it removed or changed if the hypothesis fails?

## 8. Product review checklist

- The promise, user, and first meaningful outcome are unambiguous.
- The primary action is clear in each state.
- Completion is distinguished from actual outcome evidence.
- User input and work survive recoverable failure.
- AI recommendations expose reason, confidence, and control at the level consequences require.
- Empty, loading, error, interrupted, and returning experiences are designed.
- The product does not overclaim intelligence, certainty, or progress.
- Metrics measure value and include trust guardrails.
- Non-goals prevent accidental platform expansion.

## 9. Product anti-patterns

- Feature lists without a behavioral model.
- Personas invented from stereotypes.
- Onboarding that explains every feature before value.
- Engagement treated as the outcome.
- AI chat added where a structured workflow is clearer.
- Personalization without editability or explanation.
- Roadmaps presented as commitments despite unresolved assumptions.
- Success states that celebrate system activity rather than user progress.
