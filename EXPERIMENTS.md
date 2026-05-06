# DTQEM v12.2 – Experiment Guide

This guide provides step‑by‑step experiments to explore quantum entanglement, decoherence, the quantum eraser, time sovereignty, and approximate wave‑particle balance using the **DTQEM v12.2** interactive GUI.

**Prerequisites:**  
- DTQEM v12.2 installed (see `README.md`).  
- Basic understanding of entanglement measures (visibility V, distinguishability D, concurrence C, negativity N, purity, entropy, fidelity).  
- Familiarity with the GUI sliders and buttons.

---

## Experiment 1: Temperature‑Induced Decoherence (Entanglement Lifetime)

**Goal:** Observe how increasing temperature destroys entanglement.

**Procedure:**

1. Set `θ = 180°` (maximally entangled Bell state).  
2. Set `t_obs = 1 μs`, `γφ₀ = 1000 1/s`, `γrel₀ = 300 1/s`, `ω = 0.025 eV`, `B = 0 T`.  
3. Gradually increase `T` from 0 K to 300 K.  
4. Watch the 1D interference fringes lose contrast and the visibility V drop.

**Expected result:**  
- At T = 0 K: V ≈ 1.0 (clear fringes).  
- At T = 300 K: V ≈ 0.12 (fringes almost vanish).  

**Analysis:** The thermal occupation number `n_th` increases, raising the decoherence rates `γφ`, `γ↓`, `γ↑`. The effective camera time `t_cam` dominates, switching sovereignty from particle to camera.

---

## Experiment 2: Magnetic Field Effect on Phase Coherence

**Goal:** Investigate how a magnetic field modifies distinguishability while preserving complementarity.

**Procedure:**

1. Set `θ = 90°`.  
2. Set `T = 0 K`, `t_obs = 1 μs`, `γφ₀ = 1000 1/s`, `γrel₀ = 0`.  
3. Vary `B` from 0 to 10 T in steps of 1 T.  
4. Note `V` and `D`. With pure dephasing, `D = 0` always; `V` decays as `exp(-γφ₀ t_obs)`.

**Expected result:**  
- `V` remains constant (pure dephasing with zero temperature and no relaxation gives `V = e^{-γφ₀ t_obs/2}`).  
- `D = 0` for all `B`. This shows that magnetic field alone does not create distinguishability.

**Analysis:** The Hamiltonian `H = (gμ_B B/2) σ_z⊗I` adds a phase to the off‑diagonal elements, but does not affect populations.

---

## Experiment 3: Inverse Calibration – From Visibility to Temperature

**Goal:** Given a target visibility, determine the temperature that would produce it.

**Procedure:**

1. Set `θ = 180°`, `t_obs = 1 μs`, `γφ₀ = 1000 1/s`, `γrel₀ = 300 1/s`.  
2. Assume you measure `V = 0.5` in a real experiment.  
3. Enter `0.5` in the `Target V` text box.  
4. Click **Inv T**.  

**Expected result:**  
The program prints the temperature (e.g., `T ≈ 173 K`). The slider for `T` updates automatically, and the interference fringes update accordingly.

**Analysis:** This demonstrates how DTQEM can be used to **calibrate real experiments** without a direct thermometer.

---

## Experiment 4: Time Sovereignty Map – Locating the Transition

**Goal:** Find the temperature (or angle) where particle and camera sovereignty are equal (`S_p = S_c = 0.5`).

**Procedure:**

1. Set `θ = 180°`, `t_obs = 1 μs`, `γφ₀ = 1000 1/s`, `γrel₀ = 300 1/s`.  
2. Click the **Time Map** button.  
3. A new window appears showing `S_p`, `S_c`, and `t_eff` vs. temperature.  

**Expected result:**  
- The curves cross at a temperature where `αK_eff = 0.5`.  

**Analysis:** This is the signature of the time‑sovereignty transition – the maximum uncertainty which clock dominates.

---

## Experiment 5: Quantum Eraser – Restoration by Deleting Which‑Path Information

**Goal:** Simulate the delayed‑choice quantum eraser.

**Procedure:**

1. Set `θ = 180°`, `T = 0 K`, `γφ₀ = 1000 1/s`, `γrel₀ = 0`.  
2. First, keep `t_obs = 10 μs` (camera active, recording).  
   → Fringes disappear (V small).  
3. Now reduce `t_obs` to `0.01 μs` (simulate erasing or never storing the which‑path information).  
   → Fringes reappear.  

**Expected result:**  
- Long `t_obs` (recording) → camera dominates → collapse.  
- Short `t_obs` (erasure) → particle dominates → interference returns.  

**Analysis:** This is a direct manifestation of the time‑sovereignty picture: erasing the record removes camera dominance.

---

## Experiment 6: Complementarity Check – V² + D² ≤ 1

**Goal:** Verify that the model **always** satisfies Bohr’s complementarity.

**Procedure:**

1. Randomly change any parameter (θ, T, B, γφ₀, …).  
2. Look at the **complementarity indicator** below the 1D fringe plot.  
3. Press **Validate** to run a full complementarity test over all angles (0°, 90°, 120°, 150°, 180°) and four temperatures (0, 77, 150, 300 K).  

**Expected result:**  
- The indicator always shows `✓ Complementarity satisfied`.  
- The validation report confirms `complementarity_satisfied: true`.  

**Analysis:** The Lindblad dynamics automatically preserve the positivity of the density matrix, which guarantees `V² + D² ≤ 1`.

---

## Experiment 7: Approaching the Symmetry Point (V ≈ D)

**Goal:** Observe that under fine‑tuned conditions, visibility and distinguishability can become **close** to each other and near \(1/\sqrt{2}\), but **exact equality is not forced** by the model.

**Procedure (pure dephasing):**

1. Set `θ = 90^\circ`.  
2. Turn off relaxation: `γrel₀ = 0`.  
3. Switch off the magnetic field: `B = 0` T.  
4. Set `γφ₀ = 1000` 1/s.  
5. Adjust the observation time to `t_obs = 693 μs` (this gives `K_eff = 1/√2` and `αK_eff = 0.5`).  
6. Set temperature `T = 0` K.  

**Expected result (pure dephasing):**  
You will see `V = e^{-1/2} ≈ 0.607` and `D = 0`.  
`V ≠ D` and `V ≠ 1/√2`.  

**Now add a small amount of relaxation:**  
Set `γrel₀ = 100` 1/s and `T = 100` K.  
You will see both `V` and `D` become positive and may become close to each other (e.g., `V ≈ 0.64`, `D ≈ 0.66`), but still not exactly `1/√2`.

**Conclusion:** The model respects complementarity (\(V^{2}+D^{2}\le 1\)) and can show approximate wave‑particle balance, but it does **not** produce a universal prediction \(V = D = 1/\sqrt{2}\). Any previous claim to that effect has been retracted in the white paper.

---

## Exporting Results

- **CSV:** Click **Save all** to export raw data (V, D, C, N, Pur, S, F_Bell) for all standard angles and temperatures.  
- **PDF:** Click **Export PDF** to save the current interactive figure with the DOI footer.  

---

**Enjoy exploring the dual‑time universe with DTQEM!**  
For theoretical background, read `WHITE_PAPER_EN.md` (English) or `WHITE_PAPER_AR.md` (Arabic).
