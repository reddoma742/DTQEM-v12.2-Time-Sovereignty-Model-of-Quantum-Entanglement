# DTQEM v12.2: Time‑Sovereignty Model of Quantum Entanglement

**DOI:** [10.5281/zenodo.20043754](https://doi.org/10.5281/zenodo.20043754)  
**License:** MIT  
**Author:** Redouane Berramdane (with assistance from DeepSeek, Gemini, Claude)

![Berramdane Model Result](images/DTQEM_v12.2.jpg)

## 🌟 Overview

**DTQEM v12.2** (Dual‑Time Quantum Entanglement Model) is a numerically exact, open‑source simulator of two‑qubit entanglement under realistic thermal decoherence and magnetic fields. 

It introduces the **Time‑Sovereignty** interpretation: entanglement occurs when the particle’s internal clock dominates the interaction; measurement forces the external “camera‑clock” to impose its own temporal frame, leading to collapse of the quantum coherence.

## 🚀 Key Features

- **Exact Lindblad dynamics:** Solves the master equation via Liouvillian superoperator exponentiation with machine‑precision benchmarks (dephasing error < 1e‑12, relaxation error < 1e‑12, entropy increase verified).
- **Comprehensive metrics:** Tracks visibility \(V\), distinguishability \(D\), concurrence \(C\), negativity \(N\), purity \(\text{Pur}\), von Neumann entropy \(S\), and fidelity to the Bell state.
- **Inverse calibration engine:** Automatically estimates \(\gamma_{\phi0}\), \(T\), or \(\theta\) required to reach a target visibility (e.g., from experimental data).
- **Interactive GUI:** Fully functional dashboard using `ipywidgets` – works on desktops and mobile devices.
- **Time‑Sovereignty mapping:** Visualises the transition between particle‑time and camera‑time dominance (\(S_p\) vs \(S_c\) as functions of temperature).

## 🔬 Scientific foundation and symmetry

The model strictly obeys Bohr’s complementarity principle:

\[
V^{2} + D^{2} \le 1.
\]

For the special orientation \(\theta = 90^\circ\) and under fine‑tuned conditions (pure dephasing, zero magnetic field, \(t_{\text{obs}}\) chosen so that \(\alpha K_{\text{eff}} = 0.5\)), the values of \(V\) and \(D\) can become **numerically close** to each other and to \(1/\sqrt{2}\). However, **exact equality is not enforced** by the Lindblad dynamics. The model does **not** claim a universal prediction of \(V = D\); the occasional near‑equality is an interesting numerical feature, not a theoretical postulate.

## ⚙️ Numerical stability and diagnostics

The simulator includes built‑in diagnostic tools that guarantee:

- Trace preservation (\(\operatorname{Tr}\rho = 1\))
- Hermiticity and positivity of the density matrix
- Complementarity \((V^{2}+D^{2}\le 1)\) automatically enforced

### Benchmarks

| Test Category | Status | Precision |
| :--- | :---: | :--- |
| **Pure dephasing (Bell state)** | ✅ Passed | \(< 8.33\times10^{-16}\) |
| **Relaxation at \(T=0\)** | ✅ Passed | \(< 7.77\times10^{-16}\) |
| **Entropy increase (second law)** | ✅ Passed | True |
| **Complementarity** | ✅ Always satisfied | \(V^{2}+D^{2}\le 1\) |

## 🛠 Installation & Quick Start

```bash
git clone https://github.com/reddoma742/DTQEM-v12.2.git
cd DTQEM-v12.2
pip install -r requirements.txt
python dtqem_v12_2.py
