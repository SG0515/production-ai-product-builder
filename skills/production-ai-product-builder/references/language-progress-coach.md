# AI Language Progress Coach specialization

Apply these constraints after reading the current PRD and project design system. Repository evidence and the newest explicitly approved decisions take precedence over older snapshots.

## Product invariant

The product is an AI progress coach, not another fixed course or generic chatbot. It helps a learner decide the next effective action, coordinate existing resources, produce evidence of learning, and recover after interruption without shame or learning debt.

## Core domain boundaries

Keep these concepts distinct in types, storage, analytics, and UI:

- `interfaceLocale`: product navigation and system copy;
- `explanationLocale`: coach explanations and instructions;
- `targetLanguage`: the language being learned;
- activity completion: whether a task was done;
- capability evidence: what the learner demonstrated;
- momentum: ability to start, continue, or recover;
- plan: current proposed sequence;
- plan revision: reasoned delta with autonomy level and reversibility.

Never infer mastery solely from completion. Never change the target language when the interface locale changes.

## Experience architecture

Use a stable shell plus a constrained dynamic workspace. Navigation, goal context, progress context, locale control, and coach access remain stable. The workspace selects from typed, tested components based on learning state. A model may choose content and component schema within policy; it must not emit arbitrary executable UI.

Model at least these states:

1. initial diagnosis and editable understanding summary;
2. today's normal task;
3. limited-time or low-energy minimum effective task;
4. interruption detection and recovery choice;
5. targeted micro-teaching for a blocker;
6. evidence collection appropriate to the skill;
7. feedback separating completion from demonstrated ability;
8. transparent plan adjustment with before, after, reason, and impact;
9. weekly review;
10. Day 30 learning playbook and next 30/60/90-day path.

## Autonomy policy

- Low-impact, reversible sequencing changes may apply automatically and must expose undo.
- Changes to goals, deadlines, weekly capacity, learning language, material resource commitments, or data-sharing require confirmation.
- Low-confidence recommendations should present alternatives or ask for missing context.
- The learner can inspect, edit, and delete durable memory.

## Evidence policy

Choose evidence by capability:

- vocabulary: recognition plus recall or contextual use;
- grammar: discrimination plus transfer into a new context;
- listening: comprehension at a declared audio condition;
- speaking: intelligibility and task success, with uncertainty disclosed;
- external resource: a short probe or reflection, not a completion checkbox.

Store the prompt or task context, learner response, evaluation method, confidence, and limitations necessary to interpret an evidence record. Do not present a single probabilistic evaluation as objective truth.

## Recovery policy

Detect interruption against the learner's personal cadence, not a universal streak. Do not require repayment of missed tasks. Merge, defer, or remove work according to goal relevance, dependency, evidence, and current capacity. Recovery copy is calm and choice-preserving; avoid red-alert styling, streak resets, guilt, and false urgency.

## First vertical slice

Use the approved travel-Japanese scenario only if it remains the current showcase: a learner traveling in 30 days, familiar with kana, using YouTube and Anki, interrupted for three days, available for ten minutes, and blocked on `は / が`.

The slice is complete only when it persists the learner context, adapts the next task, teaches or routes to a relevant resource, collects transfer evidence, explains the result, records a transparent plan delta, supports one failure and retry path, and preserves the separation of interface, explanation, and target language.

## Domain review gates

- One obvious next learning action per state.
- The interface explains why the recommendation fits the current goal and constraints.
- Generated activities and evaluations follow schemas and have safe fallbacks.
- Learning claims are proportional to evidence and confidence.
- Locale switching preserves the workspace, response, task identity, and target language.
- The primary journey works with keyboard and screen reader and at narrow widths.
- Personal learning data has visible memory, deletion, and retention behavior.
- Metrics distinguish recovery, activity completion, evidence generation, and demonstrated progress.
