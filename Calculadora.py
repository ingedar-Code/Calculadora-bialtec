def calcular_sintesis(dosis_ff_g_ton, em_kcal_kg):
    """
    Modelo mecanístico in silico de Bialtec
    """
    # Si el usuario no ingresa energía, usamos la base del modelo (2007.44 kcal/kg)
    if em_kcal_kg <= 0:
        em_kcal_kg = 2007.44
        
    # Tabla de referencia: Dosis FF vs Mejora relativa en degradabilidad (%)
    dosis_list = [0, 200, 300, 500, 600, 700, 800, 1000]
    delta_list = [0.00, 2.85, 3.47, 3.95, 4.08, 4.16, 4.23, 4.30]
    
    # 1. Interpolación lineal para obtener el delta relativo (%)
    delta_rel_pct = 0.0
    for i in range(len(dosis_list) - 1):
        x0, y0 = dosis_list[i], delta_list[i]
        x1, y1 = dosis_list[i+1], delta_list[i+1]
        if x0 <= dosis_ff_g_ton <= x1:
            delta_rel_pct = y0 + (y1 - y0) * ((dosis_ff_g_ton - x0) / (x1 - x0))
            break
    else:
        # Extrapolación si la dosis es mayor a 1000
        if dosis_ff_g_ton > dosis_list[-1]:
            x0, y0 = dosis_list[-2], delta_list[-2]
            x1, y1 = dosis_list[-1], delta_list[-1]
            delta_rel_pct = y0 + (y1 - y0) * ((dosis_ff_g_ton - x0) / (x1 - x0))
        elif dosis_ff_g_ton < 0:
            delta_rel_pct = 0.0
            
    delta_rel = delta_rel_pct / 100.0
    
    # 2. Energía Metabolizable (EM) liberada
    # em_liberada = em_base * delta_relativa
    em_liberada = em_kcal_kg * delta_rel
    
    # 3. Conversión a Energía Neta (EN) adicional
    EN_EM_RATIO = 0.742980688
    en_adicional = em_liberada * EN_EM_RATIO
    
    # 4. Síntesis de Proteína + Grasa
    K_PG_CALIBRADO = 8.24999996  # kcal requeridas por gramo de P+G
    sintesis_pg_g = en_adicional / K_PG_CALIBRADO
    
    # 5. Síntesis de Carne total
    FRACCION_PG_EN_CARNE = 0.30  # La carne es ~30% proteína y grasa (el resto es agua/ceniza)
    sintesis_carne = sintesis_pg_g / FRACCION_PG_EN_CARNE
    
    return round(sintesis_carne, 2)
