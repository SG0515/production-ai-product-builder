# Design system

## 1. Principles

1. **Outcome before ornament:** visual hierarchy must reveal what matters now.
2. **Calm confidence:** use restraint, precise copy, and stable layouts instead of spectacle.
3. **Progressive disclosure:** show essential decisions first and details on demand.
4. **Visible system status:** every action has immediate, truthful feedback.
5. **User control:** consequential AI or destructive actions are explainable, confirmable, and reversible when feasible.
6. **Inclusive by construction:** semantic structure, keyboard operation, contrast, readable type, and reduced motion are design inputs.
7. **Consistent, not monotonous:** shared tokens and patterns support context-specific composition.

Derive quality principles from excellent products; never imitate their trade dress, proprietary assets, distinctive layouts, or copy.

## 2. Token contract

Define semantic tokens before page-specific styling. Keep raw values behind semantic names.

### Color

At minimum define background, surface, elevated surface, foreground, secondary foreground, muted foreground, border, strong border, focus ring, accent, on-accent, positive, warning, destructive, and information roles. Provide light and dark values. Test text and non-text contrast in actual component states. Do not encode status through color alone.

### Typography

Use a restrained type scale with explicit roles for display, page title, section heading, body, label, caption, and code or numeric data. Set line height, weight, tracking, and maximum line length. Support target scripts and at least 30% interface copy expansion. Avoid ultra-light weights and tiny muted text.

### Spacing and grid

Use a base rhythm, typically 4 px with common increments at 8, 12, 16, 24, 32, 48, and 64 px. Define content widths, gutters, columns, and breakpoint behavior from content pressure rather than device names. Dense tools may use a tighter component rhythm while preserving touch targets.

### Shape, depth, and borders

Use a small radius scale and a limited depth model. Borders should organize; shadows should communicate elevation, not decorate every container. Avoid nested rounded cards when grouping and whitespace are sufficient.

### Motion

Define durations by purpose: immediate feedback, local transition, and large spatial change. Use standard easing consistently. Animate opacity and transform when possible. Preserve spatial continuity, avoid layout-shifting hover effects, and honor `prefers-reduced-motion` with a usable non-animated path.

### Iconography

Use one coherent SVG icon family. Pair unfamiliar or consequential icons with labels. Give icon-only controls accessible names and adequate targets. Do not use emoji as functional icons.

## 3. Responsive behavior

Design behavior, not snapshots. Specify:

- which regions reflow, collapse, scroll, wrap, or become overlays;
- minimum readable and interactive sizes;
- how tables expose priority columns and secondary details;
- how navigation remains reachable;
- how virtual keyboards, safe areas, long translations, and zoom affect layouts;
- how comparison or creation tasks work without forcing desktop width.

Verify representative widths around 375, 768, 1024, and 1440 px, plus intermediate stress points. Never hide required functionality solely because the viewport is small.

## 4. Page patterns

### Landing pages

State the product promise in user language, name the target situation, demonstrate the mechanism with credible evidence, address material objections, and provide one primary next step. Avoid fictional logos, fabricated testimonials, invented metrics, and vague superlatives.

### Dashboards

Prioritize decisions and exceptions over vanity summaries. Use progressive detail, legible time ranges, explicit freshness, and meaningful empty states. A dashboard should answer “what changed, why it matters, and what can I do?”

### Forms

Use persistent labels, logical grouping, appropriate input types, inline validation after meaningful interaction, and error summaries for long forms. Preserve values after failure. Explain formatting and sensitive-data use before submission. Avoid disabling submission when users cannot discover the reason.

### Tables

Use tables for comparison across repeated fields. Provide clear headers, semantic markup, alignment by data type, sorting state, selection feedback, overflow strategy, and empty/loading/error behavior. Do not turn dense data into decorative cards on desktop.

### Navigation and search

Reflect user mental models and stable information architecture. Indicate current location. Preserve search queries and filters across result inspection. Distinguish no results from load failure. Make keyboard behavior and focus transitions predictable.

### Settings

Group by user intent. Explain consequences, current value, save model, and scope. Separate reversible preferences from security, data deletion, billing, or account ownership actions.

### Charts

Use a chart only when it reveals a relationship more clearly than prose or a compact table. Label units and time windows, provide accessible summaries, expose exact values, distinguish missing from zero, and avoid misleading axes or decorative 3D treatments.

## 5. State completeness

Every interactive surface must define, when applicable:

- untouched and focused;
- hover without hover dependency;
- pressed and selected;
- disabled with an understandable reason;
- loading with stable geometry;
- empty with context and next action;
- partial data;
- success with durable confirmation;
- validation and system errors;
- retry, offline, timeout, and permission denial;
- destructive confirmation and post-action undo.

Skeletons should resemble final geometry, avoid flashing for fast responses, and never mask a stalled operation indefinitely.

## 6. Accessibility acceptance

- Use semantic landmarks and a logical heading structure.
- Ensure the complete journey is keyboard operable with visible focus.
- Manage focus for dialogs, route changes, errors, and inserted content.
- Expose programmatic names, roles, values, descriptions, and error relationships.
- Meet WCAG AA contrast and reflow expectations for the target conformance level.
- Provide text alternatives and transcripts appropriate to content purpose.
- Support zoom, text resizing, reduced motion, high contrast, and screen readers.
- Avoid time limits; when essential, warn and allow extension.
- Test with automation and manual keyboard/screen-reader spot checks.

## 7. Design anti-patterns

- Multiple competing primary actions.
- Glass, gradients, glow, and oversized hero type used as default “AI” styling.
- Placeholder copy that evades the product decision.
- Cards for every piece of content.
- Hidden controls revealed only on hover.
- Motion that delays work or communicates meaning without an alternative.
- Fixed heights that clip localized or user-generated content.
- Modals for multi-step work that needs navigation, history, or recovery.
- Toasts as the only record of important failure or success.
