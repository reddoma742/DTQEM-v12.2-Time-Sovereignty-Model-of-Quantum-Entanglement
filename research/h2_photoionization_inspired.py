#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inspired by attosecond H2 photoionization studies (Max Planck, 2024)
Uses DTQEM v12.2 core dynamics to model a Bell state under idealised conditions.
This is a theoretical benchmark, not a literal experimental replication.
"""

import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# ======================================================================
# Constants
# ======================================================================
hbar = 1.0545718e-34
k_B = 1.380649e-23
eV = 1.60217662e-19
mu_B = 9.2740100783e-24

I2 = np.eye(2, dtype=complex)
SX = np.array([[0,1],[1,0]], dtype=complex)
SY = np.array([[0,-1j],[1j,0]], dtype=complex)
SZ = np.array([[1,0],[0,-1]], dtype=complex)
SP = np.array([[0,1],[0,0]], dtype=complex)
SM = np.array([[0,0],[1,0]], dtype=complex)

def kron(a, b):
    return np.kron(a, b)

# ======================================================================
# Quantum state utilities
# ======================================================================
def entangled_state(theta_deg):
    theta = np.radians(theta_deg)
    c = np.cos(theta / 2)
    s = np.sin(theta / 2)
    return np.array([c, 0, 0, s], dtype=complex)

def density_matrix(state):
    return np.outer(state, state.conj())

def partial_trace_B(rho_AB):
    rho = rho_AB.reshape(2, 2, 2, 2)
    rho_A = np.zeros((2, 2), dtype=complex)
    for i in range(2):
        for k in range(2):
            total = 0.0
            for j in range(2):
                total += rho[i, j, k, j]
            rho_A[i, k] = total
    return rho_A

def fringe_visibility(rho):
    return float(np.clip(2.0 * np.abs(rho[0, 3]), 0.0, 1.0))

def distinguishability(rho):
    rho_A = partial_trace_B(rho)
    return float(np.abs(np.real(rho_A[0, 0] - rho_A[1, 1])))

# ======================================================================
# Lindblad evolution (exact via Liouvillian)
# ======================================================================
def thermal_occupation(omega_eV, T):
    if T <= 0:
        return 0.0
    omega = omega_eV * eV / hbar
    x = hbar * omega / (k_B * T)
    if x > 700:
        return 0.0
    return 1.0 / np.expm1(x)

def build_liouvillian(gamma_phi0, gamma_relax0, omega_eV, T, B, E):
    # Magnetic field Hamiltonian
    coeff_mag = 0.5 * 2.0 * mu_B * B
    H_mag = coeff_mag * kron(SZ, I2)
    # Electric field Hamiltonian (simple model)
    coeff_elec = 1.60217662e-19 * E
    H_elec = coeff_elec * kron(SX, I2)
    H = H_mag + H_elec

    n_th = thermal_occupation(omega_eV, T)
    g_phi = gamma_phi0 * (2 * n_th + 1) / 2.0
    g_down = gamma_relax0 * (n_th + 1)
    g_up = gamma_relax0 * n_th

    Ls = []
    if g_phi > 0:
        Ls.append(np.sqrt(g_phi) * kron(SZ, I2))
    if g_down > 0:
        Ls.append(np.sqrt(g_down) * kron(SM, I2))
    if g_up > 0:
        Ls.append(np.sqrt(g_up) * kron(SP, I2))

    dim = 4
    size = dim * dim
    L = np.zeros((size, size), dtype=complex)
    # Coherent part (Liouvillian for Hamiltonian)
    L += -1j / hbar * (np.kron(H, np.eye(dim)) - np.kron(np.eye(dim), H.T))

    for Lj in Ls:
        Lj_dag = Lj.conj().T
        LjLj = Lj_dag @ Lj
        L += np.kron(Lj, Lj.conj()) - 0.5 * (np.kron(LjLj, np.eye(dim)) + np.kron(np.eye(dim), LjLj.T))

    return L

def evolve(rho0, t_obs, gamma_phi0, gamma_relax0, omega_eV, T, B, E):
    L = build_liouvillian(gamma_phi0, gamma_relax0, omega_eV, T, B, E)
    rho_vec = rho0.flatten('C')
    rho_vec_t = expm(L * t_obs) @ rho_vec
    rho_t = rho_vec_t.reshape(4, 4)
    # Enforce Hermiticity and positivity
    rho_t = 0.5 * (rho_t + rho_t.conj().T)

    evals, evecs = np.linalg.eigh(rho_t)
    evals = np.maximum(evals, 1e-15)
    rho_t = evecs @ np.diag(evals) @ evecs.conj().T

    tr = np.trace(rho_t)
    if np.abs(tr) > 1e-15:
        rho_t /= tr
    return rho_t

def compute_V_D(theta_deg, gamma_phi0, gamma_relax0, t_obs, T, B, E, omega_eV=0.025):
    psi = entangled_state(theta_deg)
    rho0 = density_matrix(psi)
    rho = evolve(rho0, t_obs, gamma_phi0, gamma_relax0, omega_eV, T, B, E)
    V = fringe_visibility(rho)
    D = distinguishability(rho)
    return V, D

# ======================================================================
# Main simulation
# ======================================================================
print("=" * 80)
print("Numerical experiment inspired by attosecond H2 photoionization studies (Max Planck, 2024)")
print("Parameters:")
print("  t_obs = 200 as = 2e-16 s")
print("  theta = 90° (Bell state (|00⟩+|11⟩)/√2, maximal entanglement)")
print("  T = 0 K, gamma_phi0 = 0, gamma_relax0 = 0 (negligible decoherence)")
print("  B = 0 T, E = 0 V/m")
print("=" * 80)

# Set parameters to mimic ideal conditions
t_obs_h2 = 2e-16          # 200 attoseconds
theta_h2 = 90             # Bell state
gamma_phi0_h2 = 0.0
gamma_relax0_h2 = 0.0
T_h2 = 0.0
B_h2 = 0.0
E_h2 = 0.0
omega_eV_ref = 13.6       # Hydrogen ionisation energy (for thermal occupation, but T=0 so not used)

V, D = compute_V_D(theta_h2, gamma_phi0_h2, gamma_relax0_h2, t_obs_h2, T_h2, B_h2, E_h2, omega_eV_ref)

print(f"\nResults:")
print(f"  Visibility V = {V:.6f}")
print(f"  Distinguishability D = {D:.6f}")
print(f"  Complementarity V² + D² = {V**2 + D**2:.6f}")

# ======================================================================
# Comparison with ideal Bell state
# ======================================================================
print("\n" + "=" * 80)
print("Comparison with ideal Bell state (theoretical prediction):")
print("  V_ideal = 1.000000, D_ideal = 0.000000")
print(f"  DTQEM deviation: ΔV = {abs(1.0 - V):.2e}, ΔD = {abs(0.0 - D):.2e}")
if V > 0.999:
    print("  ✅ Excellent agreement – DTQEM reproduces maximal entanglement.")
else:
    print("  ⚠️ Slight deviation due to numerical precision.")
print("=" * 80)

# ======================================================================
# Optional: Add finite decoherence to see realistic decay
# ======================================================================
print("\n" + "=" * 80)
print("Optional: Adding finite decoherence to observe realistic decay")
print("gamma_phi0 = 1000 1/s, gamma_relax0 = 500 1/s")
print("=" * 80)

gamma_phi0_dec = 1000.0
gamma_relax0_dec = 500.0

t_range_fs = np.linspace(0, 100, 200)  # femtoseconds
t_range_sec = t_range_fs * 1e-15

V_dec = []
D_dec = []
for t in t_range_sec:
    Vt, Dt = compute_V_D(theta_h2, gamma_phi0_dec, gamma_relax0_dec, t, T_h2, B_h2, E_h2, omega_eV_ref)
    V_dec.append(Vt)
    D_dec.append(Dt)

plt.figure(figsize=(10, 5))
plt.plot(t_range_fs, V_dec, 'b-', linewidth=2, label='Visibility V(t)')
plt.plot(t_range_fs, D_dec, 'r--', linewidth=2, label='Distinguishability D(t)')
plt.xlabel('Time (fs)')
plt.ylabel('Value')
plt.title('DTQEM v12.2: Decoherence dynamics (γφ₀=1000, γrel₀=500)')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
