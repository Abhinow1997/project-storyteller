Using the full project analysis from this session, research and curate relevant resources, then save to ./output/resources.md

If /analyze has not been run yet, say:
"Please run /analyze first so I have the project context loaded."

## Process

### Step 1: Extract Search Targets
From the project analysis, identify:
- Primary technologies (frameworks, languages, libraries)
- Core concepts and patterns used
- Interesting challenges mentioned in analysis
- Target audience's likely knowledge gaps

### Step 2: Web Search
Run targeted searches for each technology and concept found.
Search in this order:

**Official Documentation:**
```
web_search("[technology] official documentation")
web_search("[framework] getting started guide")
```

**Relevant Tutorials:**
```
web_search("[technology] [specific pattern used in project] tutorial")
web_search("how to build [what project does] with [tech stack]")
```

**Similar Projects:**
```
web_search("[project type] open source [primary language] github")
web_search("[project domain] example projects [framework]")
```

**Deep Dive Articles:**
```
web_search("[interesting challenge from analysis] best practices")
web_search("[architecture pattern used] explained")
```

**Tools and Extensions:**
```
web_search("tools for [project domain] developers")
web_search("[primary framework] useful libraries [year]")
```

Run at minimum 8 searches. Fetch the actual pages for the top result 
of each search to verify they are real, relevant, and accessible.

### Step 3: Curate and Filter
From all search results, select the 15-20 best resources.
Filter criteria:
- Must be directly relevant to THIS project's stack and challenges
- Prefer official docs, reputable publishers, high quality tutorials
- No outdated content (check dates — prefer last 2 years for fast-moving tech)
- No paywalled content unless it's genuinely the best resource available
- Must be a real, accessible URL (verify with web_fetch)

### Step 4: Organize into Categories
Group resources into these categories (only include categories that have results):

- **Getting Started** — for someone new to this stack
- **Official Documentation** — authoritative references
- **Tutorials & Guides** — hands-on learning
- **Architecture & Patterns** — design decisions relevant to this project
- **Tools & Extensions** — things that complement this project
- **Similar Projects** — open source projects worth studying
- **Deep Dives** — advanced reading for curious learners
- **Community & Support** — forums, Discord, GitHub discussions

### Step 5: Write Output

Format each resource exactly like this:

---
**[Resource Title]**
🔗 [URL]
📌 **Why it matters for this project:** [1-2 sentences specific to THIS project, not generic]
⏱ **Time investment:** [Quick read / 30 min / Multi-hour / Reference]
🎯 **Best for:** [Who should read this and when]

---

## Full Output Structure
```markdown
# Resources for [Project Name]

> Curated based on your project's stack: [tech stack list]
> Generated: [date]

---

## 🚀 Getting Started
[resources]

## 📚 Official Documentation  
[resources]

## 🎓 Tutorials & Guides
[resources]

## 🏗️ Architecture & Patterns
[resources]

## 🛠️ Tools & Extensions
[resources]

## 🔍 Similar Projects
[resources]

## 🧠 Deep Dives
[resources]

## 💬 Community & Support
[resources]

---

## Recommended Learning Path

Based on this project's complexity, here is the suggested order to work through these resources:

**Week 1 — Foundation**
1. [resource name] — why first
2. [resource name] — why second

**Week 2 — Core Concepts**
1. [resource name]
2. [resource name]

**Week 3 — Advanced**
1. [resource name]
2. [resource name]

---

## Quick Reference Card

| Need | Go To |
|------|-------|
| [common need] | [resource name + link] |
| [common need] | [resource name + link] |
| [common need] | [resource name + link] |
```

## Rules
- Every URL must be verified real via web_fetch before including
- Descriptions must be specific to THIS project — never generic
- Minimum 15 resources, maximum 20
- Learning path must be sequenced logically from the curriculum-designer skill
- Quick reference card must cover the 5 most common needs for this project type

After writing, confirm file path and total number of resources curated.