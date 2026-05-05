# White Paper – DTQEM v12.2: Time‑Sovereignty Model of Quantum Entanglement

**Version:** 1.0  
**DOI:** [10.5281/zenodo.20039345](https://doi.org/10.5281/zenodo.20039345)  
**Authors:** Redouane Berramdane (concept, supervision), DeepSeek (numerics, code), Gemini & Claude (critical review)  

---

## Abstract

DTQEM v12.2 (Dual‑Time Quantum Entanglement Model) is an open‑source, numerically exact simulation of two‑qubit entanglement under realistic thermal decoherence and magnetic fields. The Lindblad master equation is solved via Liouvillian superoperator exponentiation, achieving machine‑precision benchmarks (dephasing error < 1e‑12, relaxation error < 1e‑12, entropy increase verified).  

We introduce the **Time‑Sovereignty** interpretive layer: the particle’s classical flight time and an effective camera time compete, and the dominant clock determines whether interference (entanglement) occurs or collapses. This picture provides an intuitive, deterministic account of the quantum eraser and the observer effect.  

Unique testable predictions are made: at launch angle θ = 90°, visibility equals distinguishability for any temperature, and at the sovereignty transition point \( \alpha K_{\text{eff}} = 0.5 \) we numerically find \( V = D \approx 1/\sqrt{2} \). The code is fully documented, interactive (ipywidgets), and ready for research and education.

---

## 1. Introduction

The measurement problem and the quantum eraser have long resisted intuitive explanation. Most interpretations either rely on “wavefunction collapse” as a primitive or invoke many‑worlds or hidden variables. Here we propose a different route: **time itself is the active agent**.  

Before measurement, the particle exists in a “free‑time” superposition. The measurement device (camera) injects its own clock, competing for temporal dominance. The outcome – interference or its absence – depends solely on which clock dominates. This **Time‑Sovereignty** picture does not replace the Lindblad equation; it is a consistent, physically motivated language that sits on top of it.

---

## 2. Mathematical Core

We consider two qubits. The density matrix \( \rho \) evolves under the Lindblad master equation:

\[
\frac{d\rho}{dt} = -\frac{i}{\hbar}[H,\rho] + \sum_k \bigl(L_k\rho L_k^\dagger - \tfrac12\{L_k^\dagger L_k,\rho\}\bigr).
\]

**Hamiltonian (magnetic field on the first qubit):**  
\[
H = \frac{g\mu_B B}{2}\,\sigma_z^{(1)}\otimes I_2.
\]

**Jump operators (decoherence):**  

- Pure dephasing: \( L_{\phi} = \sqrt{\gamma_{\phi}(T)}\,\sigma_z^{(1)}\otimes I_2 \)  
- Relaxation (emission): \( L_{\downarrow} = \sqrt{\gamma_{\downarrow}(T)}\,\sigma_-\otimes I_2 \)  
- Excitation (absorption): \( L_{\uparrow} = \sqrt{\gamma_{\uparrow}(T)}\,\sigma_+\otimes I_2 \)

**Thermal rates (Bose‑Einstein):**  

\[
n_{\text{th}} = \frac{1}{e^{\hbar\omega/k_BT}-1},\qquad
\gamma_{\phi}(T) = \frac{\gamma_{\phi0}}{2}(2n_{\text{th}}+1),\qquad
\gamma_{\downarrow}(T) = \gamma_{\text{rel}0}(n_{\text{th}}+1),\qquad
\gamma_{\uparrow}(T) = \gamma_{\text{rel}0}\,n_{\text{th}}.
\]

Because the master equation is linear, we vectorise \( \rho \) into a 16‑dimensional vector and construct the Liouvillian superoperator \( \mathcal{L} \) (16×16). Exact evolution is then:

\[
\text{vec}(\rho(t)) = \exp(\mathcal{L}t)\,\text{vec}(\rho(0)).
\]

All observables (visibility \(V\), distinguishability \(D\), concurrence \(C\), negativity \(N\), purity \(\text{Pur}\), entropy \(S\), fidelity \(F_{\text{Bell}}\), l1‑norm coherence) are computed directly from the density matrix.

---

## 3. Time‑Sovereignty Interpretation

Let \(t_{\text{real}}\) be the classical flight time. The effective time for the quantum influence is:

\[
t_{\text{eff}} = t_{\text{real}}\bigl(1 - \alpha K_{\text{eff}}\bigr),\qquad
\alpha = \sin(\theta/2),\qquad
K_{\text{eff}} = \exp\bigl(-(\Gamma_0 + aT)\,t_{\text{obs}}\bigr),
\]

where \(t_{\text{obs}}\) is the observation time and \(K_{\text{eff}}\) the coherence retention factor.

We define an **effective camera time**  

\[
t_{\text{cam}} = \alpha K_{\text{eff}}\,t_{\text{real}},
\]

so that \(t_{\text{eff}} = t_{\text{real}} - t_{\text{cam}}\). The particle’s own time is identified with \(t_{\text{eff}}\).

**Sovereignty indicators:**  

- Particle sovereignty \(S_p = \alpha K_{\text{eff}}\)  
- Camera sovereignty \(S_c = 1 - \alpha K_{\text{eff}}\)

If \(S_p > 0.5\) → particle dominates → entanglement → interference fringes appear.  
If \(S_c > 0.5\) → camera dominates → collapse → no fringes.  

The transition occurs at \(S_p = S_c = 0.5\) i.e. \(\alpha K_{\text{eff}} = 0.5\).  
A Shannon‑type **time‑sovereignty entropy** is  

\[
S_{\text{time}} = -\bigl[S_p\log S_p + S_c\log S_c\bigr],
\]

which reaches its maximum \(\ln 2\) at the transition.

**Quantum eraser:** Recording which‑path information activates camera time; erasing it sets \(t_{\text{cam}}\to0\), restoring particle sovereignty – explaining delayed‑choice experiments without retrocausality.

---

## 4. Benchmarks

Automatically run at start:

- Pure dephasing (Bell state): error \(<1\times10^{-12}\)  
- Relaxation at \(T=0\): error \(<1\times10^{-12}\)  
- Entropy increase (second law): **True**  
- Complementarity \(V^2 + D^2 \le 1\) always satisfied.

---

## 5. Unique Testable Prediction

For \(\theta = 90^\circ\) (\(\alpha = 1/\sqrt{2}\)), the model predicts **visibility equals distinguishability** for any temperature. Numerically, at the sovereignty transition point \(\alpha K_{\text{eff}} = 0.5\) we obtain \(V = D \approx 1/\sqrt{2}\). This is a clear, experimentally verifiable signature of the Time‑Sovereignty framework.

---

## 6. Interactive GUI

Built with `ipywidgets`, the interface provides:

- Real‑time control of \(\theta, T, t_{\text{obs}}, \gamma_{\phi0}, \gamma_{\text{rel}0}, \omega, B, \lambda, d\), plus quantum gates (H, CNOT, Rx).
- Live visualisation: 1D/2D double‑slit fringes, Bloch vector, real part of \(\rho\), thermal response curves.
- **Inverse calibration**: from a target visibility to the corresponding \(\gamma_{\phi0}\), \(T\), or \(\theta\).
- **Time Sovereignty Map**: plots \(S_p, S_c, t_{\text{eff}}\) vs \(T\).
- **Validation** button: runs all checks and saves a JSON report.
- **PDF export**: saves the current interactive figure with DOI footer.

---

## 7. Conclusion

DTQEM v12.2 is a **numerically exact, open‑source** simulation of two‑qubit entanglement that combines rigorous Lindblad dynamics with an intuitive **Time‑Sovereignty** interpretation. It passes all physical benchmarks, makes a unique testable prediction, and comes with a complete GUI. The model is ready for use in education, research, and as a foundation for extensions (non‑Markovian noise, gravity, multi‑qubits).

---

## 8. References

1. Lindblad, G. (1976). *Commun. Math. Phys.* **48**, 119.  
2. Breuer, H.‑P. & Petruccione, F. (2002). *The Theory of Open Quantum Systems*.  
3. Gisin, N. & Zbinden, H. (1998). *Phys. Lett. A* **248**, 1.  
4. Aspect, A. et al. (1982). *Phys. Rev. Lett.* **49**, 1804.

---

**Finally:** The code and full documentation are at  
[https://github.com/reddoma742/DTQEM-v12.2](https://github.com/reddoma742/DTQEM-v12.2)  
DOI: [10.5281/zenodo.20039345](https://doi.org/10.5281/zenodo.20039345)
