# Parámetros iniciales
potencia_inicial = 55  # Potencia inicial de la antena en miliwatts
repeticiones = 10  # Número de repeticiones
porcentajes = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]  # Lista de porcentajes

# Lista para almacenar los resultados
potencias = []

# Potencia inicial para la primera iteración
potencia_actual = potencia_inicial

# Iterar sobre el rango de repeticiones y calcular la potencia para cada porcentaje
for i in range(repeticiones):
    # Agregar el resultado actual
    potencias.append((i + 1, potencia_actual, porcentajes[i]))

    # Actualizar la potencia para la siguiente iteración
    if i < repeticiones - 1:
        potencia_actual *= porcentajes[i + 1] / 100

# Mostrar resultados
print("Repetición | Potencia (mW) | Porcentaje (%)")
for repeticion, potencia, porcentaje in potencias:
    print(f"     {repeticion}       |    {potencia:.2f} mW   |   {porcentaje}%")
