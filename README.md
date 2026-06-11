# Global Superstore Sales & Profitability Analytics

Proyecto de análisis de datos enfocado en ventas, rentabilidad, descuentos, logística y comportamiento comercial usando el dataset **Global Superstore**.

El objetivo es construir un proyecto modular, limpio y profesional que permita analizar el desempeño comercial de una superstore global, identificar oportunidades de mejora y generar insights accionables para negocio.

---

## Objetivo del proyecto

Analizar datos históricos de ventas para responder preguntas clave de negocio relacionadas con:

- Ventas globales.
- Rentabilidad.
- Descuentos.
- Productos con pérdidas.
- Segmentos de clientes.
- Categorías y subcategorías.
- Mercados y regiones.
- Costos de envío.
- Desempeño temporal.

---

## Preguntas de negocio

Este proyecto busca responder:

1. ¿Cuál es la evolución de ventas y profit en el tiempo?
2. ¿Qué mercados y regiones generan más ventas?
3. ¿Qué mercados y regiones generan más utilidad?
4. ¿Qué categorías venden más?
5. ¿Qué categorías son más rentables?
6. ¿Qué subcategorías generan pérdidas?
7. ¿Qué productos venden mucho pero dejan poco profit?
8. ¿Cómo afecta el descuento a la rentabilidad?
9. ¿Qué segmento de cliente es más rentable?
10. ¿Qué modo de envío tiene mayor impacto en costos?
11. ¿Qué mercados tienen alto volumen pero bajo margen?
12. ¿Qué recomendaciones de negocio se pueden generar?

---

## Dataset

El dataset utilizado es `superstore.csv`.

Debe colocarse en:

```bash
data/raw/superstore.csv
```

Columnas principales esperadas:

```text
Order.Date
Ship.Date
Ship.Mode
Customer.ID
Customer.Name
Segment
Country
City
State
Region
Market
Category
Sub.Category
Product.Name
Sales
Quantity
Discount
Profit
Shipping.Cost
Order.Priority
```

---

## Estructura del proyecto

```bash
.
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 00_data_review.ipynb
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_sales.ipynb
│   ├── 03_profitability_analysis.ipynb
│   ├── 04_discount_analysis.ipynb
│   └── 05_logistics_analysis.ipynb
│
├── src/
│   └── superstore/
│       ├── __init__.py
│       ├── config.py
│       ├── constants.py
│       │
│       ├── data/
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   ├── validator.py
│       │   └── cleaner.py
│       │
│       ├── features/
│       │   ├── __init__.py
│       │   └── build_features.py
│       │
│       ├── analytics/
│       │   ├── __init__.py
│       │   ├── kpis.py
│       │   ├── sales.py
│       │   ├── profitability.py
│       │   ├── discounts.py
│       │   ├── logistics.py
│       │   └── segmentation.py
│       │
│       ├── visualization/
│       │   ├── __init__.py
│       │   ├── charts.py
│       │   └── themes.py
│       │
│       └── utils/
│           ├── __init__.py
│           ├── paths.py
│           └── logging.py
│
├── dashboard/
│   ├── app.py
│   ├── pages/
│   │   ├── 01_overview.py
│   │   ├── 02_sales.py
│   │   ├── 03_profitability.py
│   │   ├── 04_discounts.py
│   │   └── 05_logistics.py
│   └── components/
│       ├── filters.py
│       ├── metrics.py
│       └── plots.py
│
├── reports/
│   ├── insights.md
│   ├── executive_summary.md
│   └── figures/
│
├── tests/
│   ├── test_loader.py
│   ├── test_cleaner.py
│   ├── test_features.py
│   └── test_kpis.py
│
├── scripts/
│   ├── run_cleaning.py
│   ├── generate_report.py
│   └── run_dashboard.sh
│
├── config/
│   ├── settings.yaml
│   └── logging.yaml
│
├── docs/
│   ├── data_dictionary.md
│   ├── business_questions.md
│   └── methodology.md
│
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Arquitectura

El proyecto sigue una arquitectura modular basada en separación de responsabilidades.

### `data/`

Contiene los datos del proyecto.

- `raw/`: datos originales sin modificar.
- `interim/`: datos temporales o transformaciones parciales.
- `processed/`: datos limpios listos para análisis.
- `external/`: datos externos adicionales, si se usan.

### `notebooks/`

Contiene notebooks exploratorios y análisis narrativos.

Los notebooks deben consumir funciones desde `src/` y no contener toda la lógica del proyecto.

### `src/superstore/`

Contiene el código principal reutilizable del proyecto.

### `dashboard/`

Contiene la aplicación visual del proyecto, preferentemente construida con Streamlit.

### `reports/`

Contiene reportes, insights y resumen ejecutivo.

### `tests/`

Contiene pruebas automatizadas para validar funciones principales.

### `scripts/`

Contiene scripts ejecutables para correr procesos del proyecto.

### `config/`

Contiene archivos de configuración.

### `docs/`

Contiene documentación técnica y de negocio.

---

## Principios de clean code

Este proyecto busca seguir estos principios:

- Separar lógica de negocio, limpieza, análisis y visualización.
- Evitar notebooks gigantes con código repetido.
- Crear funciones pequeñas y reutilizables.
- Usar nombres claros para variables, funciones y módulos.
- Mantener una estructura consistente.
- Documentar decisiones importantes.
- Validar datos antes de analizarlos.
- Automatizar pasos repetitivos.
- Escribir pruebas para funciones críticas.

---

## Flujo de trabajo recomendado

### 1. Colocar dataset original

```bash
cp superstore.csv data/raw/superstore.csv
```

### 2. Revisar datos iniciales

Notebook sugerido:

```bash
notebooks/00_data_review.ipynb
```

Objetivo:

- Revisar columnas.
- Revisar tipos de datos.
- Revisar valores nulos.
- Revisar duplicados.
- Revisar rango de fechas.
- Revisar métricas generales.

### 3. Limpiar datos

Notebook sugerido:

```bash
notebooks/01_data_cleaning.ipynb
```

O script:

```bash
python scripts/run_cleaning.py
```

Salida esperada:

```bash
data/processed/superstore_clean.csv
```

### 4. Ejecutar análisis exploratorio

Notebook sugerido:

```bash
notebooks/02_eda_sales.ipynb
```

### 5. Analizar rentabilidad

Notebook sugerido:

```bash
notebooks/03_profitability_analysis.ipynb
```

### 6. Analizar descuentos

Notebook sugerido:

```bash
notebooks/04_discount_analysis.ipynb
```

### 7. Analizar logística

Notebook sugerido:

```bash
notebooks/05_logistics_analysis.ipynb
```

### 8. Crear dashboard

```bash
streamlit run dashboard/app.py
```

O usando el script:

```bash
./scripts/run_dashboard.sh
```

---

## Instalación

### 1. Crear entorno virtual

```bash
python -m venv .venv
```

### 2. Activar entorno virtual

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Dependencias principales

El proyecto puede usar:

```text
pandas
numpy
matplotlib
seaborn
plotly
streamlit
pyyaml
pytest
jupyter
ipykernel
```

Dependencias opcionales:

```text
scikit-learn
sqlalchemy
python-dotenv
```

---

## Stack recomendado

Stack base:

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
Plotly
Jupyter Notebook
Streamlit
```

Stack profesional opcional:

```text
PostgreSQL
Docker
Metabase
Power BI
Airflow
dbt
MLflow
```

---

## Convención de nombres

Las columnas originales pueden venir con puntos o espacios, por ejemplo:

```text
Order.Date
Ship.Date
Customer.ID
Product.Name
Sub.Category
Shipping.Cost
```

Durante la limpieza deben normalizarse a formato `snake_case`:

```text
order_date
ship_date
customer_id
product_name
sub_category
shipping_cost
```

---

## KPIs principales

El proyecto debe calcular:

- Total sales.
- Total profit.
- Profit margin.
- Total orders.
- Total customers.
- Average order value.
- Average discount.
- Total quantity sold.
- Total shipping cost.
- Loss-making orders.
- Loss-making products.
- Profit by region.
- Profit by market.
- Profit by category.
- Profit by segment.

---

## Métricas sugeridas

### Sales

```text
total_sales = sum(sales)
average_sales = mean(sales)
median_sales = median(sales)
```

### Profit

```text
total_profit = sum(profit)
average_profit = mean(profit)
profit_margin = total_profit / total_sales
```

### Discount

```text
average_discount = mean(discount)
max_discount = max(discount)
```

### Logistics

```text
total_shipping_cost = sum(shipping_cost)
average_shipping_cost = mean(shipping_cost)
shipping_cost_ratio = total_shipping_cost / total_sales
```

---

## Módulos principales

### `src/superstore/data/loader.py`

Responsable de cargar datos.

Funciones esperadas:

```python
load_raw_data()
load_processed_data()
```

### `src/superstore/data/validator.py`

Responsable de validar estructura y calidad de datos.

Funciones esperadas:

```python
validate_required_columns()
validate_missing_values()
validate_duplicate_rows()
```

### `src/superstore/data/cleaner.py`

Responsable de limpiar y normalizar datos.

Funciones esperadas:

```python
clean_column_names()
parse_dates()
remove_unused_columns()
clean_superstore_data()
```

### `src/superstore/features/build_features.py`

Responsable de crear nuevas variables.

Features sugeridas:

```text
order_year
order_month
order_quarter
shipping_days
profit_margin
is_loss
discount_level
```

### `src/superstore/analytics/kpis.py`

Responsable de calcular KPIs generales.

### `src/superstore/analytics/sales.py`

Responsable de análisis de ventas.

### `src/superstore/analytics/profitability.py`

Responsable de análisis de rentabilidad.

### `src/superstore/analytics/discounts.py`

Responsable de análisis de descuentos.

### `src/superstore/analytics/logistics.py`

Responsable de análisis logístico.

### `src/superstore/analytics/segmentation.py`

Responsable de análisis por segmento de cliente.

---

## Entregables

Este proyecto debe producir:

1. Dataset limpio en `data/processed/`.
2. Notebooks de análisis en `notebooks/`.
3. Dashboard interactivo en `dashboard/`.
4. Reporte de insights en `reports/insights.md`.
5. Resumen ejecutivo en `reports/executive_summary.md`.
6. Documentación de columnas en `docs/data_dictionary.md`.
7. Preguntas de negocio en `docs/business_questions.md`.

---

## Reporte de insights

Cada insight debe seguir esta estructura:

```md
## Insight

### Hallazgo

Descripción clara del hallazgo.

### Evidencia

Métrica, tabla o gráfica que respalda el hallazgo.

### Impacto

Por qué importa para negocio.

### Recomendación

Acción sugerida.
```

Ejemplo:

```md
## Tables vende mucho, pero destruye utilidad

### Hallazgo

La subcategoría Tables genera un volumen importante de ventas, pero presenta profit acumulado negativo.

### Evidencia

Tables aparece entre las subcategorías con ventas altas, pero su profit total es negativo.

### Impacto

La empresa puede estar generando ingresos en esta subcategoría, pero perdiendo dinero por descuentos, costos o estrategia de precios.

### Recomendación

Revisar política de descuentos, costos logísticos y margen comercial de la subcategoría Tables.
```

---

## Dashboard

El dashboard debe incluir al menos estas secciones:

### Overview

- Total sales.
- Total profit.
- Profit margin.
- Total orders.
- Total customers.
- Average discount.

### Sales

- Ventas por año.
- Ventas por mes.
- Ventas por mercado.
- Ventas por región.
- Ventas por categoría.

### Profitability

- Profit por mercado.
- Profit por región.
- Profit por categoría.
- Profit por subcategoría.
- Productos con mayor pérdida.
- Productos más rentables.

### Discounts

- Discount vs profit.
- Discount promedio por categoría.
- Discount promedio por mercado.
- Órdenes con alto descuento y profit negativo.

### Logistics

- Shipping cost por mercado.
- Shipping cost por ship mode.
- Shipping days promedio.
- Relación entre shipping cost y profit.

---

## Roadmap

### Fase 1: Setup

- Crear estructura del proyecto.
- Crear entorno virtual.
- Instalar dependencias.
- Agregar dataset original.

### Fase 2: Data review

- Revisar columnas.
- Revisar tipos de datos.
- Revisar calidad del dataset.

### Fase 3: Data cleaning

- Normalizar columnas.
- Convertir fechas.
- Eliminar columnas innecesarias.
- Crear dataset limpio.

### Fase 4: Feature engineering

- Crear variables temporales.
- Crear margen de profit.
- Crear flag de pérdida.
- Crear nivel de descuento.
- Crear días de envío.

### Fase 5: Analytics

- Calcular KPIs.
- Analizar ventas.
- Analizar rentabilidad.
- Analizar descuentos.
- Analizar logística.
- Analizar segmentos.

### Fase 6: Dashboard

- Crear dashboard en Streamlit.
- Agregar filtros.
- Agregar KPIs.
- Agregar visualizaciones.

### Fase 7: Reporting

- Crear reporte de insights.
- Crear resumen ejecutivo.
- Documentar recomendaciones.

---

## Cómo ejecutar el proyecto

### Ejecutar limpieza

```bash
python scripts/run_cleaning.py
```

### Ejecutar dashboard

```bash
streamlit run dashboard/app.py
```

O:

```bash
./scripts/run_dashboard.sh
```

### Ejecutar tests

```bash
pytest
```

---

## Estado del proyecto

Estado actual:

```text
En desarrollo
```

---

## Autor

Proyecto desarrollado por:

```text
Arturo Yared Elizondo Regino
```

