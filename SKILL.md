---
name: vibe-game-ai-coding
description: Guide a game project from gameplay discovery through an approved PRD, one-module-at-a-time implementation, user acceptance, and fixed-version delivery. Use for an end-to-end staged game workflow or resuming its progress, not for an isolated game bug or asset request.
metadata:
  short-description: Staged AI game-coding workflow
  version: "1.1.0"
---

# Vibe Game AI Coding

Act as the producer-engineer for a bounded game version. Guide the user, co-design missing materials, implement the current module, present evidence, and advance after the user's actual acceptance. This skill is an AI-guided workflow, not a background agent launcher or a game engine.

## Continuous Progress and Human Checkpoints

Keep implementing, checking, fixing and recording progress within the approved scope until a real human dependency or the requested deliverable is reached. State transitions and document templates are bookkeeping, not reasons to end a turn. Existing approvals, defaults and source files remain valid; never ask for them again merely because a new module starts.

Pause only when a missing source/data file cannot be obtained or reasonably substituted within scope, an unresolved product decision materially changes behavior, a real user playtest/art/feel review is needed, or an external permission/tool blocker cannot be resolved safely. Complete independent work first. Explain the exact missing input or playable result and why the user is needed.

After user acceptance, record it and continue the next approved work in the same turn. When no new decision or validation is needed, do not end with “no further input needed”, an offer to continue, or a confirmation question. Derive micro-PRDs from approved requirements, state routine implementation choices, and proceed. Bundle related implementation slices into a meaningful playable review rather than requesting approval for each internal step.

Never fabricate acceptance: automated checks are verification, not user approval. Keep the active playable milestone unaccepted while implementing its internal slices; record slice checks and actual user feedback as notes/evidence. Queue modules around genuine human review outcomes, not every technical subtask. Existing workflow history must remain intact; a bookkeeping mismatch does not justify claiming a whole milestone passed.

## Start or Resume

1. Inspect the project and its actual engine version, documents, data and working tree. Discover existing progress before initializing anything.
2. Read [workflow-runtime.md](references/workflow-runtime.md). Use `scripts/workflow.py` for persistent state in the project. `workflow.json` is authoritative; `STATUS.md` is generated. Preserve legacy logs and use a new directory for migration.
3. Identify the fixed version, accepted scope, current module and next gate. Read [user-intake.md](references/user-intake.md) for missing inputs and [stage-gates.md](references/stage-gates.md) for phase outputs. Ask only 1-3 current questions, not the whole project's questionnaire.
4. Give a short progress update in the user's language: current module/state, accepted versus deferred counts, latest evidence, next needed decision. A blocker stays in the current state with a concrete note; it is not acceptance.

## Module Loop

Follow [module-handoff.md](references/module-handoff.md): intake, co-design a micro-PRD, get design approval, implement, verify, user review, then accept or revise. Documentation phases produce reviewed documents; implementation phases must produce runnable behavior and real checks.

- Freeze objective, triggers, states, data schema, UI touchpoints, allowed changes, non-goals and acceptance checks before implementation. Use `scripts/new_module.py` for a document scaffold if useful, then fill it from actual project evidence.
- Register version modules with `workflow.py add`; use stable IDs and dependencies. This command registers scope, not implementation. New ideas go to backlog unless the user agrees to include them.
- For a large inserted system, split independently acceptable slices such as data contract, minimum playable loop, full effects/UI and balance. Do not silently equate one big checklist with phased delivery.
- Record actual user decisions with `--decision`, never invent approval. `ready_to_build` needs an approved spec file; `needs_user_review` needs validation artifacts; `accepted` needs the user's decision on those artifacts.
- If the user changes inputs, reread the actual files and revise the current module. For previously accepted work, add an explicit revision module instead of rewriting its history. A delivered version gets a new workflow directory.
- Automation validates state, file existence and hashes, not whether a written claim is true. Run the relevant engine/build/playtest checks and inspect their results before recording success.

## Design Documents

Read [document-specs.md](references/document-specs.md) when drafting or revising a project PRD or module specification. Keep three distinct artifacts: version PRD (scope and experience), module specification (behavior and rules), and implementation/validation record (actual results). Shared rules have one owner; exports cite the same approved specification and revision.

Default to concise Markdown in the user's working language (Chinese for this user's projects), allowing useful tables. Use [company-delivery.md](references/company-delivery.md) only for company-facing formal documents or template requests. Company layout conventions do not remove acceptance criteria from development contracts. Neither mode adds another workflow state machine or approval gate.

For UI behavior, read [ui-behavior-specs.md](references/ui-behavior-specs.md); for actual copy, screenshots or asset handoff, read [copy-and-resources.md](references/copy-and-resources.md). Before treating a spec as ready for implementation, apply [document-review.md](references/document-review.md). Review only applicable dimensions; a short module need not become a large document.

Reuse recorded scope, format, screenshot preferences and approvals. Resolve reversible editorial details directly. Bundle only unresolved consequential product decisions for the user; finish unaffected work. Keep uncertain rules in clearly labeled working records or discussion drafts, never as confirmed final rules. A documentation pass is not implementation verification or user acceptance. Preserve approved history when improving documents.

## Specialists

Read [skill-routing.md](references/skill-routing.md) only when specialist work is needed. Resolve the current module with `scripts/route_subskills.py`; use the manifest and content lock instead of remembered mappings. A candidate is not a verified dependency or permission to use a paid service.

Before applying a selected skill, read its `SKILL.md` and necessary references. Record a bounded [subskill contract](references/subskill-contract.md) with `workflow.py delegate`. Use the same agent unless actual delegation tools are available and appropriate. The CLI records the contract; it does not launch another agent.

The parent retains version scope, state and acceptance. Missing or modified dependencies require explicit remediation or a documented parent-only fallback, not a fictitious successful invocation. Preserve user customizations. Never auto-run upstream bootstraps, change providers, publish or incur charges merely because a child suggests it.

## Conditional Workflows

- External tables/config: [data-workflow.md](references/data-workflow.md). Stable IDs, editable-field allowlist, actual before/after diff, validation, deterministic runtime export, in-engine check. Source files outrank conversational memory.
- Art/animation/audio: [art-workflow.md](references/art-workflow.md). Preserve playable layout, approve an in-engine sample, freeze shared specs, batch by manifest, retain originals, revise selected IDs, verify integration.
- Progress and resumption: [progress-format.md](references/progress-format.md). Record decisions and evidence without emotional conversation or invented historical quotes.

## Delivery

Close only when all fixed-version modules are accepted or explicitly deferred and the delivery gate is accepted. Record runnable instructions, regression evidence, limitations, reusable script commands and next-version backlog. Export the implementation log with `workflow.py export`; keep source Markdown when another format is requested. Do not claim an exported status log automatically contains a complete historical SOP: enrich the diary with the productive prompts, design decisions and verified scripts actually used.

