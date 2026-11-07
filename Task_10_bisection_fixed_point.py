import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)

solution = root_scalar(heat_balance, bracket=[20, 40],
                       method="bisect", xtol=1e-10)

def g(T):
    return 25 + 10 * np.exp(-T / 20)

T = 30.0
history = [T]
for _ in range(100):
    T_new = g(T)
    history.append(T_new)
    if abs(T_new - T) < 1e-10:
        break
    T = T_new

print(f"Bisection equilibrium temperature: {solution.root:.6f} C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

temps = np.linspace(20, 40, 300)
plt.plot(temps, heat_balance(temps))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Temperature (C)"); plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature"); plt.grid(True)
plt.savefig("outputs/task_10_equilibrium.png", dpi=150)
plt.show()