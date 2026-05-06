# DTQEM v12.2 – Open Issues & Future Work

## ✅ What has been achieved

- Machine‑precision benchmarks (dephasing error < 1e‑12, relaxation < 1e‑12, entropy increase verified).
- Complementarity V² + D² ≤ 1 always satisfied.
- Inverse calibration (γφ₀, T, θ) from target visibility.
- Full Lindblad + Liouvillian + ipywidgets GUI.
- DOI registration (10.5281/zenodo.20043754).

## ⚠️ What is still open / not fully achieved

1. **Time‑Sovereignty interpretation (`t_camera` definition)** –  
   In the current form, `t_cam = α K_eff t_real` remains a simple re‑scaling and does not produce a true transition (particle always dominates for our standard parameters). A better definition of `t_cam` is needed.

2. **Unique prediction `V = D` at θ = 90°** –  
   Numerically, the equality is not strictly observed for all temperatures when `γrel₀ > 0`. This indicates that either the prediction requires additional conditions (e.g., `γrel₀ = 0`) or the Lindblad structure breaks the symmetry. The issue will be re‑examined theoretically.

## 🔮 Future work (v13)

- Redefine `t_camera` based on the **actual synchronisation rate** `R_sync = 1 - K_eff`, possibly using a logistic or saturation function to produce a true transition.
- Derive the condition under which `V = D` holds exactly; test numerically with a wider range of parameters.
- Possibly add non‑Markovian noise or a third qubit.
