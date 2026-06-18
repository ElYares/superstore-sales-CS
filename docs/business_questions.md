# Business Questions

Este documento define las preguntas de negocio que guían el análisis del proyecto **Global Superstore Sales & Profitability Analytics**.

---

## 1. Executive Overview

### BQ01: ¿Cuál es el desempeño general del negocio?

Métricas relacionadas:

- Total sales.
- Total profit.
- Profit margin.
- Total orders.
- Total customers.
- Average order value.
- Average profit per order.

Objetivo:

Entender el estado general del negocio y establecer una línea base de desempeño.

---

### BQ02: ¿El negocio es rentable?

Métricas relacionadas:

- Total profit.
- Profit margin.
- Loss rows.
- Loss row rate.
- Loss orders.
- Loss order rate.

Objetivo:

Determinar si el negocio genera utilidad global y qué proporción de ventas u órdenes generan pérdida.

---

## 2. Sales Analysis

### BQ03: ¿Cómo evolucionan las ventas en el tiempo?

Dimensiones relacionadas:

- Order year.
- Order quarter.
- Order month.
- Order month name.

Métricas relacionadas:

- Sales.
- Orders.
- Quantity.

Objetivo:

Identificar crecimiento, estacionalidad, meses fuertes y periodos débiles.

---

### BQ04: ¿Qué mercados generan más ventas?

Dimensiones relacionadas:

- Market.
- Market group.
- Region.
- Country.

Métricas relacionadas:

- Sales.
- Orders.
- Customers.

Objetivo:

Identificar los mercados y regiones con mayor volumen comercial.

---

### BQ05: ¿Qué categorías y subcategorías venden más?

Dimensiones relacionadas:

- Category.
- Sub-category.
- Product name.

Métricas relacionadas:

- Sales.
- Quantity.
- Orders.

Objetivo:

Detectar las líneas de producto que impulsan el volumen de ventas.

---

## 3. Profitability Analysis

### BQ06: ¿Qué mercados generan más utilidad?

Dimensiones relacionadas:

- Market.
- Market group.
- Region.
- Country.

Métricas relacionadas:

- Profit.
- Profit margin.
- Loss orders.
- Loss order rate.

Objetivo:

Comparar volumen de ventas contra rentabilidad real.

---

### BQ07: ¿Qué categorías y subcategorías son más rentables?

Dimensiones relacionadas:

- Category.
- Sub-category.
- Product name.

Métricas relacionadas:

- Profit.
- Profit margin.
- Sales.
- Quantity.

Objetivo:

Identificar productos y categorías que generan valor, no solo volumen.

---

### BQ08: ¿Qué productos generan pérdidas?

Dimensiones relacionadas:

- Product name.
- Category.
- Sub-category.
- Market.
- Region.

Métricas relacionadas:

- Profit.
- Sales.
- Profit margin.
- Discount.
- Shipping cost.

Objetivo:

Detectar productos que deberían revisarse por pricing, descuentos, costos o estrategia comercial.

---

## 4. Discount Analysis

### BQ09: ¿Cómo afectan los descuentos a la utilidad?

Dimensiones relacionadas:

- Discount.
- Discount level.
- Category.
- Sub-category.
- Market.
- Segment.

Métricas relacionadas:

- Sales.
- Profit.
- Profit margin.
- Quantity.
- Loss rate.

Objetivo:

Entender si los descuentos están impulsando ventas rentables o destruyendo margen.

---

### BQ10: ¿Qué niveles de descuento generan mayor pérdida?

Dimensiones relacionadas:

- Discount level.
- Category.
- Sub-category.
- Market.

Métricas relacionadas:

- Profit.
- Profit margin.
- Loss rows.
- Loss row rate.
- Loss orders.
- Loss order rate.

Objetivo:

Detectar si existe un punto donde el descuento deja de ser comercialmente conveniente.

---

## 5. Customer Segment Analysis

### BQ11: ¿Qué segmento de cliente es más rentable?

Dimensiones relacionadas:

- Segment.

Métricas relacionadas:

- Sales.
- Profit.
- Profit margin.
- Orders.
- Customers.
- Average order value.

Objetivo:

Comparar Consumer, Corporate y Home Office desde ventas y rentabilidad.

---

### BQ12: ¿Qué segmentos tienen mayor riesgo de pérdida?

Dimensiones relacionadas:

- Segment.
- Market.
- Category.

Métricas relacionadas:

- Loss orders.
- Loss order rate.
- Average discount.
- Shipping cost.

Objetivo:

Identificar segmentos donde el negocio vende, pero no necesariamente gana.

---

## 6. Logistics Analysis

### BQ13: ¿Qué impacto tiene el costo de envío sobre la rentabilidad?

Dimensiones relacionadas:

- Shipping cost.
- Ship mode.
- Order priority.
- Market.
- Region.

Métricas relacionadas:

- Shipping cost ratio.
- Profit margin.
- Profit.
- Sales.

Objetivo:

Determinar si los costos logísticos están reduciendo el margen del negocio.

---

### BQ14: ¿Qué modos de envío son más costosos?

Dimensiones relacionadas:

- Ship mode.
- Order priority.
- Market.
- Region.

Métricas relacionadas:

- Shipping cost.
- Average shipping cost.
- Shipping days.
- Profit.

Objetivo:

Comparar los modos de envío para detectar oportunidades de optimización logística.

---

### BQ15: ¿El tiempo de envío afecta la rentabilidad?

Dimensiones relacionadas:

- Shipping days.
- Ship mode.
- Order priority.
- Market.

Métricas relacionadas:

- Profit.
- Profit margin.
- Shipping cost.
- Sales.

Objetivo:

Analizar si entregas más rápidas o más lentas tienen relación con margen y costos.

---

## 7. Final Business Recommendations

### BQ16: ¿Qué acciones debería priorizar el negocio?

Áreas relacionadas:

- Mercados no rentables.
- Productos con pérdida.
- Categorías con bajo margen.
- Descuentos agresivos.
- Costos logísticos elevados.
- Segmentos poco rentables.

Objetivo:

Convertir el análisis en recomendaciones accionables para mejorar rentabilidad.
