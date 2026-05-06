# DTQEM v12.2: Time‑Sovereignty Model of Quantum Entanglement

**DOI:** [10.5281/zenodo.20043754](https://doi.org/10.5281/zenodo.20043754)  
**License:** MIT  
**Author:** Redouane Berramdane (with assistance from DeepSeek, Gemini, Claude)

---

![Berramdane Model Result](images/DTQEM_v12.2.jpg)

## 🌟 Overview

**DTQEM v12.2** (Dual-Time Quantum Entanglement Model) is a numerically exact, open-source simulator of two-qubit entanglement under realistic thermal decoherence and magnetic fields. 

The model introduces the **Time‑Sovereignty** interpretation: entanglement represents a regime where the particle’s internal temporal frame dominates. Measurement and decoherence are viewed as the transition where the external "camera-clock" (the observer/environment) imposes its own frame, leading to the emergence of classical behavior.

## 🚀 Key Features

* **Exact Lindblad Dynamics:** Solves the master equation via Liouvillian superoperator exponentiation with machine-level precision (error < 1e-15).
* **Time-Sovereignty Mapping:** A unique visual tool to track the transition between particle-time and camera-time dominance.
* **Comprehensive Metrics:** Real-time calculation of Visibility ($V$), Distinguishability ($D$), Concurrence ($C$), and von Neumann Entropy ($S$).
* **Inverse Calibration Engine:** Automatically computes physical parameters ($\gamma_{\phi 0}$, $T$, or $\theta$) required to reach specific experimental visibility targets.
* **Interactive GUI:** A high-performance dashboard using `ipywidgets`, optimized for both Desktop and Mobile research.

## 🔬 Scientific Analysis: The Symmetry Point

A core focus of DTQEM v12.2 is the analysis of wave-particle duality at the geometric orientation of **$\theta = 90^\circ$**:

* **Numerical Convergence:** At this specific configuration, the model explores the maximum balance between path information and interference patterns.
* **Physical Integrity:** The simulator does not enforce arbitrary equality between $V$ and $D$. Instead, it demonstrates how they naturally converge toward each other under ideal conditions while strictly obeying the fundamental complementarity bound: $V^2 + D^2 \le 1$.
* **Thermal Robustness:** The simulation shows that as environmental noise (relaxation) increases, the system reflects realistic quantum drift, moving away from ideal symmetry in full accordance with open quantum system dynamics.

## 🛠 Numerical Stability & Diagnostics

The engine includes a robust diagnostic suite to ensure that the "Time Sovereignty" of the simulation remains physically grounded:

1.  **Dynamical Compensation:** Adjusts effective time parameters ($t_{eff}$) to accurately reflect the impact of thermal occupancy ($n_{th}$) and dephasing ($\gamma_\phi$).
2.  **Machine-Level Benchmarking:**
    * **Dephasing Stability:** Verified at $< 8.33 \times 10^{-16}$ precision.
    * **Relaxation Accuracy:** Verified at $< 7.77 \times 10^{-16}$ precision.
3.  **Entropy Validation:** Strictly enforces the Second Law of Thermodynamics regarding entropy growth during decoherence.

## 📦 Installation & Quick Start

```bash
# Clone the repository
git clone [https://github.com/reddoma742/DTQEM-v12.2-Time-Sovereignty-Model-of-Quantum-Entanglement.git](https://github.com/reddoma742/DTQEM-v12.2-Time-Sovereignty-Model-of-Quantum-Entanglement.git)

# Enter the directory
cd DTQEM-v12.2-Time-Sovereignty-Model-of-Quantum-Entanglement

# Install dependencies
pip install -r requirements.txt

# Launch the simulator
python dtqem_v12_2.py
