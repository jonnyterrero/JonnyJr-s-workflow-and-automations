---
Title: Ideal Daily Planning Prompt Inputs
Type: daily_planning
Domain: planning_inputs
Date: 2026-04-21
Keywords:
  - daily planning
  - prompt inputs
  - scheduling
  - priorities
  - execution
Summary: Structured daily input template that gives the Second Brain enough context to produce a realistic plan grounded in deadlines, constraints, and energy instead of generic task advice.
---

## Context
The quality of the daily plan depends heavily on input quality. The goal is to supply enough structure for a useful recommendation without forcing a large journaling ritual every morning.

## Key Ideas
- The assistant needs deadlines, available time, energy level, and known constraints more than it needs a giant raw task dump.
- A useful day plan should reflect real capacity.
- The plan should identify what not to do as clearly as what to do.

## Decisions
- Use this input block whenever possible:

```text
DAILY PLAN INPUTS

Date:
Available deep-work windows:
Hard appointments or class blocks:
Current energy level (low / medium / high):
Top deadlines in the next 10 days:
Current bottleneck:
Tasks or obligations already on my plate:
What I am tempted to work on but probably should not:
Desired outcome for today:
```

- If time is short, minimum viable inputs are: available time, top deadlines, current bottleneck, and desired outcome.
- The assistant should be asked to return: objective, constraints, top priorities, recommended sequence, concrete next actions, and what should be deferred.

## Constraints
- Daily energy and recovery vary more than idealized plans assume.
- Some days are logistics-heavy and cannot support deep technical work.
- Overloaded days require active cutting, not creative optimism.

## Open Questions
- Which input field most improves recommendation quality?
- Do training and recovery constraints need their own dedicated planning field?
- Should the system include a quick estimate of focus quality from the prior night of sleep?

## Next Actions
- Keep this template accessible in notes, phone, or pinned documents.
- Use the same format consistently for at least two weeks before changing it.
- Track whether plans fail from bad prioritization, bad estimates, or lack of follow-through.
- Update the input fields only when a real pattern of missing context appears.
