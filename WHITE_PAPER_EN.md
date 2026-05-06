# White Paper: Dual-Time Quantum Entanglement Model (DTQEM v12.2)
**A Time-Sovereignty Perspective on Open Quantum Systems**

**Author:** Redouane Berramdane
**Location:** Oujda, Morocco
**Date:** May 2026
**DOI:** [10.5281/zenodo.20043754](https://doi.org/10.5281/zenodo.20043754)
**License:** MIT

---

## 1. Abstract
The DTQEM v12.2 (Dual-Time Quantum Entanglement Model) is a numerical framework designed to simulate two-qubit entanglement dynamics under realistic conditions of thermal decoherence and external fields. This version formalizes the "Time-Sovereignty" interpretation, which views quantum entanglement as a regime where a particleâ€™s internal temporal frame predominates over the external observerâ€™s frame. This paper documents the modelâ€™s adherence to the complementarity principle and clarifies the boundaries of its current numerical predictions.

## 2. Introduction: The Time-Sovereignty Hypothesis
In DTQEM, the transition from quantum to classical behavior is modeled as a shift in temporal dominance. Entanglement is sustained as long as the system remains within its "sovereign" internal time-frame. External interactionsâ€”measurement, noise, or decoherenceâ€”force a transition to the "Camera-Clock" frame (the observerâ€™s time), leading to the emergence of classical outcomes.

## 3. Mathematical Framework: Lindblad Dynamics
The model solves the Lindblad Master Equation to track the evolution of the density matrix rho(t):
d(rho)/dt = -i[H, rho] + sum_k (L_k rho L_k* - 1/2 {L_k* L_k, rho})
Where H represents the Hamiltonian (including magnetic and electric field interactions) and L_k are the jump operators representing dephasing and relaxation.

## 4. Key Metrics
* Visibility (V): Quantifies the wave-like interference patterns.
* Distinguishability (D): Quantifies the particle-like path information.
* Complementarity: The model strictly enforces the inequality V^2 + D^2 <= 1.
* Concurrence (C): Measures the degree of entanglement between qubits.

## 5. Numerical Stability and Precision
DTQEM v12.2 utilizes Liouvillian superoperator exponentiation, achieving machine-level precision:
* Dephasing Stability: Verified at < 8.33e-16.
* Relaxation Accuracy: Verified at < 7.77e-16.

## 6. The Inverse Calibration Engine
The simulator includes an automated engine to determine the physical parameters required to meet specific visibility targets. This allows for reverse-engineering the environmental conditions (Temperature, Dephasing, or Orientation) that lead to observed quantum states.

## 7. Numerical Analysis of the Symmetry Point (theta = 90)
A core focus of this version was the investigation of wave-particle duality at the geometric orientation of 90 degrees. While this point represents maximum geometric symmetry, the model treats the evolution of V and D as independent physical processes governed by the environment.

## 8. Crucial Clarification: Absence of V = D = 1/sqrt(2) Prediction
Extensive numerical searches were conducted across a broad parameter space to identify a region where wave-particle equality (V = D) emerges naturally.
* Parameter Ranges Explored:
    - gamma_phi0 in [100, 5000] 1/s
    - gamma_rel0 in [0, 1000] 1/s
    - t_obs in [10^-7, 10^-4] s
    - T in [0, 300] K
    - B in [0, 2] T
    - E in [0, 10] V/m
* Conclusion: The current Lindblad-based formulation does NOT predict or enforce the condition V = D = 1/sqrt(2). The system remains constrained solely by the complementarity bound V^2 + D^2 <= 1. Any observed convergence is a local numerical result and not a general theoretical prediction of the v12.2 framework.

## 9. Future Work and Open Issues
* 9.1 Gravitational Coupling: Integrating a gravitational shift parameter to simulate "Time-Sovereignty" under varying space-time curvature.
* 9.2 Non-Markovian Dynamics: Moving beyond the Lindblad approximation to model memory effects in the environment.
* 9.3 Experimental Calibration: Aligning the "Missing Factor" in the symmetry map with real-world ion-trap or photon-counting data.

## 10. Conclusion
DTQEM v12.2 provides a rigorous and honest simulation of open quantum systems. By acknowledging the limits of standard Lindblad dynamics regarding wave-particle equality, this model serves as a transparent baseline for future research into the fundamental nature of time and entanglement.

---
Citation: Berramdane, R. (2026). DTQEM v12.2: Time-Sovereignty Model of Quantum Entanglement. Zenodo. DOI: 10.5281/zenodo.20043754
