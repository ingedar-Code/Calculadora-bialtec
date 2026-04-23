import json

def calcular_sintesis(dosis_ff_g_ton, em_kcal_kg):
    # Tabla de referencia: Dosis FF (g/Ton) vs Sintesis de Carne (g/kg alimento)
    datos_referencia = [
        (0, 0.0),
        (200, 17.1747236),
        (300, 20.9109792),
        (500, 23.8035642),
        (600, 24.5869727),
        (700, 25.0690702),
        (800, 26.2009513),
        (1000, 30.131094)
    ]
    
    # Interpolación lineal simple para la dosis
    sintesis_base = 0.0
    for i in range(len(datos_referencia) - 1):
        x0, y0 = datos_referencia[i]
        x1, y1 = datos_referencia[i+1]
        if x0 <= dosis_ff_g_ton <= x1:
            sintesis_base = y0 + (y1 - y0) * ((dosis_ff_g_ton - x0) / (x1 - x0))
            break
    else:
        # Si es mayor al máximo o menor al mínimo
        if dosis_ff_g_ton > datos_referencia[-1][0]:
            # Extrapolación plana o lineal simple, usaremos el máximo para este ejemplo
            # o una extrapolación lineal basada en el último segmento
            x0, y0 = datos_referencia[-2]
            x1, y1 = datos_referencia[-1]
            sintesis_base = y0 + (y1 - y0) * ((dosis_ff_g_ton - x0) / (x1 - x0))
        elif dosis_ff_g_ton < 0:
            sintesis_base = 0.0

    # Ajuste por energía (se asume un alimento estándar de 3000 kcal/kg como base, si no se especifica)
    # Este es un modelo sugerido, ajustando proporcionalmente la síntesis en función de la energía
    energia_base = 3000.0
    if em_kcal_kg > 0:
        factor_energia = em_kcal_kg / energia_base
    else:
        factor_energia = 1.0

    sintesis_final = sintesis_base * factor_energia

    return round(sintesis_final, 2)
