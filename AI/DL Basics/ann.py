import numpy as np
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(a):
    return a * (1 - a)

# Training data (XOR)
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])
y = np.array([[0],[1],[1],[0]])

# Parameters
np.random.seed(42)
input_size = 2
hidden_size = 2
output_size = 1
learning_rate = 0.5

# Weights and Biases initialization
W1 = np.random.rand(input_size, hidden_size)
b1 = np.random.rand(1, hidden_size)
W2 = np.random.rand(hidden_size, output_size)
b2 = np.random.rand(1, output_size)

console.rule("[bold magenta] Training a Simple ANN on XOR Problem (Infinite Loop) [/bold magenta]")

epoch = 0
try:
    while True:  # Infinite training loop
        # Forward pass
        z1 = np.dot(X, W1) + b1
        a1 = sigmoid(z1)
        z2 = np.dot(a1, W2) + b2
        a2 = sigmoid(z2)

        # Loss (Mean Squared Error)
        loss = np.mean((y - a2) ** 2)

        # Backward pass
        d_a2 = (a2 - y) * sigmoid_derivative(a2)
        d_W2 = np.dot(a1.T, d_a2)
        d_b2 = np.sum(d_a2, axis=0, keepdims=True)

        d_a1 = np.dot(d_a2, W2.T) * sigmoid_derivative(a1)
        d_W1 = np.dot(X.T, d_a1)
        d_b1 = np.sum(d_a1, axis=0, keepdims=True)

        # Update weights and biases
        W1 -= learning_rate * d_W1
        b1 -= learning_rate * d_b1
        W2 -= learning_rate * d_W2
        b2 -= learning_rate * d_b2

        # Print progress every 1000 steps
        if epoch % 1000 == 0:
            console.print(f"[bold cyan]Epoch {epoch}[/bold cyan] | Loss: [bold yellow]{loss:.6f}[/bold yellow]")
            time.sleep(0.05)

        epoch += 1

except KeyboardInterrupt:
    # Stop training gracefully when you press Ctrl+C
    console.rule("[bold red] Training stopped by user [/bold red]")

    # Final Predictions
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    # Build results table
    table = Table(title="XOR ANN Predictions", box=box.ROUNDED, style="bright_blue")
    table.add_column("Input", justify="center", style="cyan", no_wrap=True)
    table.add_column("Prediction", justify="center", style="green")
    table.add_column("Confidence", justify="center", style="white")
    table.add_column("True Label", justify="center", style="yellow")

    for i in range(len(X)):
        table.add_row(str(X[i]),
                      str(int(np.round(a2[i][0]))),
                      f"{a2[i][0]:.4f}",
                      str(y[i][0]))

    console.print(Panel.fit(table, title="[bold green] Final Results [/bold green]", border_style="bright_magenta"))
