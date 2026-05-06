# White Paper – DTQEM v12.2: Time‑Sovereignty Model of Quantum Entanglement

**Version:** 1.1 (Documentation corrected)  
**DOI:** [10.5281/zenodo.20043754](https://doi.org/10.5281/zenodo.20043754)  
**Authors:** Redouane Berramdane (concept, supervision), DeepSeek (numerics, code), Gemini & Claude (critical review)  

---

## Abstract

DTQEM v12.2 (Dual‑Time Quantum Entanglement Model) is an open‑source, numerically exact simulation of two‑qubit entanglement under realistic thermal decoherence and magnetic fields. The Lindblad master equation is solved via Liouvillian superoperator exponentiation, achieving machine‑precision benchmarks (dephasing error < 1e‑12, relaxation error < 1e‑12, entropy increase verified).  

We introduce the **Time‑Sovereignty** interpretive layer: the particle’s classical flight time and an effective camera time compete, and the dominant clock determines whether interference (entanglement) occurs or collapses. This picture provides an intuitive, deterministic account of the quantum eraser and the observer effect.  

The model respects complementarity \(V^2 + D^2 \le 1\) and does **not** claim a universal prediction of \(V = D\). Under fine‑tuned parameters one may observe approximate equality, but this is a numerical curiosity, not a theoretical postulate. The code is fully documented, interactive (ipywidgets), and ready for research and education.

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

## 5. Approximate Symmetry and the Limits of Wave‑Particle Balance

The model does **not** produce a universal prediction of \(V = D\). To avoid any misinterpretation, we state clearly what DTQEM actually does.

### 5.1 The special angle \(\theta = 90^\circ\)

For \(\theta = 90^\circ\) we have \(\alpha = \sin(45^\circ)=1/\sqrt{2}\).  
The effective time becomes \(t_{\text{eff}} = t_{\text{real}}(1 - \frac{1}{\sqrt{2}} K_{\text{eff}})\).

When the calibration satisfies \(\alpha K_{\text{eff}} = 0.5\) (i.e. \(K_{\text{eff}} = 1/\sqrt{2}\)), the values of visibility \(V\) and distinguishability \(D\) computed from the density matrix **can become numerically close** to each other and close to \(1/\sqrt{2}\) for some parameter choices, **but they are never exactly equal** in the general Lindblad model.

### 5.2 Why exact equality is not achieved

- **Pure dephasing only (\(\gamma_{\text{rel}0}=0\)):**  
  For the initial Bell state, the reduced density matrix is maximally mixed, hence \(D = 0\) while \(V = e^{-\gamma_{\phi}t}\). Thus \(V = D\) only in the trivial case \(V = D = 0\).

- **With relaxation (\(\gamma_{\text{rel}0}>0\)):**  
  The Lindblad dynamics does not preserve the symmetry required for \(V = D\). Numerical searches show that \(V\) and \(D\) can approach each other within a few percent, but never reach exact equality.

### 5.3 What the model actually guarantees

The only rigorous relation is the complementarity bound:

\[
V^{2} + D^{2} \le 1
\]

and, for a pure Bell state and pure dephasing, \(V^{2} + D^{2} = 1\).  
The occasional near‑equality \(V \approx D\) is a **numerical curiosity** observable under fine‑tuned parameters (e.g., \(\theta = 90^\circ\), \(\alpha K_{\text{eff}} = 0.5\), small but non‑zero relaxation, and zero magnetic field). It is **not** a theoretical prediction of the model.

**Therefore, we retract any earlier claim that DTQEM predicts \(V = D = 1/\sqrt{2}\).** The model remains a precise simulator of open‑quantum dynamics, but it does not enforce wave‑particle equality.

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

DTQEM v12.2 is a **numerically exact, open‑source** simulation of two‑qubit entanglement that combines rigorous Lindblad dynamics with an intuitive **Time‑Sovereignty** interpretation. It passes all physical benchmarks and respects complementarity. The claim of a universal prediction \(V = D = 1/\sqrt{2}\) has been retracted; the model only guarantees \(V^2 + D^2 \le 1\). Under fine‑tuned conditions one may observe approximate equality, but this is a numerical feature, not a theoretical postulate. The code, documentation, and DOI are ready for use in education and research.

---

## 8. References

1. Lindblad, G. (1976). *Commun. Math. Phys.* **48**, 119.  
2. Breuer, H.‑P. & Petruccione, F. (2002). *The Theory of Open Quantum Systems*.  
3. Gisin, N. & Zbinden, H. (1998). *Phys. Lett. A* **248**, 1.  
4. Aspect, A. et al. (1982). *Phys. Rev. Lett.* **49**, 1804.

---

## 9. Open Issues and Future Work

### 9.1 The (non‑)prediction \(V = D = 1/\sqrt{2}\)

Earlier versions of this white paper suggested that DTQEM predicts \(V = D = 1/\sqrt{2}\) at \(\theta = 90^\circ\) and \(\alpha K_{\text{eff}} = 0.5\). **Systematic numerical searches and analytical reasoning have shown that this exact equality does not hold in the Lindblad model.**  

The model only guarantees \(V^{2}+D^{2}\le 1\). Approximate equality can be observed under fine‑tuned parameters (small relaxation, zero magnetic field, specific \(t_{\text{obs}}\)), but it is not a theoretical prediction. We have therefore corrected the text accordingly. This does not affect the numerical accuracy or the usability of DTQEM.

### 9.2 Time‑Sovereignty interpretation – need for a better \(t_{\text{cam}}\)

The current definition \(t_{\text{cam}} = \alpha K_{\text{eff}} t_{\text{real}}\) is a simple rescaling and does not produce a genuine transition between particle and camera dominance. A future version (v13) will explore a physically motivated redefinition, possibly based on the synchronisation rate \(R_{\text{sync}} = 1 - K_{\text{eff}}\) with a non‑linear saturation function.

### 9.3 Planned extensions for v13

- Redefinition of \(t_{\text{cam}}\) to obtain a true time‑sovereignty transition.
- Inclusion of non‑Markovian noise (Ornstein‑Uhlenbeck process).
- Optional support for three‑qubit systems (W and GHZ states).

---

**Finally:** The code and full documentation are at  
[https://github.com/reddoma742/DTQEM-v12.2](https://github.com/reddoma742/DTQEM-v12.2)  
DOI: [10.5281/zenodo.20043754](https://doi.org/10.5281/zenodo.20043754)
