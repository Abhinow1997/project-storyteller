import requests
import base64
import json
from pathlib import Path

output_dir = Path("./output/diagrams")
output_dir.mkdir(parents=True, exist_ok=True)

diagrams = {
    "architecture": """
graph TD
    Browser["🌐 Browser/Client"]

    subgraph Routes["SvelteKit Routes Layer"]
        Dashboard["+page.svelte<br/>Dashboard"]
        Missions["missions/+page.svelte<br/>Mission Catalog"]
        Briefing["briefing/+page.svelte<br/>Audio Briefing"]
        Games["missions/*/game/+page.svelte<br/>Interactive Games"]
        Cert["certifications/+page.svelte<br/>Quiz"]
    end

    subgraph Components["Svelte Components"]
        MissionCard["Mission Card<br/>Display"]
        GameBoard["Drag-Drop Board<br/>Game Logic"]
        AudioPlayer["Custom Audio<br/>Player"]
        QuizUI["Quiz Questions<br/>UI"]
    end

    subgraph State["State Management<br/>Svelte Stores"]
        MissionProgress["missionProgress<br/>Store"]
        QuizState["quizState<br/>Store"]
    end

    subgraph Styling["Design System<br/>app.css + Tailwind v4"]
        Theme["Color Theme<br/>terminal-green/blue/amber/purple"]
        Animations["Keyframes<br/>glow, float, twinkle"]
        Components["Panel, Button<br/>Status Indicators"]
    end

    Layout["Layout: +layout.svelte<br/>Nav, Status Bar, Footer"]

    Browser --> Layout
    Layout --> Routes
    Routes --> Components
    Components --> State
    Components --> Styling
    State --> State

    style Browser fill:#2c3e50,stroke:#00d4ff,color:#fff
    style Routes fill:#1a252f,stroke:#00ff88,color:#fff
    style Components fill:#1a252f,stroke:#00ff88,color:#fff
    style State fill:#16202a,stroke:#a855f7,color:#fff
    style Styling fill:#16202a,stroke:#ffb800,color:#fff
    """,

    "dataflow": """
graph LR
    User["👤 User Input<br/>Click/Drag"]
    Event["Event Handler<br/>onDragStart/<br/>onClick"]
    Logic["Game Logic<br/>Drag-Drop<br/>Order Check"]
    Store["State Update<br/>missionProgress<br/>store.update"]
    Derived["Derived State<br/>$derived<br/>feedback, score"]
    Render["Re-render<br/>Components<br/>UI Updates"]
    Visual["Visual Feedback<br/>Colors, Icons<br/>Animations"]

    User -->|trigger| Event
    Event -->|process| Logic
    Logic -->|commit| Store
    Store -->|reactive| Derived
    Derived -->|compute| Render
    Render -->|display| Visual
    Visual -->|user sees| User

    style User fill:#0d1117,stroke:#00ff88,color:#fff,stroke-width:2px
    style Event fill:#161b22,stroke:#00d4ff,color:#fff
    style Logic fill:#21262d,stroke:#a855f7,color:#fff
    style Store fill:#21262d,stroke:#a855f7,color:#fff
    style Derived fill:#161b22,stroke:#00d4ff,color:#fff
    style Render fill:#161b22,stroke:#00d4ff,color:#fff
    style Visual fill:#0d1117,stroke:#00ff88,color:#fff,stroke-width:2px
    """,

    "sequence": """
sequenceDiagram
    participant User as User
    participant Game as Game Component
    participant Handlers as Drag/Drop Handlers
    participant Store as missionProgress Store
    participant UI as UI Reactive State

    User->>Game: Click "Start Game"
    activate Game
    Game->>Game: shuffledItems = shuffle(correctOrder)
    Game->>Game: dropZone = []
    Game->>UI: Component Re-renders
    deactivate Game

    User->>Game: Drag item from shuffled
    activate Game
    Game->>Handlers: handleDragStart(item)
    Handlers->>Handlers: draggedItem = {item, source}
    deactivate Game

    User->>Game: Drop into zone
    activate Game
    Game->>Handlers: handleDropToZone(e)
    Handlers->>Game: Remove from shuffled
    Handlers->>Game: Add to dropZone
    Game->>UI: UI re-renders with new zones
    deactivate Game

    User->>Game: Click "Check Order"
    activate Game
    Game->>Game: feedbackResults = validate(dropZone)
    Game->>Game: Check if order === correctOrder
    alt Correct
        Game->>Game: gameComplete = true
        Game->>Store: completeMission(id, attempts)
        Store->>Store: Update completion status
    else Incorrect
        Game->>Game: Show feedback with X marks
        Game->>UI: Shake animation trigger
    end
    Game->>UI: Display feedback
    deactivate Game
    """
}

def render_diagram(name: str, mermaid_syntax: str) -> Path:
    """Render Mermaid diagram to PNG via mermaid.ink API."""

    graph_str = mermaid_syntax.strip()
    encoded = base64.urlsafe_b64encode(graph_str.encode('utf-8')).decode('utf-8')
    url = f"https://mermaid.ink/img/{encoded}?bgColor=white&width=1200"

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
            print(f"  FAILED to render {name}: HTTP {response.status_code}")
            print(f"  Response: {response.text[:200]}")
            return None
    except Exception as e:
        print(f"  ERROR rendering {name}: {str(e)}")
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
        "project": "Mission Control (promptchaining-sveltekit)",
        "generated": "2026-02-24"
    }, indent=2))

    print(f"\nDiagrams saved to: {output_dir}")
    print(f"  - architecture.png")
    print(f"  - dataflow.png")
    print(f"  - sequence.png")
    print(f"  - manifest.json")

if __name__ == "__main__":
    main()
