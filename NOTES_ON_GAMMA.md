# Note on the dephasing rate convention

In DTQEM v12.2, the parameter `gamma_phi0` used in the GUI and in `jump_operators` is such that the physical dephasing rate is `gamma_phi0 / 2` (when T=0). Consequently, the analytical condition for V = D becomes:

\[
\gamma_{\phi0}\,t_{\text{obs}} = 2\ln(\tan\theta).
\]

If one prefers a convention where `gamma_phi0` directly equals the physical rate, the right‑hand side would be `\ln(\tan\theta)`. Both conventions are internally consistent; the code uses the former.
