from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "docs" / "second-brain-chief-of-staff" / "knowledge-base"


FILES: dict[str, str] = {
    "SB__OperatingSystem__IdentityAndMission.md": dedent(
        """\
        ---
        Title: Identity and Mission
        Type: operating_system
        Domain: personal_strategy
        Date: 2026-04-21
        Keywords:
          - identity
          - mission
          - bioengineering
          - software systems
          - faith
          - training
        Summary: Operating doctrine for aligning academics, product execution, physical training, and spiritual discipline under one coherent identity instead of treating them as separate lives.
        ---

        ## Context
        This system exists to support a bioengineering student who is building a serious portfolio across biomedical engineering, software systems, AI agents, embedded devices, and data products while also maintaining demanding physical and spiritual commitments.

        The main failure mode is fragmentation: acting like a different person in class, in code, in the gym, in church, and in long-term planning. The purpose of this file is to anchor one operating identity that can survive stress, deadlines, and ambition without collapsing into scattered effort.

        ## Key Ideas
        - The central identity is builder-scholar-athlete-disciple, not just student or coder.
        - Work should be evaluated by whether it compounds into competence, credibility, usefulness, and character.
        - Academic work is not separate from project work; classes, labs, and personal systems should feed each other whenever possible.
        - Physical training is not extracurricular. Strength, conditioning, recovery, and discipline directly affect cognition, energy, and execution quality.
        - Spiritual commitments are not background decoration. They shape what tradeoffs are acceptable, what pace is sustainable, and what success means.
        - The system should reward deep work, consistency, and evidence over novelty, busyness, and mood.

        ## Decisions
        - Default priority order is: obligations with real deadlines, flagship academic progress, flagship build projects, health and recovery, then optional exploration.
        - Maintain at most three serious active fronts at one time: one academic push, one build or research push, and one maintenance or operations push.
        - Treat GPA, technical depth, and portfolio quality as joint objectives rather than trading one away casually.
        - Prefer durable artifacts over ephemeral effort: notes, code, writeups, reusable prompts, data schemas, and validated experiments.
        - Any commitment that repeatedly produces guilt without measurable progress should be either redesigned, reduced, or cut.
        - Weekly planning should assume finite energy, not ideal motivation.

        ## Constraints
        - Bioengineering coursework can generate clustered deadlines, labs, and exam weeks that create temporary overload.
        - Training for powerlifting and BJJ adds recovery and scheduling constraints that cannot be ignored without performance decline.
        - Church commitments, family obligations, and health maintenance place non-negotiable limits on available time.
        - Ambition across too many domains can create hidden context-switching costs even when every project is valuable.
        - Long-term goals require consistent documentation and retrieval; memory alone is not reliable enough.

        ## Open Questions
        - Which projects are truly flagship and which are interesting but non-essential?
        - What is the strongest near-term positioning: research-heavy, product-heavy, or hybrid?
        - Which commitments are currently being carried for identity reasons rather than actual value?
        - What does a sustainable training and study cadence look like during exam-heavy weeks?

        ## Next Actions
        - Review this file at the start of each month and after any major schedule change.
        - Add one short paragraph after each weekly review describing whether behavior matched stated identity.
        - Use this file as a tie-breaker whenever planning feels crowded or incoherent.
        - Update flagship goals only when there is a real strategic reason, not because of short-term frustration.
        """
    ),
    "SB__OperatingSystem__RulesOfEngagement.md": dedent(
        """\
        ---
        Title: Rules of Engagement
        Type: operating_system
        Domain: execution_protocol
        Date: 2026-04-21
        Keywords:
          - decision rules
          - planning
          - workload control
          - chief of staff
          - execution
        Summary: Decision rules that govern how the Second Brain should interpret requests, rank work, challenge weak thinking, and convert vague goals into executable plans.
        ---

        ## Context
        This file defines how the Second Brain should behave so it does not drift into generic productivity coaching, overlong summaries, or agreeable nonsense. The standard is disciplined operational usefulness.

        ## Key Ideas
        - Always prefer clarity over comfort.
        - Use uploaded notes as primary evidence before reaching for the web.
        - Separate facts, interpretations, constraints, and inferences every time the distinction matters.
        - Plans should expose bottlenecks, dependencies, and opportunity cost rather than dumping tasks.
        - If priorities conflict, say so directly instead of pretending everything fits.
        - Weak retrieval should be disclosed explicitly; never fake context coverage.

        ## Decisions
        - Default response structure is: Situation, What matters most, Evidence or retrieved context, Recommendation, Next actions, Risks or blind spots.
        - When planning, produce no more than three top priorities unless the user explicitly asks for a longer stack.
        - When reading uploaded files, cite the file name and section header whenever available.
        - When ambiguity is not blocking, proceed with the best defensible interpretation instead of stalling.
        - Challenge overcommitment whenever requested output exceeds realistic time, energy, or deadline capacity.
        - Recommend handoff when the task becomes deeply course-specific problem solving or code implementation outside the assistant's mandate.

        ## Constraints
        - Uploaded material may be partial, outdated, inconsistent, or emotionally biased.
        - Journal entries and self-reflection can mix facts with distorted interpretations.
        - Current external information may matter for research tasks, but web context should not drown out the user's own files.
        - The system should remain strict without becoming performatively harsh or unhelpful.

        ## Open Questions
        - What level of aggressiveness is most useful when calling out drift or rationalization?
        - Which recurring prompt patterns deserve reusable macros or templates?
        - What kinds of handoffs happen often enough to formalize further?

        ## Next Actions
        - Use this file to tune instruction patches when the GPT becomes too soft, too generic, or too summary-heavy.
        - Review failed conversations and map each failure to a violated rule.
        - Add one new rule only when a real repeated failure pattern appears.
        - Keep this file short enough to stay operational, not aspirational.
        """
    ),
    "SB__OperatingSystem__LongTermGoals.md": dedent(
        """\
        ---
        Title: Long-Term Goals
        Type: operating_system
        Domain: strategy
        Date: 2026-04-21
        Keywords:
          - long-term goals
          - career strategy
          - research
          - product building
          - health
        Summary: Multi-year target state for academic excellence, technical depth, portfolio credibility, health, spiritual discipline, and research leverage.
        ---

        ## Context
        The goal is not to stay busy across many interests. The goal is to build a defensible trajectory: strong academic performance, serious technical execution, credible biomedical or health-tech work, durable systems thinking, and a life structure that can scale without self-destruction.

        ## Key Ideas
        - A strong graduation profile should include both grades and real shipped systems.
        - Research value rises when technical depth, experimental rigor, and domain understanding reinforce each other.
        - Product work should demonstrate judgment, not just coding volume.
        - Health, strength, and recovery are infrastructure, not optional extras.
        - Long-term credibility comes from coherent themes: health systems, biomedical engineering, AI tooling, data systems, and disciplined execution.

        ## Decisions
        - Target outcomes over the next three to five years:
          - Graduate with a transcript and project portfolio that both signal seriousness.
          - Build at least two flagship systems with clear architectural depth and user value.
          - Develop one strong research direction that could support graduate study, startup work, or applied R&D.
          - Maintain a high-functioning body through powerlifting, BJJ, sleep, and injury management.
          - Preserve spiritual discipline and avoid achievement patterns that hollow out the rest of life.
        - Prefer fewer flagship systems with evidence of polish over many half-built experiments.
        - Use JonnyJr, Second Brain, and one health or bioengineering system as the primary narrative spine unless a better strategic cluster emerges.
        - Treat internships, research positions, or collaborators as force multipliers only if they fit the long-term story.

        ## Constraints
        - Academic calendars create cyclical compression that can choke long-term work if not planned around.
        - Financial, career, and time pressure can incentivize chasing short-term wins at the expense of coherent positioning.
        - Too many simultaneous domains can blur the professional narrative even if each piece is individually strong.
        - Physical overtraining or under-recovery can quietly degrade cognition and discipline.

        ## Open Questions
        - Should graduate study, startup building, or applied industry work be the default post-graduation direction?
        - Which flagship system has the highest upside for portfolio signaling over the next twelve months?
        - What research problem is both intellectually serious and strategically aligned with product interests?
        - What work should be intentionally ignored to protect compounding focus?

        ## Next Actions
        - Revisit this file at semester boundaries and after major opportunities appear.
        - Add measurable one-year targets beneath each multi-year goal.
        - Cross-check every new project idea against this file before committing serious time.
        - Identify one goal each quarter that deserves concentrated acceleration.
        """
    ),
    "SB__Academics__CurrentSemesterOverview.md": dedent(
        """\
        ---
        Title: Current Semester Overview
        Type: academics
        Domain: semester_planning
        Date: 2026-04-21
        Keywords:
          - semester
          - courses
          - schedule
          - deadlines
          - study system
        Summary: Operating overview for the current semester, including assumed course load, recurring obligations, risk points, and planning rules for staying ahead instead of reacting late.
        ---

        ## Context
        This file assumes a demanding semester for a bioengineering student with CS and Chemistry depth, plus active project work and athletic training. Replace course names only if actual enrollment differs.

        Assumed course stack for planning defaults:
        - Bioinstrumentation
        - Transport Phenomena
        - Organic Chemistry II
        - Algorithms and Data Structures
        - Engineering Design or Biomechanics Lab

        Recurring non-course obligations:
        - Powerlifting sessions
        - BJJ sessions
        - Church attendance and spiritual commitments
        - Project maintenance for JonnyJr, Second Brain, and one active product system

        ## Key Ideas
        - The semester should be run as a control problem: reduce surprise, smooth workload, and protect deep-work windows before deadline compression arrives.
        - Labs, exams, and problem sets should be mapped at least two weeks ahead whenever possible.
        - Course success depends on continuous note consolidation, not just attendance and last-minute review.
        - Technical projects should complement the semester, not cannibalize it.

        ## Decisions
        - Protect fixed study blocks for the two most conceptually heavy courses each week.
        - Create weekly review checkpoints for every course with one question: what can still become a crisis in the next ten days?
        - Treat lab writeups and coding assignments as early-start work because they expand unpredictably.
        - Use office hours, professor questions, and peer clarification early rather than after confusion compounds.
        - During exam weeks, reduce project ambition instead of pretending both workloads can stay at full intensity.

        ## Constraints
        - Lab reports, exams, and project checkpoints often cluster rather than arriving evenly.
        - Training and recovery take real time and cannot be optimized away.
        - Some courses require cumulative understanding, so missed weeks are expensive.
        - Sleep debt rapidly lowers performance in both quantitative coursework and programming.

        ## Open Questions
        - Which course is currently the grade-risk bottleneck?
        - Which course has the strongest connection to active project or research work?
        - Are current notes organized well enough to support fast review before exams?
        - What needs to be dropped temporarily during the heaviest academic weeks?

        ## Next Actions
        - Replace the assumed course list with the real schedule if needed.
        - Add professor office hours, lab meeting times, and exam windows once confirmed.
        - Review this file every Monday before building the weekly plan.
        - Link major assignments to the deadline registry file so work does not live in two places.
        """
    ),
    "SB__Academics__DeadlinesAndDeliverables.md": dedent(
        """\
        ---
        Title: Deadlines and Deliverables
        Type: academics
        Domain: deadline_tracking
        Date: 2026-04-21
        Keywords:
          - deadlines
          - assignments
          - exams
          - deliverables
          - schedule risk
        Summary: Live registry for deadlines, study milestones, and deliverables across coursework, research, and non-academic obligations so the week can be prioritized by actual risk.
        ---

        ## Context
        This file is the central deadline ledger. The goal is to make upcoming obligations visible early enough to sequence work rationally instead of relying on memory or stress signals.

        ## Key Ideas
        - Hard deadlines outrank vague intentions.
        - A deadline without a preparation milestone is already late in planning terms.
        - Exams require study deadlines, not just exam dates.
        - Administrative commitments and training events still count if they constrain time.

        ## Decisions
        - Track deadlines in one list using this format: date, obligation, effort level, dependency, consequence of delay.
        - Maintain a rolling two-week view at minimum.
        - For every exam, include the date by which the study guide, practice problems, and weak-topic review must begin.
        - For every writing or coding assignment, include a first-draft date before the final due date.
        - Current default entries to refine with real dates:
          - [Enter date] Bioinstrumentation lab report due; high effort; depends on clean data and plots; late submission damages grade quickly.
          - [Enter date] Transport Phenomena problem set due; medium effort; depends on lecture understanding; late work creates compounding backlog.
          - [Enter date] Organic Chemistry II exam; high effort; depends on reaction mechanism review; weak preparation raises study debt for later units.
          - [Enter date] Algorithms assignment or quiz; medium-high effort; depends on implementation and proof review; delay blocks confidence before exam.
          - [Enter date] Design or biomechanics lab checkpoint; medium effort; depends on team coordination and documentation.
          - [Enter date] Weekly church or family obligation with travel or preparation; medium constraint; affects deep-work availability.
          - [Enter date] Training event, sparring round, meet prep, or recovery-sensitive session; medium constraint; affects fatigue budget.

        ## Constraints
        - Exact due dates may change across syllabi, announcements, and professor updates.
        - Group work introduces dependency risk outside direct control.
        - Back-to-back exams can create hidden workload overlap if preparation is not front-loaded.
        - Non-academic obligations can consume prime evening or weekend planning time.

        ## Open Questions
        - Which deadlines are fixed versus likely to move?
        - Which assignment has the highest downside if started late?
        - Which deliverables can be combined with project work or note consolidation?
        - What should be deferred immediately if the next ten days become overloaded?

        ## Next Actions
        - Replace bracketed dates with actual calendar dates from syllabi and announcements.
        - Review this file during every weekly review and every time a new deadline appears.
        - Mark one item each week as the primary schedule-risk item.
        - Remove completed items only after the weekly review captures lessons learned.
        """
    ),
    "SB__Projects__MasterProjectIndex.md": dedent(
        """\
        ---
        Title: Master Project Index
        Type: projects
        Domain: portfolio_management
        Date: 2026-04-21
        Keywords:
          - projects
          - portfolio
          - roadmap
          - prioritization
          - systems
        Summary: Portfolio-level map of active and dormant projects with their purpose, current status, leverage, and why each one exists.
        ---

        ## Context
        This file keeps project work from becoming a blur of partially remembered ideas. It should answer four questions quickly: what exists, why it matters, what state it is in, and whether it deserves time right now.

        ## Key Ideas
        - Every project should justify itself by learning leverage, portfolio signal, user value, research value, or operational leverage.
        - Projects should reinforce a coherent narrative around health systems, AI tooling, automation, and engineering rigor.
        - Dormant does not mean dead; it means not funded with current attention.
        - If a project cannot state a next milestone, it is probably not truly active.

        ## Decisions
        - Default portfolio map:
          - JonnyJr: personal AI helper and workflow orchestrator; high leverage; active.
          - Second Brain Chief of Staff: planning and retrieval system for notes, priorities, and knowledge synthesis; high leverage; active.
          - 5amClub: personal operating system and structured workspace; high leverage; active or near-active.
          - GastroGuard: digestive-health tracking and analytics platform; high domain value; selective active.
          - SkinTrack+: skin-condition tracking and provider-shareable symptom management; medium-high domain value; selective active.
          - MindMap: mental-health journaling and tracking platform with strong privacy constraints; medium-high value; dormant unless focused.
          - HealthHelper: general health assistant and support tooling; exploratory unless scoped tightly.
          - Arduino or robotic arm prototypes: embedded systems and mechatronics credibility; active only when tied to course or research goals.
        - Allow only two or three projects to receive serious weekly build time.
        - Use status labels: active, maintenance, parked, archive-candidate.
        - Require each active project to define one current milestone and one blocking risk.

        ## Constraints
        - Academic demands cap available build bandwidth.
        - Health and privacy-sensitive products require more careful thinking than generic app ideas.
        - Context switching between hardware, AI systems, data pipelines, and UI work is expensive.
        - Some projects overlap enough that separate maintenance becomes redundant.

        ## Open Questions
        - Which project is the best flagship for internships, research opportunities, or investor-facing credibility?
        - Which product deserves real user interviews or validation next?
        - Which dormant projects are strategically useful versus identity clutter?
        - Where can shared infrastructure reduce duplicated effort?

        ## Next Actions
        - Review this index monthly and after any new project idea appears.
        - Add one-sentence milestone statements for each active project.
        - Mark any project untouched for two months as parked unless there is a clear reason otherwise.
        - Use this file during project audits and weekly planning to prevent priority drift.
        """
    ),
    "SB__Projects__CurrentFocusAndBlockers.md": dedent(
        """\
        ---
        Title: Current Focus and Blockers
        Type: projects
        Domain: execution_tracking
        Date: 2026-04-21
        Keywords:
          - blockers
          - current focus
          - execution
          - priorities
          - project management
        Summary: Short-horizon project operating view that identifies what is active now, what is blocked, and what should not be worked on until key constraints are removed.
        ---

        ## Context
        This file is for current execution, not portfolio identity. It should make it obvious what deserves near-term attention and what is stuck for a real reason.

        ## Key Ideas
        - Blockers should be named concretely: missing schema, unclear scope, missing data, weak prompt contract, unresolved UX, hardware uncertainty.
        - If a blocker persists for multiple weeks, the system should either escalate it or cut the project from active focus.
        - A focus list without explicit non-focus is not a real priority list.

        ## Decisions
        - Default near-term active focus:
          - JonnyJr: tighten orchestration, role boundaries, prompt contracts, and durable workflows.
          - Second Brain: stabilize GPT instructions, knowledge-base quality, and repeatable operating prompts.
          - One academic or research-facing technical build that supports the semester directly.
        - Current likely blockers:
          - JonnyJr: tool sprawl, ambiguous role boundaries, and missing consistent operating protocols across assistants.
          - Second Brain: good prompt quality exists, but reliability depends on disciplined knowledge uploads and consistent review habits.
          - 5amClub or related planning systems: risk of becoming broad architecture work without direct weekly payoff.
          - Health products: privacy, schema, evidence, and product-scope risk if pushed without tighter user and data definitions.
        - Default non-focus for now:
          - Any new project idea without a strategic reason.
          - Cosmetic refactors that do not improve outcome quality.
          - Projects that require substantial setup before clarifying value.

        ## Constraints
        - Available attention changes with academic compression.
        - Some blockers are informational, not technical, and require decisions rather than more work.
        - Momentum can be lost if active projects do not produce visible artifacts weekly.
        - Hardware or health-tech work may require validation steps not available on short timelines.

        ## Open Questions
        - Which blocker is the true bottleneck across all projects right now?
        - What can be shipped or validated in the next seven days?
        - Which project is being kept active out of guilt rather than strategic value?
        - What would make one project obviously ready for a heavier push?

        ## Next Actions
        - Review this file at the start of each week and after any project reset.
        - Attach one concrete next milestone and one unblock action to every active project.
        - Remove anything from active focus that has no believable seven-day action.
        - Use this file during weekly reviews to decide what should be paused.
        """
    ),
    "SB__Research__CurrentResearchQuestions.md": dedent(
        """\
        ---
        Title: Current Research Questions
        Type: research
        Domain: question_mapping
        Date: 2026-04-21
        Keywords:
          - research
          - questions
          - biomedical engineering
          - health systems
          - AI
        Summary: Working map of research questions that connect biomedical engineering, data systems, sensing, and AI-enabled decision support so reading and project work can accumulate toward a stronger research direction.
        ---

        ## Context
        This file holds questions worth sustained attention. The goal is not to hoard topics but to identify a small set of questions that can shape reading choices, project selection, and possible research positioning.

        ## Key Ideas
        - Good research questions connect mechanism, measurement, and practical consequence.
        - The strongest questions usually sit at the intersection of domain need and systems capability.
        - Reading should sharpen questions, not just expand trivia.
        - Questions should be specific enough to guide paper selection and project experiments.

        ## Decisions
        - Current default research questions:
          - How can low-cost sensing systems be designed to maximize data quality without making user workflows fragile?
          - What makes health-tracking systems clinically defensible versus merely informative or aesthetically convincing?
          - How should retrieval, memory, and workflow agents be structured so they remain reliable over long personal knowledge horizons?
          - Which signal-processing or instrumentation problems in bioengineering are tractable with student-level hardware and serious validation discipline?
          - How can personal health or behavior data be modeled to support insight without drifting into overclaiming or pseudo-diagnostics?
          - What design patterns best preserve privacy and user trust in longitudinal health-data systems?
        - Use these questions to choose papers, project milestones, and note-taking categories.
        - Prefer primary literature, official documentation, and methods-heavy sources over commentary when possible.

        ## Constraints
        - Research bandwidth is limited by coursework and build commitments.
        - Some questions are too broad and must be narrowed before they can drive useful reading.
        - Experimental work may require equipment, data access, or validation setups that are not immediately available.
        - AI-related claims are especially easy to overstate without strong evidence.

        ## Open Questions
        - Which one question has the highest payoff if explored seriously this semester?
        - Which question can produce both a literature synthesis and a practical prototype?
        - What measurements or evaluation criteria would make a project result meaningful instead of superficial?
        - Which question best fits potential faculty collaboration or independent study work?

        ## Next Actions
        - Pick one primary question and one secondary question for the next four weeks.
        - Link papers, notes, and experiments back to one of these questions instead of filing them loosely.
        - Rewrite any question that cannot produce a concrete reading or experiment plan.
        - Review this file after every major reading sprint or research memo.
        """
    ),
    "SB__WeeklyReview__Template.md": dedent(
        """\
        ---
        Title: Weekly Review Template
        Type: weekly_review
        Domain: reflection_and_planning
        Date: 2026-04-21
        Keywords:
          - weekly review
          - template
          - planning
          - reflection
          - execution
        Summary: Weekly review protocol for extracting lessons, resetting priorities, identifying drift, and building the next week from evidence instead of mood.
        ---

        ## Context
        This template is the weekly reset. It should turn the last seven days into better judgment, not a guilt ritual or a vague recap.

        ## Key Ideas
        - Review outcomes, not intentions.
        - Distinguish wins, misses, and drift.
        - Convert reflection into one or two operational changes.
        - Use the review to cut work, not only to add work.

        ## Decisions
        - Run the weekly review once per week, ideally before planning the next week.
        - Use this template:

        ```text
        WEEKLY REVIEW

        1. What were the three most important things that actually happened this week?
        2. What meaningful progress was made in academics, projects, training, and spiritual life?
        3. Where did I drift, procrastinate, overcommit, or rationalize?
        4. What deadlines, risks, or bottlenecks matter most in the next 10 days?
        5. What should I deliberately defer, reduce, or ignore next week?
        6. What is the single biggest bottleneck right now?
        7. What are the top three priorities for next week?
        8. What supporting actions or appointments must be scheduled for those priorities to happen?
        9. What lesson from this week should become a rule or adjustment?
        10. Did my behavior match my stated identity and long-term goals? Where not?
        ```

        ## Constraints
        - Reviews become useless if they are too long to sustain.
        - Memory is biased toward recent stress and emotion, so the review should use real notes, deadlines, and outputs.
        - If the review does not affect the next week, it is performative.

        ## Open Questions
        - Which review prompts produce the best behavioral corrections?
        - Should project and academics be reviewed together or as separate blocks during high-pressure weeks?
        - What recurring misses deserve their own checklist or system fix?

        ## Next Actions
        - Run this review every Sunday or at the natural week boundary.
        - Save short weekly outputs so trends can be recognized over time.
        - Add one sentence each week about what needs to be cut, not just what needs to be improved.
        - If the same issue appears for three consecutive weeks, escalate it into a real system change.
        """
    ),
    "SB__DailyPlanning__IdealPromptInputs.md": dedent(
        """\
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
        """
    ),
}


def write_files(output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    for filename, content in FILES.items():
        destination = output_dir / filename
        destination.write_text(content, encoding="utf-8")
        written.append(destination)

    return written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate the foundational markdown files for the Second Brain Chief of Staff knowledge base."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to receive the generated markdown files. Defaults to {DEFAULT_OUTPUT_DIR}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        written_files = write_files(args.output_dir)
    except OSError as exc:
        print(f"Failed to generate knowledge-base files: {exc}")
        return 1

    print("Generated Second Brain knowledge-base files:")
    for path in written_files:
        print(f"- {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
