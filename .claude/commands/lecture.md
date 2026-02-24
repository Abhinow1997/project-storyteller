Using the full project analysis from this session, create a structured lecture document to ./output/lecture.md

If /analyze has not been run yet, say:
"Please run /analyze first so I have the project context loaded."

## Process

### Step 1: Load Skills
First apply the curriculum-designer skill to sequence concepts from simple to complex.
Then apply the analogy-builder skill to map technical components to real-world equivalents.
Then apply the diagram-builder skill to prepare an architecture diagram for the lecture.

### Step 2: Build the Lecture

Structure the output exactly like this:

---

# [Project Name]: A Technical Lecture

## Course Information
**Subject:** [inferred from project domain]
**Level:** [Beginner / Intermediate / Advanced — based on complexity]
**Estimated Time:** [realistic reading/study time]
**Prerequisites:** [what you should already know]

---

## Learning Objectives
By the end of this lecture, you will be able to:
1. [concrete skill or understanding]
2. [concrete skill or understanding]
3. [concrete skill or understanding]
4. [concrete skill or understanding]

---

## Part 1: The Problem Space
[Explain the problem this project solves as if the student has never heard of it.
Use the analogy-builder output here — ground it in real-world terms first.
No code yet. Pure conceptual understanding.]

---

## Part 2: The Architecture
[High-level system overview. Insert the Mermaid architecture diagram here.
Explain each component using the analogy-builder mappings.
Walk through how the components connect.]
```mermaid
[architecture diagram from diagram-builder skill]
```

[Paragraph explaining what the diagram shows]

---

## Part 3: Core Concepts
[Work through the Foundation and Core tiers from curriculum-designer.
One subsection per concept. Each subsection:
- Concept name as heading
- Plain English explanation
- Real-world analogy
- How it appears in THIS codebase specifically
- A relevant code snippet (pulled from actual files)]

---

## Part 4: How It All Comes Together
[Walk through one complete end-to-end flow — from user action to final output.
Use a sequence diagram here from diagram-builder skill.
Make it concrete: "when a user does X, here is exactly what happens"]
```mermaid
[sequence diagram from diagram-builder skill]
```

---

## Part 5: Advanced Topics
[Cover the Advanced tier from curriculum-designer.
Design decisions, tradeoffs, and non-obvious implementation choices.
This is where technically curious students go deeper.]

---

## Part 6: What Could Be Better
[Honest assessment of limitations and gaps.
Frame as learning opportunities — "if you were to extend this project..."]

---

## Knowledge Check
10 questions that test genuine understanding (not memorization):

**Conceptual Questions (no code needed):**
1. [question]
2. [question]
3. [question]
4. [question]
5. [question]

**Technical Questions (requires understanding the codebase):**
6. [question]
7. [question]
8. [question]
9. [question]
10. [question]

---

## Further Reading
[5-7 resources relevant to the technologies and concepts in this project.
Include: official docs, key papers if relevant, tutorials, related projects.
Each with a one-sentence description of what it adds.]

---

## Summary
[3-4 sentence recap. What did we cover, why does it matter, what should the student do next.]

---

## Requirements
- Complete document, no truncation
- Every code snippet must come from actual files in the repo
- Diagrams must use valid Mermaid syntax
- Knowledge check questions must be answerable from the lecture content
- Further reading resources must be real and relevant

After writing, confirm file path and estimated reading time to user.


## PDF Generation

### Step 1: Resolve pandoc path
```bash
if command -v pandoc &> /dev/null; then
    PANDOC_CMD="pandoc"
elif [ -f "/c/Users/ab/AppData/Local/Pandoc/pandoc.exe" ]; then
    PANDOC_CMD="/c/Users/ab/AppData/Local/Pandoc/pandoc.exe"
else
    echo "❌ Pandoc not found. Run /setup first."
    exit 1
fi
echo "Using pandoc: $PANDOC_CMD"
```

### Step 2: Resolve LaTeX engine
```bash
if command -v xelatex &> /dev/null; then
    ENGINE="xelatex"
elif command -v pdflatex &> /dev/null; then
    ENGINE="pdflatex"
else
    echo "❌ No LaTeX engine found. Run /setup first."
    exit 1
fi
echo "Using engine: $ENGINE"
```

### Step 3: Generate PDF
```bash
$PANDOC_CMD ./output/lecture.md \
  -o ./output/lecture.pdf \
  --pdf-engine=$ENGINE \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V linestretch=1.4 \
  -V colorlinks=true \
  -V linkcolor=blue \
  --highlight-style=tango \
  --toc \
  --toc-depth=2
```

### Step 4: Verify output
```bash
ls -lh ./output/lecture.pdf && echo "✅ PDF generated successfully"
```