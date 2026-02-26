# Mission Control — System Diagrams

System architecture and interaction diagrams for the prompt chaining learning platform.

---

## 1. Architecture Overview

![Architecture Diagram](./diagrams/architecture.png)

This diagram shows the layered architecture of Mission Control. The **SvelteKit Routes** layer handles page navigation and mission flows. The **State Management** layer (game store) tracks progress and quiz state across all missions. **Interactive Components** manage drag-and-drop mechanics, feedback systems, and Svelte animations. The **Presentation Layer** combines Svelte 5's reactivity with Tailwind CSS for responsive styling.

**Reading this diagram:**
- Routes directly navigate players between home, overview, and individual mission games
- All game state flows through centralized stores, ensuring progress persists across navigation
- Svelte 5's $state and $derived reactivity drives component updates without manual re-renders
- Tailwind and animations provide visual feedback for every game action (correct/wrong sequences, drag effects)

---

## 2. Data Flow

![Data Flow Diagram](./diagrams/dataflow.png)

This diagram traces a complete game loop from player action to completion. A player starts with the mission briefing, then operations are shuffled into an available pool. They drag operations into a drop zone to assemble the correct sequence. When ready, they submit for verification. The system compares against the expected order and either shows success (saving to the store) or feedback with hints for retry.

**What to notice:**
- **Critical loop**: Wrong answers loop back to the dragging phase, not restart — players refine in place
- **State convergence**: All feedback paths eventually lead to either "Success → Store" or "Feedback → Retry"
- **Bottleneck**: The Verify Order step is the single point of truth — if the sequence doesn't match exactly, the feedback system engages
- **Progress tracking**: Only successful completions update the Game Store, ensuring only validated progress is recorded

---

## 3. Key Interaction: Game Flow Sequence

![Sequence Diagram](./diagrams/sequence.png)

This diagram shows the temporal flow of a single mission game. The user clicks "Accept Mission," which initializes game state and shuffles operations. They then drag operations one at a time into the drop zone. When the sequence is complete (all 5 operations placed), they click "Verify Sequence." The system validates by comparing dropZone against the correct order. If correct, it marks the game complete and stores the result. If wrong, it shows which items are incorrect and allows another attempt.

**Step by step:**
1. Player clicks "Accept Mission" button on briefing screen
2. Game screen initializes: shuffledItems array randomized, dropZone emptied, gameStarted flag set to true
3. Player drags first operation (e.g., "Signal Acquisition") from shuffledItems
4. Svelte state reactively removes it from shuffledItems and adds to dropZone
5. Player repeats for remaining 4 operations, visually building the sequence
6. Player clicks "Verify Sequence" button
7. Game calls checkOrder() function to validate
8. System builds feedbackResults array comparing each dropZone item against correctOrder
9. If all match: gameComplete = true, success screen shown, progress saved to Game Store
10. If any mismatch: showFeedback = true, visual indicators show which items are wrong, hints appear, player can drag items back to retry

---

## Component Reference

| Component | Layer | Responsibility |
|-----------|-------|-----------------|
| `+layout.svelte` | Routes | Mission Control header, navigation bar, page template |
| `missions/+page.svelte` | Routes | Mission index displaying all 7 patterns with descriptions |
| `missions/[type]/game/+page.svelte` | Routes | Individual game screen with drag-drop interface |
| `gameState.js` | Stores | missionProgress & quizState writable stores, completion tracking |
| Drag handlers | Components | handleDragStart, handleDragOver, handleDropToZone, handleDropToShuffled |
| Feedback system | Components | feedbackResults array, visual pulse animations for correct/wrong |
| Svelte animations | Components | flip animations on reordering, shake effect on failed attempts |
| Tailwind CSS | Styling | Grid layouts, responsive spacing, color theming (green/cyan/amber) |
| Svelte 5 runes | Styling | $state for reactive variables, $derived for computed values |

