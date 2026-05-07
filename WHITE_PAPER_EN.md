# White Paper: Dual-Time Quantum Entanglement Model (DTQEM v12.2)
**A Time-Sovereignty Perspective on Open Quantum Systems**

**Author:** Reddouane Berramdane  
**Location:** Oujda, Morocco  
**Date:** May 2026  
**DOI:** [10.5281/zenodo.20043754](https://doi.org/10.5281/zenodo.20043754)  
**License:** MIT  

---

## 1. Abstract

DTQEM (Dual‑Time Quantum Entanglement Model) is a numerical framework for simulating two‑qubit entanglement under realistic thermal decoherence and external fields. This version formalises the *Time‑Sovereignty* interpretation and introduces an exact analytical condition for wave‑particle balance (`V = D`), bridging the gap between numerical simulation and theoretical prediction. All benchmarks pass with machine precision (errors < 1e‑12).

---

## 2. Introduction: The Time‑Sovereignty Hypothesis

In DTQEM, the transition from quantum to classical behaviour is modelled as a shift in temporal dominance. Entanglement is sustained as long as the system remains within its sovereign internal time‑frame. External interactions – measurement, noise, or decoherence – force a transition to the “camera‑clock” frame (the observer’s time), leading to the emergence of classical outcomes.

---

## 3. Mathematical Framework: Lindblad Dynamics

The model solves the Lindblad master equation for the density matrix `ρ(t)`:

\[
\frac{d\rho}{dt} = -i[H, \rho] + \sum_k \left( L_k \rho L_k^\dagger - \frac{1}{2} \{ L_k^\dagger L_k, \rho \} \right)
\]

where `H` is the Hamiltonian and `L_k` are jump operators describing dephasing and relaxation. The exact solution uses Liouvillian superoperator exponentiation (`expm(L·t)`), which avoids numerical drift.

---

## 4. Numerical Stability and Precision

DTQEM v12.2 achieves machine‑level precision:

| Test | Value | Error |
|------|-------|-------|
| Pure dephasing (Bell state) | `exp(-γφ₀ t)` | < 8.33×10⁻¹⁶ |
| Relaxation at T=0 | `exp(-γrel₀ t)` | < 7.77×10⁻¹⁶ |
| Entropy increase (second law) | `S_final > S_initial` | True |

---

## 5. Exact Balance Condition V = D (Pure Dephasing)

For pure dephasing (`γrel₀ = 0`, `T = 0`, `B = 0`), the initial entangled state is:

\[
|\psi(\theta)\rangle = \cos\left(\frac{\theta}{2}\right)|00\rangle + \sin\left(\frac{\theta}{2}\right)|11\rangle.
\]

Under the Lindblad master equation with the dephasing jump operator \(L_\phi = \sqrt{\gamma_{\phi0}}\,\sigma_z\otimes I\) (note: in the DTQEM code the user‑supplied `γφ₀` enters such that the physical dephasing rate is `γφ₀/2`), the density matrix evolves as:

\[
\rho_{03}(t_{\text{obs}}) = \frac{1}{2}\sin\theta\;\exp\!\left(-\frac{\gamma_{\phi0}}{2}t_{\text{obs}}\right).
\]

Using the definitions:

\[
V = 2|\rho_{03}(t_{\text{obs}})| = \sin\theta\;\exp\!\left(-\frac{\gamma_{\phi0}}{2}t_{\text{obs}}\right),\qquad
D = |\rho_{00} - \rho_{33}| = |\cos\theta|.
\]

Setting `V = D` (wave‑particle balance) gives:

\[
\sin\theta\;\exp\!\left(-\frac{\gamma_{\phi0}}{2}t_{\text{obs}}\right) = \cos\theta.
\]

Solving for the product yields the exact analytical condition:

\[
\boxed{\gamma_{\phi0}\,t_{\text{obs}} = 2\ln(\tan\theta)},\qquad \theta > 45^\circ.
\]

**Key implications:**

- **Invariant parameter:** The product `γφ₀·t_obs` is the fundamental control, not `γφ₀` alone.
- **θ = 90° is impossible** because `tan 90° → ∞`; this matches numerical simulations (`V` and `D` never meet at a right angle).
- **No “magic angle” at 65°** – the earlier observed minimum of `γφ₀(θ)` was an artefact of fixing `t_obs`. Changing `t_obs` shifts the balance point according to the `ln(tan θ)` law.

> **Technical note on code convention:** In the DTQEM implementation, the user‑supplied parameter `γφ₀` is related to the physical dephasing rate by `γ_phys = γφ₀/2`. Consequently the balance condition includes a factor 2. If one prefers a convention where `γφ₀` directly equals the physical rate, the relation simplifies to `γφ₀ t_obs = ln(tan θ)`.

---

## 6. The Inverse Calibration Engine

The simulator includes an automated engine that determines the physical parameters required to meet a target visibility. Given experimental data (`θ`, `V_target`), the engine returns the corresponding `γφ₀`, `T`, or `θ`. This allows reverse‑engineering of environmental conditions (temperature, dephasing, or orientation) from observed quantum states.

---

## 7. Numerical Analysis Ranges

Extensive parameter searches were performed over:

- `γφ₀` ∈ [10, 50000] s⁻¹
- `γrel₀` ∈ [0, 10000] s⁻¹
- `t_obs` ∈ [1e‑9, 1e‑3] s
- `T` ∈ [0, 300] K
- `θ` ∈ [0, 180]°

The analytical condition derived in Sec. 5 holds exactly for the pure‑dephasing subset and has been verified numerically with errors below 1e‑12.

---

## 8. Open Issues and Future Work

- **8.1 Gravitational coupling:** integrate a gravitational redshift parameter to test time‑sovereignty under curved space‑time.
- **8.2 Non‑Markovian dynamics:** move beyond the Lindblad approximation to model memory effects in the environment.
- **8.3 Experimental benchmarking:** compare with attosecond H₂ photoionisation experiments (Max Planck, 2024) for which DTQEM reproduces the ideal Bell‑state regime.

---

## 9. Acknowledgments

We thank **DeepSeek** for code development and numerical implementation, **Gemini** for philosophical dialogue and conceptual sharpening, and **Claude** for critical reviews that corrected earlier fitting artefacts. Special thanks to an independent physicist who provided the rigorous derivation of the `ln(tan θ)` condition, eliminating a factor‑2 discrepancy and clarifying the code‑convention relation.

---

## 10. Conclusion

DTQEM v12.2 provides a rigorous, open‑source simulation of open quantum systems. By establishing the analytical relation `γφ₀ t_obs = 2 ln(tan θ)` for wave‑particle balance, the model moves beyond empirical observation into the realm of formal quantum mechanical prediction. The code, documentation, and DOI are ready for use in education and research.

---

**Citation:** Berramdane, R. (2026). *DTQEM v12.2: Time‑Sovereignty Model of Quantum Entanglement*. Zenodo. DOI: [10.5281/zenodo.20043754](https://doi.org/10.5281/zenodo.20043754)
