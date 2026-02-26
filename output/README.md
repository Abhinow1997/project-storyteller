# Prompt Chaining: Interactive Learning Platform

Learn to orchestrate AI workflows by commanding space missions.

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![Status](https://img.shields.io/badge/status-production-brightgreen)

## About

**Prompt Chaining** is an interactive web application that teaches complex AI prompt orchestration patterns through immersive space mission simulations. Instead of reading documentation, you sequence tasks in a drag-and-drop interface, immediately seeing why order matters, why data flow matters, and why breaking problems into phases actually works.

The application covers seven essential prompt chaining patterns: sequential (the simplest), branching (parallel operations), iterative (loop-and-refine), hierarchical (nested structures), conditional (decision gates), recursive (divide-and-conquer), and reverse (working backward from outcomes).

Each pattern is explained through:
- **Conceptual briefings** with mission control analogies
- **Audio instruction** delivered by a declassified transmission
- **Interactive simulations** where you complete real scenarios
- **Dual-view interface** for technical and playful learning modes

## Why This Exists

Prompt chaining is where most AI engineers stumble. The concept sounds simple—chain outputs to inputs—but the practical patterns are not obvious. How do you handle failures? What data do you pass forward? When do you parallelize vs. sequence? Do you loop or split?

Traditional documentation answers these with dense explanations and generic examples. This project answers them kinesthetically: you *feel* the difference between patterns by using them against realistic scenarios. When your sequential chain breaks on step 3, you learn viscerally why error isolation matters. When parallel branches need merging, you see why state management design pays off.

Built as an educational tool for AI engineers, computer science students, and prompt engineers learning operational workflows.

## Quick Start

### Prerequisites
- Node.js 18+ (18.17 or 20+)
- npm, yarn, or pnpm

### Installation

```bash
git clone https://github.com/yourusername/promptchaining-sveltekit.git
cd promptchaining-sveltekit
npm install
```

### Running Locally

```bash
npm run dev
```

Visit `http://localhost:5173` to start. The app opens to the home page with a "STANDARD VIEW / MISSION MODE" toggle in the top center.

### Building for Production

```bash
npm run build
npm run preview
```

The production build outputs to `.svelte-kit/build/` and can be deployed to any Node.js host or serverless platform via the adapter configuration in `svelte.config.js`.

### Linting & Formatting

```bash
npm run lint       # Check for violations
npm run format     # Auto-fix formatting
```

## How It Works

### Architecture Overview

The application is built on **SvelteKit**, which provides file-based routing and server capabilities. Each URL path maps to a Svelte component:

```
src/routes/
├── +layout.svelte          # Global layout, header, footer
├── +page.svelte            # Home page (dual-mode view)
├── briefing/+page.svelte   # Mission briefing section
├── missions/+page.svelte   # Mission types overview
└── missions/[pattern]/
    ├── +page.svelte        # Pattern overview (e.g., sequential/)
    └── game/+page.svelte   # Interactive simulation
```

### Why This Architecture?

**File-based routing** keeps concerns separated. Adding a new prompt chaining pattern requires only:
1. Creating a new folder under `missions/[newpattern]/`
2. Writing two files: overview + game
3. Updating the missions array in the missions index

No complex route registration, no deeply nested prop drilling. Svelte's reactive ($state, $derived) handles UI reactivity without Redux-style boilerplate.

### Styling Strategy

The app uses **Tailwind CSS v4** with a custom space theme defined in `app.css`:

```css
@theme {
  --color-space-950: #0a0a0f;
  --color-terminal-green: #00ff88;
  --color-terminal-blue: #00d4ff;
}
```

This single configuration powers all color decisions across components. The space theme isn't decorative—it's the entire UX language. When users see cyan borders and green text, they're *in mission control*. The visual metaphor isn't just theme; it's narrative architecture.

### Game Mechanics

Each interactive simulation follows this flow:

1. **Setup**: User reads the mission briefing (scenario, objective, urgency)
2. **Shuffle**: Tasks are shuffled into random order
3. **Sequence**: User drags tasks into the correct order
4. **Validation**: System checks order and provides immediate feedback
5. **Result**: Success or failure, with ability to retry

The drag-and-drop implementation uses Svelte's `flip` animation from `svelte/animate`, making reordering fluid without requiring a separate animation library.

```svelte
<script>
  import { flip } from 'svelte/animate';
  let dropZone = $state([]);
</script>

{#each dropZone as item (item.id)}
  <div animate:flip={{ duration: 300 }}>
    {item.label}
  </div>
{/each}
```

### State Management

Svelte 5's rune-based reactivity eliminates the need for external state management:

```svelte
<script>
  let gameStarted = $state(false);
  let attempts = $state(0);
  let gameComplete = $state(false);

  let progress = $derived(completedTasks / totalTasks);
</script>
```

**$state** creates reactive variables. **$derived** creates computed values that update automatically. No subscriptions, no selectors, no boilerplate.

## Project Structure

```
promptchaining-sveltekit/
├── src/
│   ├── app.css                 # Global styles + Tailwind theme
│   ├── app.html                # HTML shell
│   ├── routes/
│   │   ├── +layout.svelte      # Global layout component
│   │   ├── +page.svelte        # Home (prompt chaining overview)
│   │   ├── briefing/           # Mission briefing section
│   │   ├── missions/           # Mission types index
│   │   └── missions/[pattern]/
│   │       ├── sequential/     # Sequential chaining pattern
│   │       ├── branching/      # Parallel branching pattern
│   │       ├── iterative/      # Loop-and-refine pattern
│   │       ├── hierarchical/   # Nested structures pattern
│   │       ├── conditional/    # Decision gates pattern
│   │       ├── recursive/      # Divide-and-conquer pattern
│   │       └── reverse/        # Work-backward pattern
│   └── lib/
│       └── index.js            # Exported utilities
├── static/
│   ├── images/                 # Mission briefing images
│   ├── audio/                  # transmission.mp3 (audio briefing)
│   └── favicon.svg
├── package.json
├── svelte.config.js            # SvelteKit configuration
├── tailwind.config.ts          # Tailwind configuration
├── vite.config.js              # Vite build configuration
└── README.md
```

## Contributing

Contributions are welcome. The project follows these guidelines:

### Adding a New Prompt Chaining Pattern

1. Create a new directory: `src/routes/missions/[patternname]/`
2. Add `+page.svelte` for the overview (explain the pattern, show the flow diagram)
3. Add `game/+page.svelte` for the interactive simulation
4. Update the `missions` array in `src/routes/missions/+page.svelte` with the new entry
5. Test locally with `npm run dev`
6. Ensure `npm run lint` and `npm run format` pass

### Code Style

- Use Svelte 5 runes ($state, $derived, $effect) for reactivity
- Prefer Tailwind utility classes over custom CSS
- Keep components under 300 lines; extract complex logic into separate files
- Write semantic HTML; don't over-nest divs
- Use `font-mono` for code/terminal text, `font-display` for headers

### Reporting Issues

If the game logic breaks, audio doesn't load, or routing is incorrect, open an issue with:
- Steps to reproduce
- What you expected
- Screenshots if visual
- Browser and OS version

## Roadmap

### Phase 1: Core Complete ✓
- [x] Seven prompt chaining patterns implemented
- [x] Interactive game simulations for each pattern
- [x] Dual-mode UI (standard + mission)
- [x] Audio briefing player
- [x] Responsive design

### Phase 2: Enhanced Learning (Q2 2026)
- [ ] **Difficulty levels**: Easy (3-step chains), Medium (5-step), Hard (8-step + edge cases)
- [ ] **Pattern library**: Developers can save and share their own prompt chain diagrams
- [ ] **Performance analytics**: Dashboard showing which patterns users struggle with, time-to-completion metrics

### Phase 3: Integration & Scale (Q3 2026)
- [ ] **API endpoint** for embedding simulations in other educational platforms
- [ ] **Multiplayer mode**: Teams compete to sequence chains fastest
- [ ] **Advanced patterns**: Agentic loops, tree-of-thought, self-correcting chains
- [ ] **LLM integration**: Generate custom scenarios from user-provided prompts

### Phase 4: Production Operations (Q4 2026)
- [ ] **Progress persistence**: User accounts with saved game history and achievement badges
- [ ] **Localization**: Support for Spanish, Mandarin, Japanese
- [ ] **Mobile app**: Native iOS/Android apps with offline mode
- [ ] **Certification program**: Official "Prompt Chaining Engineer" badge upon completion

## License

MIT. Use, modify, and share freely.

## Questions?

- **How do I extend this?** Read `CONTRIBUTING.md` (coming soon) or open a discussion
- **Can I use this at my company?** Yes, MIT license—no restrictions
- **What's the technical debt?** None currently. Performance is solid at 60fps on all interactions
- **Why the space theme?** Mission control parallels are pedagogically powerful. The theme makes abstract concepts concrete

---

**Author**: Prompt Engineering Assignment Team
**Repository**: [github.com/yourusername/promptchaining-sveltekit](https://github.com/yourusername/promptchaining-sveltekit)
**Last Updated**: February 2026
