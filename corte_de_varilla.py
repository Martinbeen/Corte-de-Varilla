def corte_de_varilla_Dp(precios, longitud_total):

    ganancias = [0] * (longitud_total + 1)
    cortes = [0] * (longitud_total + 1)

    for longitud in range(1, longitud_total + 1):
        mejor_valor = float('-inf')
        for corte in range(1, longitud + 1):
            valor = precios[corte - 1] + ganancias[longitud - corte]
            if valor > mejor_valor:
                mejor_valor = valor
                cortes[longitud] = corte
        ganancias[longitud] = mejor_valor

    partes = []
    restante = longitud_total
    while restante > 0:
        partes.append(cortes[restante])
        restante -= cortes[restante]

    return ganancias[longitud_total], partes

precios = [2, 3, 7, 10, 12, 14, 16, 18, 20, 25, 30, 35, 36, 37, 40, 41]
longitud = 16
ganancia, cortes = corte_de_varilla_Dp(precios, longitud)

print("Algoritmo de Programacion Dinamica")
print(f"La ganancia maxima es: {ganancia}")
print("Los cortes optimos son:", cortes)

def corte_de_varilla_Fb(precios, longitud_total):

    if longitud_total == 0:
        return 0

    mejor_valor = float('-inf')

    for corte in range(1, longitud_total + 1):
        valor = precios[corte - 1] + corte_de_varilla_Fb(precios, longitud_total - corte)
        if valor > mejor_valor:
            mejor_valor = valor

    return mejor_valor

precios = [2, 3, 7, 10, 12, 14, 16, 18, 20, 25, 30, 35, 36, 37, 40, 41]
longitud = 16
ganancia = corte_de_varilla_Fb(precios, longitud)

print("Algoritmo de Fuerza Bruta")
print(f"La ganancia maxima obtenida para una varilla de longitud {longitud} es: {ganancia}")