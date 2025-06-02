import math
import matplotlib.pyplot as plt

def calcular_fuerza_electrica(q1_mc, q2_mc, x2, y2):
    constante_electrica = 9*(10**9)
    delta_x = x2
    delta_y = y2
    r = math.sqrt(delta_x**2 + delta_y**2)
    r_x = delta_x / r
    r_y = delta_y / r
    q1 = q1_mc * (10**-6)
    q2 = q2_mc * (10**-6)
    magnitud_fuerza = constante_electrica * abs(q1) * abs(q2) / (r ** 2)
    signo = 1 if q1 * q2 > 0 else -1
    fuerza_x = signo * magnitud_fuerza * r_x
    fuerza_y = signo * magnitud_fuerza * r_y
    print(f"Fuerza sobre Q2 en ({x2}, {y2}):")
    print(f"Componente X: {fuerza_x:.2e} N")
    print(f"Componente Y: {fuerza_y:.2e} N")
    print(f"Magnitud total de la fuerza: {magnitud_fuerza:.2e} N")
    return fuerza_x, fuerza_y, magnitud_fuerza

def graficar(x2, y2, fx, fy, magnitud):
    plt.figure(figsize=(8, 8))
    plt.scatter(0, 0, color='blue', label='Q1 (origen)')
    plt.text(0.2, 0.2, 'Q1', fontsize=12, color='blue')
    plt.scatter(x2, y2, color='green', label='Q2 (variable)')
    plt.text(x2 + 0.2, y2 + 0.2, 'Q2', fontsize=12, color='green')
    factor_visual = 5000  
    fx_vis = fx * factor_visual
    fy_vis = fy * factor_visual
    plt.quiver(x2, y2, fx_vis, fy_vis, angles='xy', scale_units='xy', scale=1, color='red', label='Fuerza sobre Q2')
    rango_x = max(abs(x2), abs(x2 + fx_vis)) + 2
    rango_y = max(abs(y2), abs(y2 + fy_vis)) + 2
    plt.xlim(-rango_x, rango_x)
    plt.ylim(-rango_y, rango_y)
    plt.title(f'Fuerza eléctrica entre dos cargas\nF = {magnitud:.2e} N')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.grid(True)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

print("Cálculo de la Fuerza Eléctrica entre dos cargas puntuales, puede utilizar valores enteros")
q1_mc = int(input("Ingrese la carga Q1 (μC): "))
q2_mc = int(input("Ingrese la carga Q2 (μC): "))
x2 = int(input("Ingrese la coordenada X de Q2: "))
y2 = int(input("Ingrese la coordenada Y de Q2: "))
fx, fy, mag = calcular_fuerza_electrica(q1_mc, q2_mc, x2, y2)
graficar(x2, y2, fx, fy, mag)
