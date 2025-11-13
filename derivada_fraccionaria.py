# ================================================================
# Archivo: derivadas_fraccionarias.py
# Descripción:
#   Cálculo y visualización de derivadas fraccionarias en Python
#   Incluye:
#     1. Teoría breve
#     2. Derivada simbólica (Riemann-Liouville con Sympy)
#     3. Derivadas numéricas (con 'fractional')
#     4. Ecuación diferencial fraccionaria (con 'fdeint')
# ================================================================

# ------------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# ------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Algunas librerías especializadas deben instalarse:
# pip install fractional fdeint
try:
    from fractional import fractional_diff
    import fdeint
except ImportError:
    print("⚠️ Algunas librerías no están instaladas. Ejecute en consola:")
    print("   pip install fractional fdeint")
    print("Luego vuelva a ejecutar este script.")
    exit()

# ------------------------------------------------
# 2. TEORÍA BREVE (salida informativa)
# ------------------------------------------------
print("=" * 60)
print("DERIVADAS FRACCIONARIAS EN PYTHON")
print("=" * 60)
print("""
La derivada fraccionaria de orden α generaliza el concepto de derivada entera.
Dos definiciones comunes son:

  - Riemann–Liouville:
      D^α f(x) = 1/Γ(n-α) * d^n/dx^n ∫₀ˣ f(t)/(x-t)^{α-n+1} dt

  - Caputo:
      ^C D^α f(x) = 1/Γ(n-α) ∫₀ˣ f⁽ⁿ⁾(t)/(x-t)^{α-n+1} dt

Ambas coinciden para funciones suaves y condiciones iniciales adecuadas.
""")

# ------------------------------------------------
# 3. DERIVADA FRACCIONARIA SIMBÓLICA
# ------------------------------------------------
print("=" * 60)
print("Cálculo simbólico con Sympy (Riemann–Liouville formal)")
print("=" * 60)

x, t = sp.symbols('x t', positive=True)
f = sp.sin(x)
alpha = sp.Rational(1, 2)

# Definición formal (Riemann–Liouville)
D_frac = (1/sp.gamma(1 - alpha)) * sp.integrate(sp.diff(f, x).subs(x, t) / (x - t)**alpha, (t, 0, x))

print("Derivada fraccionaria simbólica (orden 1/2) de sin(x):")
print(D_frac)
print()

# ------------------------------------------------
# 4. DERIVADAS FRACCIONARIAS NUMÉRICAS
# ------------------------------------------------
print("=" * 60)
print("Cálculo numérico y visualización con 'fractional'")
print("=" * 60)

x_vals = np.linspace(0, 10, 400)
f_vals = np.sin(x_vals)

orders = [0.5, 1.0, 2.0]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label='f(x) = sin(x)', linewidth=2)

for alpha in orders:
    f_frac = fractional_diff(f_vals, alpha)
    plt.plot(x_vals, f_frac, label=f'D^{alpha} f(x)')

plt.title("Derivadas fraccionarias de sin(x)")
plt.xlabel("x")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 5. ECUACIÓN DIFERENCIAL FRACCIONARIA
# ------------------------------------------------
print("=" * 60)
print("Resolviendo D^0.5 y = -y con fdeint")
print("=" * 60)

def f_rhs(t, y):
    """Ecuación diferencial: D^α y = -y"""
    return -y

alpha = 0.5
t = np.linspace(0, 10, 200)
y0 = 1

sol = fdeint.solve_fde(f_rhs, alpha, y0, t)

plt.figure(figsize=(8,5))
plt.plot(t, sol, label=r"Solución de $D^{0.5} y = -y$")
plt.title(r"Ecuación diferencial fraccionaria ($D^{0.5} y = -y$)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 6. FINALIZACIÓN
# ------------------------------------------------
print("=" * 60)
print("✅ Proceso completado con éxito.")
print("Se mostraron:")
print("  • Derivada simbólica formal (Riemann–Liouville)")
print("  • Derivadas numéricas (α = 0.5, 1, 2)")
print("  • Solución a la ecuación diferencial fraccionaria D^0.5 y = -y")
print("=" * 60)