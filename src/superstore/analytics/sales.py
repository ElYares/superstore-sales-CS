from __future__ import annotations

import pandas as pd


def sales_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales, profit, orders and yearly growth rates.
    """
    yearly_sales = (
        df.groupby("order_year", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .sort_values("order_year")
    )

    yearly_sales["sales_growth_rate"] = yearly_sales["total_sales"].pct_change()
    yearly_sales["profit_growth_rate"] = yearly_sales["total_profit"].pct_change()
    yearly_sales["orders_growth_rate"] = yearly_sales["total_orders"].pct_change()

    return yearly_sales


def sales_by_quarter(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales, profit and orders by year and quarter.
    """
    return (
        df.groupby(["order_year", "order_quarter"], as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .sort_values(["order_year", "order_quarter"])
    )


def sales_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales, profit and orders by year and month.
    """
    monthly_sales = (
        df.groupby(
            ["order_year", "order_month", "order_month_name"],
            as_index=False,
        )
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .sort_values(["order_year", "order_month"])
    )

    monthly_sales["period"] = (
        monthly_sales["order_year"].astype(str)
        + "-"
        + monthly_sales["order_month"].astype(str).str.zfill(2)
    )

    monthly_sales["sales_growth_rate"] = monthly_sales["total_sales"].pct_change()
    monthly_sales["profit_growth_rate"] = monthly_sales["total_profit"].pct_change()

    return monthly_sales


def sales_by_market(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales performance by market.
    """
    return (
        df.groupby("market", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_customers=("customer_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .assign(
            profit_margin=lambda data: data["total_profit"] / data["total_sales"],
            average_order_value=lambda data: data["total_sales"] / data["total_orders"],
        )
        .sort_values("total_sales", ascending=False)
    )


def sales_by_market_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales performance by market group.
    """
    return (
        df.groupby("market_group", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_customers=("customer_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .assign(
            profit_margin=lambda data: data["total_profit"] / data["total_sales"],
            average_order_value=lambda data: data["total_sales"] / data["total_orders"],
        )
        .sort_values("total_sales", ascending=False)
    )


def sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales performance by region.
    """
    return (
        df.groupby("region", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_customers=("customer_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .assign(
            profit_margin=lambda data: data["total_profit"] / data["total_sales"],
            average_order_value=lambda data: data["total_sales"] / data["total_orders"],
        )
        .sort_values("total_sales", ascending=False)
    )


def sales_by_country(df: pd.DataFrame, top_n: int = 20) -> pd.DataFrame:
    """
    Calculate sales performance by country.

    Parameters
    ----------
    df:
        Processed Superstore dataframe.
    top_n:
        Number of countries to return ordered by sales.
    """
    return (
        df.groupby("country", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_customers=("customer_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .assign(
            profit_margin=lambda data: data["total_profit"] / data["total_sales"],
            average_order_value=lambda data: data["total_sales"] / data["total_orders"],
        )
        .sort_values("total_sales", ascending=False)
        .head(top_n)
    )


def sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales performance by product category.
    """
    return (
        df.groupby("category", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_quantity=("quantity", "sum"),
            total_products=("product_id", "nunique"),
        )
        .assign(
            profit_margin=lambda data: data["total_profit"] / data["total_sales"],
            average_order_value=lambda data: data["total_sales"] / data["total_orders"],
        )
        .sort_values("total_sales", ascending=False)
    )


def sales_by_sub_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales performance by product sub-category.
    """
    return (
        df.groupby("sub_category", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_quantity=("quantity", "sum"),
            total_products=("product_id", "nunique"),
        )
        .assign(
            profit_margin=lambda data: data["total_profit"] / data["total_sales"],
            average_order_value=lambda data: data["total_sales"] / data["total_orders"],
        )
        .sort_values("total_sales", ascending=False)
    )


def sales_by_segment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sales performance by customer segment.
    """
    return (
        df.groupby("segment", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_customers=("customer_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .assign(
            profit_margin=lambda data: data["total_profit"] / data["total_sales"],
            average_order_value=lambda data: data["total_sales"] / data["total_orders"],
        )
        .sort_values("total_sales", ascending=False)
    )


def top_products_by_sales(
    df: pd.DataFrame,
    top_n: int = 10,
) -> pd.DataFrame:
    """
    Return top products by total sales.
    """
    return (
        df.groupby(
            ["product_id", "product_name", "category", "sub_category"],
            as_index=False,
        )
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_orders=("order_id", "nunique"),
            total_quantity=("quantity", "sum"),
        )
        .assign(
            profit_margin=lambda data: data["total_profit"] / data["total_sales"],
        )
        .sort_values("total_sales", ascending=False)
        .head(top_n)
    )


def sales_summary(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """
    Generate a dictionary with the main sales analysis tables.
    """
    return {
        "sales_by_year": sales_by_year(df),
        "sales_by_quarter": sales_by_quarter(df),
        "sales_by_month": sales_by_month(df),
        "sales_by_market": sales_by_market(df),
        "sales_by_market_group": sales_by_market_group(df),
        "sales_by_region": sales_by_region(df),
        "sales_by_category": sales_by_category(df),
        "sales_by_sub_category": sales_by_sub_category(df),
        "sales_by_segment": sales_by_segment(df),
        "top_products_by_sales": top_products_by_sales(df),
    }
