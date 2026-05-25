# Análisis de Datos Climáticos Globales

## Integrantes
| Rol | Nombre |
|-----|--------|
| P1 – Líder (Hugo) | [Gaston Reynoso] |
| P2 – Desarrollador (Paco) | [Gaston Reynoso] |
| P3 – QA (Luis) | [Gaston Reynoso] |

## Escenario
Escenario A – Análisis de Datos Climáticos (UTN TUP 2026)

## Dataset
- **Fuente:** GISTEMP (NASA) vía DataHub.io
- **URL:** https://datahub.io/core/global-temp
- **Formato:** CSV con registros anuales de anomalía de temperatura global
- **Licencia:** Dominio público

## Estructura del Repositorio
analisis-climatico-tup/
├── datos/               # Dataset CSV de entrada
├── scripts/             # Script Python de análisis
├── resultados/          # Gráficos e indicadores exportados
├── README.md
└── .gitignore
## Cómo ejecutar el script
1. Clonar el repositorio
2. Abrir Google Colab y montar el entorno
3. Instalar dependencias: `pip install pandas matplotlib`
4. Ejecutar desde la carpeta /scripts: `python analisis_climatico.py`

## Resultados obtenidos
- Indicadores exportados en `resultados/indicadores_temperatura.csv`
- Gráfico de evolución en `resultados/grafico_temperatura.png`
