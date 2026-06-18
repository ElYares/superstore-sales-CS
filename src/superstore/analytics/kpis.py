from __future__ import annotations

import pandas as pd


def calculate_total_sales(df: pd.DataFrame) -> float:
    """
    Calculate total sales.
    """
    return float(df["sales"].sum())


def calculate_total_profit(df: pd.DataFrame) -> float:
    """
    Calculate total profit.
    """
    return float(df["profit"].sum())


def calculate_profit_margin(df: pd.DataFrame) -> float:
    """
    Calculate global profit margin.
    """
    total_sales = calculate_total_sales(df)

    if total_sales == 0:
        return 0.0

    return calculate_total_profit(df) / total_sales


def calculate_total_orders(df: pd.DataFrame) -> int:
    """
    Calculate total unique orders.
    """
    return int(df["order_id"].nunique())


def calculate_total_customers(df: pd.DataFrame) -> int:
    """
    Calculate total unique customers.
    """
    return int(df["customer_id"].nunique())


def calculate_average_order_value(df: pd.DataFrame) -> float:
    """
    Calculate average order value.
    """
    total_orders = calculate_total_orders(df)

    if total_orders == 0:
        return 0.0

    return calculate_total_sales(df) / total_orders


def calculate_average_discount(df: pd.DataFrame) -> float:
    """
    Calculate average discount.
    """
    return float(df["discount"].mean())


def calculate_total_quantity(df: pd.DataFrame) -> int:
    """
    Calculate total quantity sold.
    """
    return int(df["quantity"].sum())


def calculate_total_shipping_cost(df: pd.DataFrame) -> float:
    """
    Calculate total shipping cost.
    """
    return float(df["shipping_cost"].sum())


def calculate_loss_rows(df: pd.DataFrame) -> int:
    """
    Calculate number of rows with negative profit.
    """
    return int((df["profit"] < 0).sum())


def calculate_loss_row_rate(df: pd.DataFrame) -> float:
    """
    Calculate percentage of rows with negative profit.
    """
    total_rows = len(df)

    if total_rows == 0:
        return 0.0

    return calculate_loss_rows(df) / total_rows

def calculate_loss_rows(df: pd.DataFrame) -> int:
    """
    Calculate number of rows with negative profit.
    """
    return int((df["profit"] < 0).sum())


def calculate_loss_row_rate(df: pd.DataFrame) -> float:
    """
    Calculate percentage of rows with negative profit.
    """
    total_rows = len(df)

    if total_rows == 0:
        return 0.0

    return calculate_loss_rows(df) / total_rows


def calculate_loss_orders(df: pd.DataFrame) -> int:
    """
    Calculate number of unique orders with total negative profit.
    """
    order_profit = df.groupby("order_id")["profit"].sum()

    return int((order_profit < 0).sum())


def calculate_loss_order_rate(df: pd.DataFrame) -> float:
    """
    Calculate percentage of unique orders with total negative profit.
    """
    total_orders = calculate_total_orders(df)

    if total_orders == 0:
        return 0.0

    return calculate_loss_orders(df) / total_orders


def calculate_average_shipping_cost(df: pd.DataFrame) -> float:
    """
    Calculate average shipping cost per row.
    """
    return float(df["shipping_cost"].mean())


def calculate_shipping_cost_ratio(df: pd.DataFrame) -> float:
    """
    Calculate shipping cost as a percentage of total sales.
    """
    total_sales = calculate_total_sales(df)

    if total_sales == 0:
        return 0.0

    return calculate_total_shipping_cost(df) / total_sales


def calculate_average_profit_per_order(df: pd.DataFrame) -> float:
    """
    Calculate average profit per unique order.
    """
    total_orders = calculate_total_orders(df)

    if total_orders == 0:
        return 0.0

    return calculate_total_profit(df) / total_orders


def calculate_main_kpis(df: pd.DataFrame) -> dict[str, float | int]:
    """
    Calculate main business KPIs.
    """
    return {
        "total_sales": calculate_total_sales(df),
        "total_profit": calculate_total_profit(df),
        "profit_margin": calculate_profit_margin(df),
        "total_orders": calculate_total_orders(df),
        "total_customers": calculate_total_customers(df),
        "average_order_value": calculate_average_order_value(df),
        "average_profit_per_order": calculate_average_profit_per_order(df),
        "average_discount": calculate_average_discount(df),
        "total_quantity": calculate_total_quantity(df),
        "total_shipping_cost": calculate_total_shipping_cost(df),
        "average_shipping_cost": calculate_average_shipping_cost(df),
        "shipping_cost_ratio": calculate_shipping_cost_ratio(df),
        "loss_rows": calculate_loss_rows(df),
        "loss_row_rate": calculate_loss_row_rate(df),
        "loss_orders": calculate_loss_orders(df),
        "loss_order_rate": calculate_loss_order_rate(df),
    }
