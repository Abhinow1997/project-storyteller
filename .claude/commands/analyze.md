The user will provide a repository path. Read and deeply analyze it.

## Step 1: Explore Structure
List the full directory tree. Identify:
- Entry points (main files, index files, app files)
- Config files (package.json, pyproject.toml, etc.)
- Core logic directories
- Test files
- Documentation files

## Step 2: Read Files
Read files in priority order:
1. Config/setup files first (understand dependencies and project intent)
2. Entry points (understand flow)
3. Core logic (understand implementation)
4. Tests if present (understand intended behavior)
5. Any existing README (understand how author describes it)

Skip binary files, lock files, dependency directories.

## Step 3: Build Analysis
Present your findings in this exact format:

---
## 📊 Project Analysis

**Project Name:** ...
**One Liner:** ...

**The Problem:**
(2-3 sentences. Be specific about pain, not generic.)

**How It Works:**
(3-4 sentences. Technical but human. Architecture + approach.)

**Key Components:**
- ComponentName: what it does and why it matters
- (list all significant components)

**Tech Stack:** ...

**The Interesting Part:**
(The one thing about this project that is surprising, clever, or underappreciated. This is the hook everything else builds from.)

**Biggest Design Decision:**
(The most consequential architectural or implementation choice made.)

**What's Missing / Could Be Better:**
(Honest gaps — missing tests, undocumented code, scalability concerns, etc.)

**Target Audience:** ...

**Tone Keywords:** (exactly 5 adjectives)

**The Deeper Story:**
(What does this project represent beyond its immediate function? What problem in the world does it push back against?)
---

## Step 4: Confirm
After presenting analysis, ask:
"Ready to generate content. Which would you like?
- /generate-readme
- /generate-article  
- /generate-linkedin
- /tweet
- /critique
- /ask (to ask questions about the project)
- /all (run all generators)"