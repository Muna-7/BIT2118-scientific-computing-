 # BIT 2118 Scientific Computing — Individual GitHub Submission

**Student:** [Aden Muna Musa]  
**Reg. No.:** [BSCCS252604761 ]  
**Unit:** BIT 2118 Scientific Computing  

All 19 computational tasks (Tasks 2–20) are implemented in Python using NumPy, SciPy and Matplotlib.
Each task below records: inputs, mathematical operation, output, a changed parameter,
interpretation, graph (where applicable), and a modified real-world case.

---

## Task 2 — NumPy Arrays and Numerical Computation

**Inputs:** 24 hourly temperature readings in °C.
**Operation:** mean, minimum, maximum, and vectorized conversion F = 1.8C + 32.
**Output:** mean = 23.12 °C; min = 17.50 °C; max = 29.40 °C;
first six Fahrenheit values = [65.30, 64.40, 64.04, 63.50, 64.22, 66.20].
**Parameter change:** shifting all readings by +2 °C shifts the mean, min and max
by exactly +2 °C (25.12, 19.50, 31.40 °C) and every Fahrenheit value by +3.6 °F,
because the conversion is linear.
**Interpretation:** The day is mild, averaging 23.12 °C, coolest before dawn
(17.5 °C) and warmest mid-afternoon (29.4 °C). NumPy performs the statistics and
unit conversion without an explicit loop.
**Modified case:** A wind farm records 24 hourly wind speeds in m/s. I would modify the code to compute mean/min/max and a vectorized m/s → km/h conversion (×3.6). The output would show the farm generates for 21 of 24 hours.

---

## Task 3 — Mathematical Functions and Vectorization

**Inputs:** 1,000,000 simulated network latency values (uniform, 5–250 ms).
**Operation:** seconds = ms/1000; squared = seconds², done by a Python loop vs a
vectorized NumPy expression.
**Output:** first five squared latency values are printed; the vectorized version is substantially faster than the loop.
**Parameter change:** reducing the sample to 100,000 readings reduces both times roughly 10× but the vectorized version stays faster.
**Interpretation:** Vectorization replaces an explicit Python loop with one array expression, so it is far faster on large datasets.
**Modified case:** A weather station has one million pressure readings in Pascals. I would modify the code to convert them to kilopascals by dividing by 1000 and compute squared deviations from the mean. This supports anomaly detection.

---

## Task 4 — Floating-Point Arithmetic and Numerical Errors

**Inputs:** 0.1 + 0.2, 0.3, √2, 1.414.
**Operation:** floating-point comparison; absolute error |true − approx| and relative error |true − approx| / |true|.
**Output:** 0.1 + 0.2 = 0.30000000000000004; exact comparison gives False; `np.isclose` gives True; absolute error of √2 = 0.00021356; relative error = 0.0151%.
**Parameter change:** tightening the `np.isclose` tolerance can turn True into False, showing the result depends on the chosen tolerance.
**Interpretation:** Computers store most real numbers approximately, so exact `==` is unsafe for floats; tolerance-based comparisons and numerically stable formulas avoid spurious errors.
**Modified case:** A banking system compares calculated account balances. Instead of exact equality, I would modify the code to use `np.isclose(balance1, balance2, atol=0.01)` to allow rounding to cents.

---

## Task 5 — Matrix Algebra and Matrix Operations

**Inputs:** unit square points (0,0), (1,0), (1,1), (0,1); 45° rotation; scale diag(2, 1.5).
**Operation:** combined transformation T = R·S; each point transformed by p' = T·p; determinant of T.
**Output:** T ≈ [[1.4142, −1.0607], [1.4142, 1.0607]]; determinant = 3. Transformed points ≈ (0,0), (1.4142, 1.4142), (0.3536, 2.4749), (−1.0607, 1.0607).
**Parameter change:** changing the angle to 90° rotates the shape a quarter turn; changing x-scale from 2 to 3 stretches it further horizontally.
**Interpretation:** Matrix multiplication applies one consistent geometric transformation to every point; the determinant is the area-scaling factor.
**Modified case:** A robotics arm moves a 2-D tool path. I would modify the code to use rotation and scaling matrices to transform the path before sending commands to motors.

---

## Task 6 — Solution of Systems of Linear Equations

**Inputs:** A = [[4, 2], [8, 12]], b = [20, 72].
**Operation:** solve Ax = b with `np.linalg.solve`; residual r = b − Ax.
**Output:** Type A servers = 3, Type B servers = 4; A·x = [20, 72]; residual norm = 0.
**Parameter change:** increasing total CPU from 20 to 24 (memory unchanged) changes the solution to more Type A servers.
**Interpretation:** the two equations uniquely determine how many servers of each type produced the observed CPU and memory usage.
**Modified case:** A traffic model has two road types. Given total vehicles and total travel time, I would modify the code to solve for the number of vehicles on each road type.

---

## Task 7 — Gaussian Elimination and LU Decomposition

**Inputs:** A = [[4, −1, 0], [−1, 4, −1], [0, −1, 3]]; three right-hand sides b₁, b₂, b₃.
**Operation:** LU factorization A = LU once, then forward/back substitution for each b.
**Output:** b₁ → x = [5, 5, 5]; b₂ and b₃ give different solutions; residual norms ≈ 0.
**Parameter change:** increasing the diagonal entries makes the system more diagonally dominant, changing the solution and improving numerical stability.
**Interpretation:** LU is efficient when the same matrix A is reused with many different right-hand-side vectors.
**Modified case:** A structural engineering model reuses the same stiffness matrix for many load cases. I would modify the code to factor once and solve many times.

---

## Task 8 — Iterative Methods for Linear Systems

**Inputs:** 5×5 tridiagonal system with b = [100, 0, 0, 0, −20] (boundary influences 100 °C left and −20 °C right).
**Operation:** Jacobi and Gauss–Seidel iteration with tolerance 1e-8, compared with the direct solution.
**Output:** both methods converge to x = [80, 60, 40, 20, 0] °C, matching the direct solution.
**Parameter change:** raising the left boundary to 150 °C and lowering the right to −50 °C raises all interior temperatures.
**Interpretation:** iterative methods solve sparse systems cheaply because they never factorize the full matrix.
**Graph:** `outputs/task_08_convergence.png` — semilog error-vs-iteration plot; both curves fall steeply, with Gauss–Seidel below Jacobi.
**Modified case:** Heat distribution in a metal plate with different boundary temperatures. I would modify the boundary variables in the code to simulate this.

---

## Task 9 — Eigenvalues and Eigenvectors

**Inputs:** adjacency matrix of a 4-node network A–B, A–C, B–C, B–D, C–D.
**Operation:** eigenvalues/eigenvectors with `np.linalg.eig`; take the dominant eigenvector, take absolute values, normalize to sum 1.
**Output:** dominant eigenvalue ≈ 2.5616; normalized centrality: A = 0.219, B = 0.281, C = 0.281, D = 0.219.
**Parameter change:** adding an edge A–D makes the graph more symmetric and equalizes the centrality of all four nodes.
**Interpretation:** B and C are structurally most influential because they connect to more and better-connected nodes.
**Modified case:** A social network identifies influential users from friendship connections. I would modify the adjacency matrix to represent users.

---

## Task 10 — Root Finding: Bisection and Fixed-Point Methods

**Inputs:** heat-balance function f(T) = T − 25 − 10·exp(−T/20), bracket [20, 40].
**Operation:** bisection with xtol = 1e-10; fixed-point iteration until |ΔT| < 1e-10.
**Output:** bisection equilibrium temperature ≈ 27.524 °C; fixed-point result ≈ 27.524 °C.
**Parameter change:** raising the ambient constant from 25 °C to 30 °C raises the equilibrium temperature.
**Interpretation:** the root is the temperature where heat gain equals heat loss.
**Graph:** `outputs/task_10_equilibrium.png` — f(T) crosses zero once in [20, 40]; the vertical dashed line marks the equilibrium temperature.
**Modified case:** Find the break-even production quantity where revenue equals cost. I would modify the function to represent profit.

---

## Task 11 — Root Finding: Newton–Raphson and Secant Methods

**Inputs:** cash flows [−10000, 3000, 3500, 4000, 2500]; Newton start r₀ = 0.10; secant starts 0.05 and 0.20.
**Operation:** solve NPV(r) = 0 using Newton–Raphson and the secant method.
**Output:** IRR ≈ 11.54% by both methods; NPV at the solution ≈ 0.
**Parameter change:** increasing the initial investment to −11000 lowers the IRR.
**Interpretation:** the IRR is the discount rate at which the project breaks even in present-value terms.
**Modified case:** Compute the effective interest rate for a loan with fees and monthly payments. I would modify the cash flow array.

---

## Task 12 — Polynomial and Nonlinear Equation Solving

**Inputs:** circle x² + y² = 4 and parabola y = x² − 1.
**Operation:** solve the two coupled residual equations with `scipy.optimize.root`.
**Output:** intersections ≈ (1.5175, 1.3028) and (−1.5175, 1.3028); residuals ≈ 0.
**Parameter change:** increasing the circle radius from 2 to 3 moves the intersection points outward.
**Interpretation:** the solutions are the coordinates where the curve and parabola cross.
**Modified case:** Find where a circular robot workspace intersects a parabolic path. I would modify the equations.

---

## Task 13 — Interpolation

**Inputs:** hourly temperatures 8:00–14:00 = [18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0] °C.
**Operation:** linear interpolation and cubic spline; evaluate every 10 minutes.
**Output:** linear estimate at 10:30 = 23.25 °C; cubic spline estimate ≈ 23.28 °C.
**Parameter change:** adding an extra measurement changes the spline near that point more strongly than the linear interpolation.
**Interpretation:** interpolation fills in missing values between known measurements; the cubic spline is smoother but can overshoot.
**Graph:** `outputs/task_13_interpolation.png` — hourly points with a piecewise-linear line and a smooth cubic curve through them.
**Modified case:** A sensor records data every hour, but a control system needs values every 10 minutes. I would modify the time array to resample.

---

## Task 14 — Curve Fitting and Approximation

**Inputs:** concurrent users [50, 100, 150, 200, 250, 300, 350]; response time [82, 95, 115, 145, 185, 238, 305] ms.
**Operation:** least-squares fit of a quadratic y = ax² + bx + c with `curve_fit`.
**Output:** fitted coefficients a ≈ 0.002167, b ≈ −0.1345, c ≈ 85; predicted response at 400 users ≈ 378 ms.
**Parameter change:** a linear model fits poorly at high load because response grows faster than linearly.
**Interpretation:** the model quantifies how server response degrades nonlinearly with load.
**Graph:** `outputs/task_14_curve_fit.png` — scatter of measurements with the fitted quadratic rising steeply at high user counts.
**Modified case:** Fit electricity demand against temperature to forecast peak load. I would modify the input arrays.

---

## Task 15 — Numerical Differentiation

**Inputs:** time [0..6] s; position [0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0] m.
**Operation:** forward difference at the start, central difference in the interior, backward difference at the end.
**Output:** speeds = [4.80, 5.10, 5.65, 6.25, 6.95, 7.65, 8.00] m/s.
**Parameter change:** smaller time steps improve accuracy; larger steps smooth out accelerations.
**Interpretation:** the vehicle is accelerating throughout, from 4.8 m/s to 8.0 m/s.
**Graph:** `outputs/task_15_speed.png` — estimated speed increases roughly linearly with time.
**Modified case:** Estimate acceleration from vehicle velocity data. I would modify the input to use velocity arrays.

---

## Task 16 — Numerical Integration

**Inputs:** time [0, 2, 4, 6, 8, 10, 12] h; power [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9] kW.
**Operation:** trapezoidal rule and Simpson's rule.
**Output:** trapezoidal energy = 15.700 kWh; Simpson energy = 15.800 kWh.
**Parameter change:** with higher power readings the energy increases proportionally; with more sample points both estimates converge.
**Interpretation:** total electrical energy used over the day is about 15.7–15.8 kWh.
**Modified case:** Estimate total water flow from flow-rate measurements. I would modify the input variables.

---

## Task 17 — Ordinary Differential Equations — Euler Method

**Inputs:** Newton's cooling dT/dt = −k(T − 25), T(0) = 90 °C, k = 0.12, step h = 1 min, end time 30 min.
**Operation:** Euler update T_{n+1} = T_n + h·f(T_n); compared with the exact exponential solution.
**Output:** Euler temperature after 30 min = 26.41 °C; exact = 26.78 °C.
**Parameter change:** halving h to 0.5 min reduces the final error but doubles the number of steps.
**Interpretation:** the object cools toward room temperature; Euler underestimates the temperature slightly.
**Graph:** `outputs/task_17_cooling.png` — Euler points sit just below the exact exponential cooling curve.
**Modified case:** Predict medicine concentration decay in the body over time. I would modify the ODE function.

---

## Task 18 — Numerical Solution of ODEs Using SciPy

**Inputs:** RC charging dV/dt = (Vs − V)/(RC), Vs = 5 V, R = 1000 Ω, C = 0.001 F, V₀ = 0.
**Operation:** `solve_ivp` with rtol = 1e-9, atol = 1e-11, compared with the exact analytic solution.
**Output:** solver success = True; capacitor voltage at 5 s = 4.9663 V; maximum error vs exact ≈ 1e-9 V.
**Parameter change:** increasing R or C increases the time constant RC, so the capacitor charges more slowly.
**Interpretation:** the capacitor charges quickly and approaches the 5 V supply.
**Graph:** `outputs/task_18_rc_charging.png` — solve_ivp and exact curves overlap.
**Modified case:** Model drug concentration in blood after repeated doses. I would modify the ODE system.

---

## Task 19 — Numerical Optimization

**Inputs:** cost = 12x + 18y; capacity constraint 100x + 170y ≥ 1000; x, y ≥ 0.
**Operation:** constrained minimization with SLSQP, then a brute-force search over nearby integer combinations.
**Output:** continuous optimum x ≈ 0, y ≈ 5.882, cost ≈ 105.88; best integer solution x = 0, y = 6, cost = 108.
**Parameter change:** raising Type B's cost from 18 to 25 makes Type B no longer the cheapest per unit capacity.
**Interpretation:** Type B is cheaper per unit of capacity, so the optimum uses only Type B.
**Modified case:** Allocate cloud instances of different costs and capacities to meet minimum computing demand. I would modify the cost and constraint functions.

---

## Task 20 — Random Numbers and Monte Carlo Methods

**Inputs:** capacity = 1000; demand ~ Normal(850, 120); N = 100,000 simulations; seed 42.
**Operation:** Monte Carlo — sample demand, count overloads, estimate probability.
**Output:** estimated overload probability ≈ 10.56%; about 10,560 overload cases out of 100,000.
**Parameter change:** raising mean demand to 900 raises the overload probability; increasing capacity lowers it.
**Interpretation:** there is roughly a 1-in-10 chance the server is overloaded under the assumed demand distribution.
**Graph:** `outputs/task_20_monte_carlo.png` — the running probability converges to the final value as N grows.
**Modified case:** Estimate the probability that a hospital emergency department exceeds bed capacity. I would modify the mean and capacity variables.