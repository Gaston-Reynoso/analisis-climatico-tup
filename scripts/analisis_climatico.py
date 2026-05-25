# analisis_climatico.py
# Script de análisis de datos climáticos globales (GISTEMP)
# Tecnicatura Universitaria en Programación — UTN
# Cátedra: Organización Empresarial — 2026

import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Carga de datos ---
df = pd.read_csv("../datos/dataset_climatico.csv")
df_gistemp = df[df["Source"] == "GISTEMP"].copy()

# --- Indicadores estadísticos ---
# Calculamos anomalías de temperatura respecto a la media histórica 1951-1980
temp_promedio = df_gistemp["Mean"].mean()
temp_maxima = df_gistemp["Mean"].max()
temp_minima = df_gistemp["Mean"].min()

print(f"Temperatura promedio (anomalía): {temp_promedio:.4f} °C")
print(f"Temperatura máxima registrada:   {temp_maxima:.4f} °C")
print(f"Temperatura mínima registrada:   {temp_minima:.4f} °C")

# Exportar indicadores
os.makedirs("../resultados", exist_ok=True)
resumen = pd.DataFrame({
    "Indicador": ["Promedio", "Máximo", "Mínimo"],
    "Valor (°C)": [temp_promedio, temp_maxima, temp_minima]
})
resumen.to_csv("../resultados/indicadores_temperatura.csv", index=False)

# --- Gráfico de evolución temporal ---
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df_gistemp["Year"], df_gistemp["Mean"], color="tomato", linewidth=1.5, label="Anomalía GISTEMP")
ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)
ax.set_title("Evolución de la Anomalía de Temperatura Global (GISTEMP)", fontsize=14)
ax.set_xlabel("Año")
ax.set_ylabel("Anomalía de Temperatura (°C)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("../resultados/grafico_temperatura.png", dpi=150)
print("Gráfico exportado.")
