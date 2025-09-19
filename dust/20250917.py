import math
import sys
import random
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

# Prime check - Cryptographic stardust for secure cosmic networks
def prime_check(num):
    steps = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        steps += 1
        if num % i == 0:
            return False, steps, sys.getsizeof(num)
    return True, steps, sys.getsizeof(num)

# Fibonacci (iterative) - Spirals of nature, twinkling in cosmic code
def fibonacci_iter(n):
    a, b = 0, 1
    steps = 0
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
        steps += 1
    return seq, steps, sys.getsizeof(seq)

# Historical countdown - A joyful jaunt through coding’s starry timeline
def historical_countdown(days=5):
    steps = 0
    milestones = [
        "📜 Ancient Algorithms (825 CE): Logic’s first giggle!",
        "🖋️ Poetic Programs (1843): Code that sings!",
        "🤖 Universal Machine (1936): Silicon dreams born!",
        "🦋 Bug Hunt (1957): Squashing cosmic critters!",
        "🌐 Web Weaving (1989): Spinning digital galaxies!"
    ]
    for day in range(1, days + 1):
        console.print(f"🎉 Day {day}: {milestones[day-1]}", style="bold magenta")
        steps += 1
    return None, steps, sys.getsizeof(milestones)

# Hash map - Lightning-fast data for interstellar treasure hunts
def hash_map_example(elements=10):
    hm = {}
    steps = 0
    for i in range(elements):
        hm[i] = i * i
        steps += 1
    lookup = hm.get(elements // 2)
    steps += 1
    return lookup, steps, sys.getsizeof(hm)

# Quantum Bit Simulation - Playful quantum flips in a cosmic dance
def qubit_simulation(num_qubits=3):
    steps = 0
    states = []
    for _ in range(2 ** num_qubits):
        state = random.choice([0, 1])
        states.append(state)
        steps += 1
    return states, steps, sys.getsizeof(states)

# Rocket Trajectory - Zooming to stars with playful physics
def rocket_trajectory(initial_velocity=100, gravity=3.71, time_steps=10):
    steps = 0
    positions = []
    velocity = initial_velocity
    position = 0
    dt = 0.1
    for _ in range(time_steps):
        position += velocity * dt
        positions.append(position)
        velocity -= gravity * dt
        steps += 1
    return positions[-1], steps, sys.getsizeof(positions)

# AI Decision Tree - Cosmic game of space tag with fun choices
def ai_decision(obstacles=5):
    steps = 0
    decisions = []
    for _ in range(obstacles):
        decision = "Zoom!" if random.random() > 0.5 else "Duck!"
        decisions.append(decision)
        steps += 1
    return decisions, steps, sys.getsizeof(decisions)

# Binary Search - Hunting treasures in sorted starry arrays
def binary_search(arr, target):
    steps = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return True, steps, sys.getsizeof(arr)
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False, steps, sys.getsizeof(arr)

# Recursive Fibonacci - Exponential adventures in recursive space
def recursive_fib(n):
    steps = [0]
    def fib(k):
        steps[0] += 1
        if k <= 1:
            return k
        return fib(k-1) + fib(k-2)
    res = fib(n)
    return res, steps[0], sys.getsizeof(res)

# Cosmic galaxy animation with color cycling
def galaxy_animation():
    colors = ["bright_cyan", "bright_magenta", "bright_yellow", "bright_green"]
    frames = [
        "   ✨   \n  🌌🌌  \n ✨✨✨ \n  🌌🌌  \n   ✨   ",
        "  🌌🌌  \n ✨✨✨ \n   ✨   \n  🌌🌌  \n ✨✨✨ ",
        " ✨✨✨ \n  🌌🌌  \n   ✨   \n ✨✨✨ \n  🌌🌌  ",
        "  🌌🌌  \n   ✨   \n ✨✨✨ \n  🌌🌌  \n   ✨   "
    ]
    for i, frame in enumerate(frames * 2):  # Loop twice for effect
        console.print(Panel(frame, border_style=colors[i % len(colors)], title="🌠 Cosmic Spin"), style=colors[i % len(colors)])
        time.sleep(0.3)
        console.clear()

# Welcome animation
def welcome_animation():
    stars = ["✨", "🌟", "💫"]
    for i in range(3):
        console.print(f"{' '.join(random.choice(stars) for _ in range(20))}", style="bold cyan")
        time.sleep(0.2)
    console.print(Panel("🌌 FWPK: Code the Cosmos with a Smile! 🚀", border_style="bright_green", style="bold green"))
    console.print(Text("'Code is the universe’s playground—jump in and play!' 😄", style="italic yellow"))
    time.sleep(0.5)

# Table printer with vibrant, animated cosmic style
def complexity_analysis():
    table = Table(title="📊 FWPK Cosmic Complexity Party 🎉", show_lines=True, border_style="bold blue", header_style="bold yellow")
    
    table.add_column("Method", justify="left", style="cyan bold")
    table.add_column("Steps", style="green bold")
    table.add_column("Memory (Bytes)", style="yellow bold")
    table.add_column("Time Complexity", style="magenta bold")
    table.add_column("Space Complexity", style="blue bold")
    table.add_column("Cosmic Fun Fact", style="white italic")
    table.add_column("Cosmic Score", style="bright_red bold")
    table.add_column("Puzzle Hint", style="bright_cyan italic")

    rows = [
        ("🔍 Prime Check", lambda: prime_check(42), "O(√n)", "O(1)", "Primes: The VIPs of number parties! 🎈", "bright_green", "Code a prime sieve!"),
        ("🧬 Fibonacci", lambda: fibonacci_iter(8), "O(n)", "O(n)", "Spirals in stars & code—cosmic winks! 🌟", "bright_yellow", "Plot a spiral!"),
        ("⏳ Galactic Countdown", lambda: historical_countdown(5), "O(n)", "O(1)", "Time travel via code—zoom through history! ⏰", "bright_magenta", "Add a new milestone!"),
        ("📦 Star Map", lambda: hash_map_example(10), "O(1) avg", "O(n)", "Fast lookups for interstellar treasure hunts! 🗺️", "cyan", "Cache a star map!"),
        ("⚛️ Qubit Party", lambda: qubit_simulation(3), "O(2^n)", "O(2^n)", "Quantum flips—code’s wildest dance! 💃", "bright_blue", "Simulate entanglement!"),
        ("🚀 Starship Path", lambda: rocket_trajectory(100, 3.71, 10), "O(n)", "O(n)", "Zoom to Mars with a physics giggle! 🌌", "bright_cyan", "Animate an orbit!"),
        ("🤖 Cosmic Choices", lambda: ai_decision(5), "O(n)", "O(n)", "AI plays tag with asteroids—fun decisions! 🎮", "bright_red", "Add a new choice!"),
        ("🔎 Binary Search", lambda: binary_search(list(range(100)), 42), "O(log n)", "O(n)", "Hunt treasures in sorted stars! 🔭", "bright_green", "Find a cosmic key!"),
        ("🌀 Recursive Fib", lambda: recursive_fib(10), "O(2^n)", "O(n)", "Exponential fun in recursive realms! 🐇", "bright_magenta", "Memoize it!")
    ]

    for method, func, time_c, space_c, fact, style, puzzle in rows:
        result = func()
        steps = result[1]
        mem = result[2]
        # Cosmic Score: Normalized to reward efficiency (log scale for steps to handle recursive_fib)
        score = max(0, 100 - (math.log10(max(steps, 1)) * 20 + mem * 0.005))
        table.add_row(method, str(steps), str(mem), time_c, space_c, fact, f"{score:.1f}⭐", puzzle, style=style)
        console.print(table)
        time.sleep(0.4)  # Progressive row display for animation

    console.print(Panel(table, title="🌌 FWPK Cosmic Code Bash", subtitle="Where Logic Meets Laughter", border_style="bright_cyan", expand=False))

# Main with playful cosmic vibes
if __name__ == "__main__":
    welcome_animation()
    complexity_analysis()
    console.print(Text("\n🌠 Spinning up a cosmic surprise...", style="bold purple"))
    galaxy_animation()
    console.print(Text("\n🔮 Party’s over, but the fun’s just started! What cosmic code will you spin next? 🌟", style="bold purple"))