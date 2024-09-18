# ejercicio 1

productos = ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Teclado']
ventas = [120, 150, 200, 80, 170]
precios = [1000, 500, 700, 150, 50]


ventas_totales = []
for i in range(len(productos)):
    total = ventas[i] * precios[i]
    ventas_totales.append(total)


print("Producto | Ventas | Precio | Ventas Totales")
for i in range(len(productos)):
    print(f"{productos[i]:9} | {ventas[i]:6} | {precios[i]:6} | {ventas_totales[i]:13}")


total_ventas = sum(ventas_totales)
max_ventas = max(ventas_totales)
min_ventas = min(ventas_totales)
promedio_ventas = total_ventas / len(ventas_totales)

print("\nEstadísticas de Ventas Totales:")
print(f"Total de ventas: {total_ventas}")
print(f"Máximas ventas: {max_ventas}")
print(f"Mínimas ventas: {min_ventas}")
print(f"Promedio de ventas: {promedio_ventas}")
