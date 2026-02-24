Check if the required tools for Project Storyteller are installed.

## Important: Windows Path Detection
On Windows, tools may exist but not be in the bash PATH.
Always check both the command directly AND known Windows locations.

## Step 1: Detect OS and Shell
```bash
echo "OS: $(uname -s)"
echo "Shell: $SHELL"
echo "PATH: $PATH"
```

## Step 2: Check Python
```bash
python --version 2>&1 || python3 --version 2>&1 || echo "MISSING: python"
```

## Step 3: Check Pandoc
Check command first, then fallback to known Windows locations:
```bash
if command -v pandoc &> /dev/null; then
    echo "✅ pandoc found: $(pandoc --version | head -1)"
elif [ -f "/c/Users/ab/AppData/Local/Pandoc/pandoc.exe" ]; then
    echo "✅ pandoc found at Windows path but NOT in bash PATH"
    echo "NEEDS: bash wrapper setup"
    PANDOC_PATH="/c/Users/ab/AppData/Local/Pandoc/pandoc.exe"
else
    echo "❌ pandoc not found anywhere"
fi
```

## Step 4: Check LaTeX
```bash
if command -v xelatex &> /dev/null; then
    echo "✅ xelatex: $(xelatex --version 2>&1 | head -1)"
elif command -v pdflatex &> /dev/null; then
    echo "✅ pdflatex: $(pdflatex --version 2>&1 | head -1)"
else
    echo "❌ No LaTeX engine found"
fi
```

## Step 5: If pandoc found at Windows path but not in bash PATH
Create a bash wrapper automatically:
```bash
WRAPPER_PATH="/c/Users/ab/miniconda3/Scripts/pandoc"
cat > "$WRAPPER_PATH" << 'EOF'
#!/bin/bash
"/c/Users/ab/AppData/Local/Pandoc/pandoc.exe" "$@"
EOF
chmod +x "$WRAPPER_PATH"
echo "✅ Bash wrapper created at $WRAPPER_PATH"
```

Then verify:
```bash
pandoc --version | head -1
```

## Step 6: Summary
Print a clean status table:
```
Tool         Status    Version
-----------  --------  -------
Python       ✅/❌     x.x.x
Pandoc       ✅/❌     x.x.x
LaTeX        ✅/❌     x.x.x
```

If everything is ✅ say:
"All tools ready. Run /analyze followed by /lecture to generate a PDF lecture."

If anything is ❌ provide the specific install command for the missing tool.