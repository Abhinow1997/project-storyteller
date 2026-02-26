import requests
import base64
import json
from pathlib import Path
from datetime import datetime

output_dir = Path("./output/diagrams")
output_dir.mkdir(parents=True, exist_ok=True)

diagrams = {
    "architecture": """
graph TD
    subgraph Routes["SvelteKit Routes"]
        Root["+page.svelte<br/>Home Dashboard"]
        Overview["+page.svelte<br/>Overview/Briefing"]
        MissionIndex["missions/+page.svelte<br/>Mission Index"]
        Games["7 Game Pages<br/>/missions/[type]/game"]
    end
    
    subgraph Stores["State Management"]
        GameStore["gameState.js<br/>missionProgress"]
        QuizStore["quizState"]
    end
    
    subgraph Components["Interactive Components"]
        Drag["Drag & Drop Logic"]
        Feedback["Feedback System"]
        Animations["Svelte Animations"]
    end
    
    subgraph Styling["Presentation Layer"]
        Tailwind["Tailwind CSS<br/>4.1.18"]
        Svelte5["Svelte 5 Reactivity<br/>$state, $derived"]
    end
    
    Root -->|navigate| MissionIndex
    MissionIndex -->|launch| Games
    Games -->|update| GameStore
    GameStore -->|read| Feedback
    Games -->|drag operations| Drag
    Drag -->|reorder| Animations
    Feedback -->|visual| Tailwind
    Svelte5 -->|drives all| Components
""",
    "dataflow": """
graph LR
    User["👤 Player"] -->|clicks Start| Brief["Mission Briefing"]
    Brief -->|accepts challenge| GameStart["Game State Init"]
    GameStart -->|shuffle operations| Board["Available Operations"]
    
    Board -->|drag| Sequence["Drop Zone"]
    Sequence -->|organize| Complete{Full Sequence?}
    
    Complete -->|no| Board
    Complete -->|yes| Verify["Verify Order"]
    
    Verify -->|check against| Correct["Correct Sequence"]
    Correct -->|compare| Validate{Match?}
    
    Validate -->|correct| Success["Game Complete"]
    Validate -->|wrong| Feedback["Show Feedback<br/>+ Hint"]
    Feedback -->|try again| Board
    
    Success -->|save to| Store["Game Store<br/>Track Progress"]
    Store -->|increment| Attempts["Best Score<br/>+ Attempts"]
""",
    "sequence": """
sequenceDiagram
    actor User
    participant Game as Game Screen
    participant State as Svelte State
    participant Store as Game Store
    
    User->>Game: Click "Accept Mission"
    Game->>State: gameStarted = true
    Game->>State: shuffledItems = randomize()
    
    Note over Game: Mission briefing shown
    User->>Game: Drag "Signal Acquisition"
    Game->>State: Remove from shuffled
    Game->>State: Add to dropZone
    
    User->>Game: Complete sequence (5 items)
    User->>Game: Click "Verify Sequence"
    Game->>State: checkOrder() function
    State->>State: feedbackResults = validate
    State->>State: showFeedback = true
    
    alt Correct Order
        State->>State: gameComplete = true
        State->>Store: completeMission() called
        Store->>User: Show success screen
    else Wrong Order
        Game->>User: Show which items wrong
        User->>Game: Continue dragging
    end
"""
}

def render_diagram(name: str, mermaid_syntax: str) -> Path:
    """Render Mermaid diagram to PNG via mermaid.ink API."""
    
    graph_str = mermaid_syntax.strip()
    encoded = base64.urlsafe_b64encode(graph_str.encode('utf-8')).decode('utf-8')
    url = f"https://mermaid.ink/img/{encoded}"
    
    print(f"  Rendering {name}...")
    try:
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            output_path = output_dir / f"{name}.png"
            output_path.write_bytes(response.content)
            size_kb = len(response.content) / 1024
            print(f"  OK: {name}.png saved ({size_kb:.1f} KB)")
            return output_path
        else:
            print(f"  ERROR: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"  ERROR: {e}")
        return None

def main():
    print("Generating diagram PNGs via Mermaid.ink...\n")
    
    results = {}
    for name, syntax in diagrams.items():
        path = render_diagram(name, syntax)
        results[name] = str(path) if path else None
    
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps({
        "diagrams": results,
        "project": "Mission Control - Prompt Chaining Academy",
        "generated": datetime.now().isoformat()
    }, indent=2))
    
    print(f"\nDiagrams saved to: {output_dir}")
    for name in ["architecture", "dataflow", "sequence"]:
        path = output_dir / f"{name}.png"
        if path.exists():
            print(f"  {name}.png ({path.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    main()
