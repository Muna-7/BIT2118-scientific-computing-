import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

# Log-spaced sample indices for a clean semilog plot
idx = np.unique(np.logspace(0, np.log10(N), 300).astype(int)) - 1
idx = idx[idx >= 0]

plt.semilogx(idx + 1, running_probability[idx])
plt.axhline(overload_probability, color="red", linestyle="--",
            label=f"Final = {overload_probability:.4f}")
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.legend(); plt.grid(True)
plt.savefig("outputs/task_20_monte_carlo.png", dpi=150)
plt.show()