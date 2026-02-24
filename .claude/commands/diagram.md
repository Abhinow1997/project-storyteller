Using the full project analysis from this session, generate system diagrams as actual PNG files.

If /analyze has not been run yet, say:
"Please run /analyze first so I have the project context loaded."

## Process

### Step 1: Apply diagram-builder skill
Generate three diagrams:
1. Architecture diagram — flowchart TD with subgraphs
2. Data flow diagram — flowchart LR
3. Sequence diagram — key user interaction

### Step 2: Verify Python dependencies
```bash
python -c "import requests, base64; print('✅ Dependencies ready')"
```
If requests missing:
```bash
pip install requests
```

### Step 3: Write the PNG generator script
Write this Python script to ./output/generate_diagrams.py,
substituting the actual Mermaid syntax you generated in Step 1:
```python
import requests
import base64
import json
from pathlib import Path

output_dir = Path("./output/diagrams")
output_dir.mkdir(parents=True, exist_ok=True)

diagrams = {
    "architecture": """
[PASTE ARCHITECTURE MERMAID SYNTAX HERE]
""",
    "dataflow": """
[PASTE DATA FLOW MERMAID SYNTAX HERE]
""",
    "sequence": """
[PASTE SEQUENCE MERMAID SYNTAX HERE]
"""
}

def render_diagram(name: str, mermaid_syntax: str) -> Path:
    """Render Mermaid diagram to PNG via mermaid.ink API."""
    
    # Encode diagram for API
    graph_str = mermaid_syntax.strip()
    encoded = base64.urlsafe_b64encode(graph_str.encode('utf-8')).decode('utf-8')
    url = f"https://mermaid.ink/img/{encoded}?bgColor=white&width=1200"
    
    print(f"  Rendering {name}...")
    response = requests.get(url, timeout=30)
    
    if response.status_code == 200:
        output_path = output_dir / f"{name}.png"
        output_path.write_bytes(response.content)
        size_kb = len(response.content) / 1024
        print(f"  ✅ {name}.png saved ({size_kb:.1f} KB)")
        return output_path
    else:
        print(f"  ❌ Failed to render {name}: HTTP {response.status_code}")
        print(f"  Response: {response.text[:200]}")
        return None

def main():
    print("🎨 Generating diagram PNGs via Mermaid.ink...\n")
    
    results = {}
    for name, syntax in diagrams.items():
        path = render_diagram(name, syntax)
        results[name] = str(path) if path else None
    
    # Save manifest
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps({
        "diagrams": results,
        "project": "[PROJECT NAME]",
        "generated": "[DATE]"
    }, indent=2))
    
    print(f"\n📁 Diagrams saved to: {output_dir}")
    print(f"   architecture.png")
    print(f"   dataflow.png") 
    print(f"   sequence.png")
    print(f"   manifest.json")

if __name__ == "__main__":
    main()
```

### Step 4: Run the script
```bash
python ./output/generate_diagrams.py
```

### Step 5: Verify outputs
```bash
ls -lh ./output/diagrams/
```

### Step 6: Write diagram.md as a companion reference doc
After PNGs are confirmed generated, write ./output/diagram.md with this structure:

---
# [Project Name] — System Diagrams

> PNG diagrams generated in ./output/diagrams/

---

## 1. Architecture Overview
![Architecture](./diagrams/architecture.png)

[2-3 sentence explanation of what this diagram shows]

**Reading this diagram:**
- [most important connection]
- [non-obvious grouping]
- [any decision points]

---

## 2. Data Flow
![Data Flow](./diagrams/dataflow.png)

[2-3 sentence explanation]

**What to notice:**
- [most interesting transformation]
- [bottlenecks or critical paths]

---

## 3. Key Interaction: [interaction name]
![Sequence](./diagrams/sequence.png)

[1-2 sentence setup]

**Step by step:**
1. [plain English explanation of each step]

---

## Component Reference

| Component | Layer | Responsibility |
|-----------|-------|----------------|
| [name] | [layer] | [one sentence] |

---

## Rules
- Only use components that actually exist in the codebase
- Label every arrow in Mermaid syntax
- Max 12 nodes per diagram
- Verify each PNG is non-zero bytes before confirming success
- If mermaid.ink API fails, fall back to saving raw .mmd files and 
  notify user to render manually at https://mermaid.live

After completion confirm:
"✅ Diagrams generated:
- output/diagrams/architecture.png
- output/diagrams/dataflow.png
- output/diagrams/sequence.png
- output/diagram.md (companion reference)"
```

---

Your output folder structure now becomes:
```
output/
├── README.md
├── article.md
├── linkedin.txt
├── tweet_thread.txt
├── critique.md
├── lecture.md
├── lecture.pdf
├── resources.md
├── diagram.md
└── diagrams/
    ├── architecture.png
    ├── dataflow.png
    ├── sequence.png
    └── manifest.json