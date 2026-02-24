Run all generation commands in sequence using the current session's project analysis.

If /analyze has not been run yet, say:
"Please run /analyze first so I have the project context loaded."

Otherwise run in this order:
1. generate-readme → output/README.md
2. generate-article → output/article.md  
3. generate-linkedin → output/linkedin.txt
4. tweet → output/tweet_thread.txt
5. critique → output/critique.md

After each file is written, confirm it before moving to the next.

When all are complete, print a summary:

## ✅ Project Storyteller Complete

Generated 5 artifacts in ./output/:
- README.md — developer documentation
- article.md — narrative nonfiction (~XXXX words)
- linkedin.txt — LinkedIn post (XXX chars)
- tweet_thread.txt — X tweet thread
- critique.md — technical assessment