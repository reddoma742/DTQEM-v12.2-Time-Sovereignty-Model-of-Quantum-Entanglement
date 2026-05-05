
markdown
![Berramdane Model Result](images/DTQEM v12.2.jpg)


# DTQEM-v12.2-Time-Sovereignty-Model-of-Quantum-Entanglement
DTQEM v12.2 is an open‑source, exact simulator of two‑qubit entanglement under thermal decoherence and magnetic fields. It introduces the Time‑Sovereignty interpretation: entanglement occurs when the particle’s clock dominates; measurement forces camera‑clock dominance. Includes inverse calibration, unique prediction V=D at θ=90°, and full GUI.
# DTQEM v12.2 – Time‑Sovereignty Model of Quantum Entanglement

**DOI: 10.5281/zenodo.20039345**  
**License: MIT**

## Overview

DTQEM v12.2 is a numerically exact, open‑source simulator of two‑qubit entanglement under realistic thermal decoherence and magnetic fields. It solves the Lindblad master equation via Liouvillian superoperator exponentiation (machine‑precision benchmarks). The novel **Time‑Sovereignty** interpretation rephrases measurement as a competition between the particle’s clock and the camera’s clock – the dominant clock determines entanglement or collapse.

## Key features

- Exact Lindblad dynamics (expm(L·t))
- All standard entanglement/coherence metrics (V, D, C, N, Pur, S, F_Bell, l1)
- Inverse calibration: from target visibility to γφ₀, T, or θ
- Unique testable prediction: at θ=90°, V = D for any temperature
- Interactive ipywidgets GUI (works on desktop and mobile)
- Time Sovereignty Map (S_p, S_c, t_eff vs T)
- Automated validation + PDF export with DOI footer

## Installation & quick start

```bash
git clone https://github.com/reddoma742/DTQEM-v12.2.git
cd DTQEM-v12.2
pip install -r requirements.txt
python dtqem_v12_2.py
