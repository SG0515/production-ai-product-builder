# Component bible

Use this contract for shared components. A component entry must state purpose, suitable and unsuitable use, variants, anatomy, states, responsive behavior, accessibility, interaction, motion, content rules, and common mistakes.

## Actions

### Button

- **Purpose:** trigger an immediate action.
- **Use:** submit, create, confirm, retry, or open a task surface.
- **Do not use:** navigation to another location; use a link.
- **Variants:** primary, secondary, quiet, destructive, icon-only; size variants follow density, not hierarchy.
- **Behavior:** preserve label width during progress when possible; prevent duplicate submissions while communicating activity.
- **Accessibility:** semantic `button`, visible focus, accessible name, disabled reason when material, minimum practical target size.
- **Motion:** fast color or elevation feedback; no layout-changing scale.
- **Mistakes:** several primary buttons, ambiguous verbs, icons without names, disabling before validation guidance.

### Link

- **Purpose:** navigate to a resource or location.
- **Variants:** inline, standalone, navigational, external, download.
- **Accessibility:** meaningful text independent of surrounding context; indicate external behavior when surprising.
- **Mistakes:** buttons styled as links for mutations, “click here,” opening new tabs without reason.

### Menu and command palette

- **Purpose:** expose secondary actions or fast navigation.
- **Use:** related action sets; expert cross-product access for command palettes.
- **Do not use:** hide the only route to a primary action or place form-like workflows inside a menu.
- **Behavior:** arrow-key navigation, typeahead where useful, escape closes, focus returns to trigger.
- **Mistakes:** nested menus on touch, destructive actions without separation, searchable palette with invisible scope.

## Inputs

### Text field and textarea

- **Purpose:** collect free-form or constrained text.
- **Variants:** plain, search, password, numeric, with prefix or suffix.
- **Behavior:** persistent label, optional guidance, validation after meaningful interaction, preserved value on failure.
- **Accessibility:** associated label, described errors and requirements, correct autocomplete and input mode.
- **Responsive:** allow text zoom and virtual keyboard visibility; textarea grows within sensible limits.
- **Mistakes:** placeholder as label, masking formatting rules, rejecting pasted text, inaccessible character counters.

### Select, combobox, radio, checkbox, and switch

- **Use select:** choose one option from a longer stable list.
- **Use combobox:** search or create within a large option set.
- **Use radio:** compare a small set of mutually exclusive choices.
- **Use checkbox:** select independent items or acknowledge a statement.
- **Use switch:** apply an immediate binary setting, not submit a form choice.
- **Accessibility:** prefer native controls; group names, selected states, keyboard behavior, and error relationships must be programmatic.
- **Mistakes:** custom dropdowns without full keyboard support, switch for destructive behavior, disabled options without explanation.

### Date, time, file, and rich input

- **Behavior:** accept locale-aware keyboard entry as well as picker interaction. Show constraints before selection. Validate file type, size, and upload state. Keep rich editors operable without pointer precision.
- **Mistakes:** calendar-only entry, ambiguous time zones, upload progress without cancellation, editor toolbar without names or shortcuts.

## Information

### Card

- **Purpose:** group one coherent object or option.
- **Do not use:** as a default wrapper for every section.
- **Variants:** static, interactive, selectable, metric, media.
- **Behavior:** if the whole card is interactive, preserve valid nested interaction and a clear focus model.
- **Mistakes:** nested cards, decorative shadow stacks, clickable appearance on static content.

### Table and list

- **Use table:** repeated records compared across the same fields.
- **Use list:** records scanned primarily by identity or sequence.
- **Behavior:** sorting and selection are explicit; bulk actions disclose scope; loading does not reorder unexpectedly.
- **Responsive:** prioritize fields, allow controlled horizontal scroll, or expose row details; do not silently drop required data.
- **Accessibility:** semantic headers, captions where needed, announced sort state and selection count.

### Badge, status, tooltip, and callout

- **Badge:** compact category or state, with text as well as color.
- **Status:** current operational state with timestamp or freshness when relevant.
- **Tooltip:** brief supplementary explanation, never required instructions or interactive content.
- **Callout:** contextual information, warning, success, or next action.
- **Mistakes:** badge overload, stale status without timestamp, hover-only tooltip, permanent success toast instead of durable state.

### Empty, loading, skeleton, and error states

- **Empty:** distinguish first use, filtered absence, permission absence, and cleared history; explain context and next action.
- **Loading:** show what is happening and preserve stable layout; offer cancel when meaningful.
- **Skeleton:** mirror likely geometry and avoid rapid flashes.
- **Error:** state what failed, impact, preserved work, recovery, and support path when necessary.

## Navigation

### Header, sidebar, tabs, breadcrumbs, and pagination

- **Header:** stable global identity and highest-value utilities.
- **Sidebar:** persistent navigation for broad desktop information architecture; collapses without losing discoverability.
- **Tabs:** peer views of the same context, not sequential steps or unrelated pages.
- **Breadcrumbs:** location in a hierarchy, not browsing history.
- **Pagination:** navigate bounded result pages; retain filters, sort, and return position.
- **Accessibility:** current location or selected tab is programmatic; tab keyboard behavior follows the established pattern.
- **Mistakes:** mobile hamburger with no information scent, tabs wrapping unpredictably, breadcrumb as a back button.

### Search and filters

- **Behavior:** preserve query, reveal active scope, make filter chips removable, distinguish no results from failure, and provide clear reset.
- **Accessibility:** results updates are announced without stealing focus; suggestions are keyboard navigable.
- **Mistakes:** search on every keystroke without cancellation, hidden active filters, empty result state that erases the query.

## Overlays and feedback

### Dialog, drawer, popover, toast

- **Dialog:** focused decision or compact task requiring temporary modality.
- **Drawer:** contextual detail or editing that benefits from retaining page context.
- **Popover:** lightweight non-modal content anchored to a trigger.
- **Toast:** transient acknowledgement for non-critical information with a durable state elsewhere.
- **Accessibility:** label overlays, trap focus only when modal, escape closes when safe, restore focus, prevent background interaction for modality.
- **Responsive:** dialogs may become full-screen sheets when needed; critical controls remain visible above safe areas and keyboards.
- **Mistakes:** long workflows in modals, nested overlays, destructive confirmation with vague labels, toasts containing essential recovery details.

## Domain visualization

### Progress and charts

- **Purpose:** communicate change, relationship, distribution, or completion against a meaningful target.
- **Do not use:** to reward activity that is not outcome progress.
- **Accessibility:** textual summary, exact values, labeled axes and units, non-color distinctions.
- **Mistakes:** false precision, unlabeled normalization, missing data shown as zero, celebration that overstates evidence.

## Shared acceptance template

For every implemented component verify:

1. semantic element and accessible name;
2. keyboard and focus behavior;
3. all relevant states;
4. responsive and long-copy behavior;
5. reduced-motion behavior;
6. server or async failure behavior;
7. analytics semantics if the interaction represents a product outcome;
8. visual consistency with tokens and neighboring components.
