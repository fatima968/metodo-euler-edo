# Método de Euler vs. Solución Analítica (Separación de Variables)

Este proyecto implementa en Python el **Método de Euler** para aproximar la solución de una ecuación diferencial ordinaria (EDO) separable de primer orden y la compara con su solución exacta.

## 1. Planteamiento del Problema
Se resuelve el siguiente problema de valor inicial (crecimiento exponencial):

$$\frac{dy}{dt} = 2y, \quad y(0) = 1$$

* **Intervalo de evaluación:** $t \in [0, 1]$
* **Paso de tiempo:** $h = 0.2$

## 2. Solución Analítica (Separación de Variables)
1. Separamos las variables $y$ y $t$:
   $$\frac{1}{y}\,dy = 2\,dt$$
2. Integramos ambos lados:
   $$\int \frac{1}{y}\,dy = \int 2\,dt \implies \ln|y| = 2t + C$$
3. Despejamos $y(t)$:
   $$y(t) = A e^{2t}$$
4. Evaluamos la condición inicial $y(0) = 1$:
   $$1 = A e^{0} \implies A = 1$$

**Solución exacta:**
$$y(t) = e^{2t}$$

## 3. Resultados (Comparación en $t \in [0, 1]$ con $h = 0.2$)

| $t$ | Aproximación Euler $y(t)$ | Solución Exacta $y(t)$ | Error Absoluto |
| :--- | :---: | :---: | :---: |
| 0.0 | 1.0000 | 1.0000 | 0.0000 |
| 0.2 | 1.4000 | 1.4918 | 0.0918 |
| 0.4 | 1.9600 | 2.2255 | 0.2655 |
| 0.6 | 2.7440 | 3.3201 | 0.5761 |
| 0.8 | 3.8416 | 4.9530 | 1.1114 |
| 1.0 | 5.3782 | 7.3891 | 2.0108 |

## 4. Ejecución
```bash
python euler_separable.py
```