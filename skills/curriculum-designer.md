# Skill: Curriculum Designer

When called, take a project understanding and sequence its concepts from simple to complex for teaching purposes.

## Process

### Step 1: Concept Inventory
List every meaningful concept present in the codebase:
- Core abstractions (what are the main "things" in this system?)
- Key processes (what are the main "actions" this system takes?)
- Design patterns used
- External dependencies and why they were chosen

### Step 2: Dependency Mapping
For each concept, identify:
- What must be understood BEFORE this concept makes sense
- What this concept unlocks understanding of

### Step 3: Sequence
Order concepts into 4 tiers:
- **Foundation** — concepts with no prerequisites (start here)
- **Core** — concepts that require Foundation
- **Advanced** — concepts that require Core
- **Expert** — concepts that require Advanced (optional for most learners)

### Output Format
Return a structured curriculum map:

**Foundation Concepts:**
- [concept]: [one sentence explanation]

**Core Concepts:**
- [concept]: [one sentence explanation] | Requires: [foundation concept]

**Advanced Concepts:**
- [concept]: [one sentence explanation] | Requires: [core concept]

**Expert Concepts (optional):**
- [concept]: [one sentence explanation]

## Rules
- Every concept must have a clear one-sentence explanation
- No concept should appear in two tiers
- Sequence should feel natural — each concept should make the next one obvious