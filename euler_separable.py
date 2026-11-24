import math


# 1. Definición de la EDO: dy/dt = f(t, y) = 2y
def f(t, y):
  return 2 * y


# 2. Solución analítica exacta por separación de variables: y(t) = e^(2t)
def solucion_exacta(t):
  return math.exp(2 * t)


# 3. Implementación del Método de Euler
def metodo_euler(f, t0, y0, t_final, h):
  t = t0
  y = y0

  resultados = []
  y_ex = solucion_exacta(t)
  resultados.append((t, y, y_ex, abs(y_ex - y)))

  while round(t, 5) < t_final:
    y = y + h * f(t, y)
    t = round(t + h, 5)
    y_ex = solucion_exacta(t)
    error = abs(y_ex - y)
    resultados.append((t, y, y_ex, error))

  return resultados


if __name__ == "__main__":
  t0 = 0.0
  y0 = 1.0
  t_final = 1.0
  h = 0.2

  tabla = metodo_euler(f, t0, y0, t_final, h)

  print(f"{'t':<6} | {'Euler y(t)':<12} | {'Exacta y(t)':<12} | {'Error Abs.':<12}")
  print("-" * 50)
  for t, y_euler, y_exacta, err in tabla:
    print(f"{t:<6.1f} | {y_euler:<12.4f} | {y_exacta:<12.4f} | {err:<12.4f}"):<12.4f} | {err:<12.4f}")