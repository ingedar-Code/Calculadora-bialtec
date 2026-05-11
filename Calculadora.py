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

def calcular_leche(dosis_ff_g_dia,
                   relacion_forraje_pct=70.0,
                   dms_base_conc_pct=70.0,
                   dms_base_forraje_pct=70.0,
                   dmi_kg_dia=22.0,
                   eb_conc_mcal_kg=4.4,
                   eb_forraje_mcal_kg=4.4,
                   ed_em_factor=0.82,
                   em_en_factor=0.64,
                   eff_metabolica_pct=0.65,
                   en_por_kg_leche_mcal=0.80,
                   densidad_leche=1.03):
    """
    Modelo mecanístico in silico para aumento de leche.
    """
    # Tabla de calibración: (dosis, mejora_dms_conc, mejora_dms_forraje)
    calibracion = [
        (0.0, 0.0, 0.0),
        (1.5, 0.0200, 0.0150),
        (2.5, 0.0193, 0.0250),
        (5.0, 0.0400, 0.0500),
        (5.6, 0.0450, 0.0600)
    ]
    
    # Interpolación de mejoras de digestibilidad (DMS)
    imp_c = 0.0
    imp_f = 0.0
    if dosis_ff_g_dia <= 0:
        imp_c, imp_f = 0.0, 0.0
    elif dosis_ff_g_dia >= 5.6:
        # Extrapolación suave basada en los últimos dos puntos
        x0, y0_c, y0_f = calibracion[-2]
        x1, y1_c, y1_f = calibracion[-1]
        slope_c = (y1_c - y0_c) / (x1 - x0)
        slope_f = (y1_f - y0_f) / (x1 - x0)
        imp_c = y1_c + slope_c * (dosis_ff_g_dia - x1)
        imp_f = y1_f + slope_f * (dosis_ff_g_dia - x1)
    else:
        for i in range(len(calibracion) - 1):
            x0, y0_c, y0_f = calibracion[i]
            x1, y1_c, y1_f = calibracion[i+1]
            if x0 <= dosis_ff_g_dia <= x1:
                t = (dosis_ff_g_dia - x0) / (x1 - x0)
                imp_c = y0_c + t * (y1_c - y0_c)
                imp_f = y0_f + t * (y1_f - y0_f)
                break
                
    # Asegurar que no sea negativo
    imp_c = max(0.0, imp_c)
    imp_f = max(0.0, imp_f)
    
    f_ratio = relacion_forraje_pct / 100.0
    base_c = dms_base_conc_pct / 100.0
    base_f = dms_base_forraje_pct / 100.0
    
    # Nuevas digestibilidades (con tope en 98%)
    deg_c = min(0.98, base_c + imp_c)
    deg_f = min(0.98, base_f + imp_f)
    
    # Energía Digestible (ED)
    ed0 = eb_conc_mcal_kg * (1 - f_ratio) * base_c + eb_forraje_mcal_kg * f_ratio * base_f
    ed1 = eb_conc_mcal_kg * (1 - f_ratio) * deg_c + eb_forraje_mcal_kg * f_ratio * deg_f
    
    # Energía Metabolizable (EM)
    em0 = ed0 * ed_em_factor
    em1 = ed1 * ed_em_factor
    
    # Energía Neta lactancia (ENl)
    nel0 = em0 * em_en_factor
    nel1 = em1 * em_en_factor
    
    # EN diaria disponible
    nel_day0 = nel0 * dmi_kg_dia
    nel_day1 = nel1 * dmi_kg_dia
    
    # Ajuste metabólico
    adj0 = nel_day0 * eff_metabolica_pct
    adj1 = nel_day1 * eff_metabolica_pct
    
    delta_adj = adj1 - adj0
    
    # Producción de leche
    kg_leche_adicional = delta_adj / en_por_kg_leche_mcal if en_por_kg_leche_mcal > 0 else 0
    litros_leche_adicional = kg_leche_adicional / densidad_leche if densidad_leche > 0 else 0
    
    return round(litros_leche_adicional, 2)
