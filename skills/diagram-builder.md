# Skill: Diagram Builder

When called, generate valid Mermaid syntax diagrams from project analysis.

## Diagram Types You Can Generate

### Architecture Diagram (flowchart)
Shows components and how data flows between them.
Use when: explaining system structure
```
flowchart TD
    A[Component] --> B[Component]
    B --> C{Decision Point}
    C -->|condition| D[Outcome]
    C -->|condition| E[Outcome]
```

### Sequence Diagram
Shows the order of operations for a specific process.
Use when: explaining how a request flows through the system
```
sequenceDiagram
    participant User
    participant System
    User->>System: action
    System-->>User: response
```

### Component Diagram (flowchart with subgraphs)
Shows how modules are grouped and connected.
Use when: explaining codebase organization
```
flowchart TD
    subgraph LayerName
        A[Component]
        B[Component]
    end
    A --> C[External]
```

## Rules
- Only use components that actually exist in the codebase
- Label every arrow with what is being passed (data, events, calls)
- Keep diagrams readable — max 12 nodes per diagram
- Use subgraphs to group related components
- Always validate that Mermaid syntax is correct before outputting
- Prefer flowchart TD (top-down) for architecture, LR (left-right) for pipelines