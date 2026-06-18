import numpy as np
import pandas as pd


def add_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add temporal features from order_date.
    """
    if "order_date" not in df.columns:
        return df

    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.month
    df["order_month_name"] = df["order_date"].dt.month_name()
    df["order_quarter"] = df["order_date"].dt.quarter
    df["order_weekday"] = df["order_date"].dt.day_name()

    return df


def add_shipping_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add shipping duration features.
    """
    if "order_date" not in df.columns or "ship_date" not in df.columns:
        return df

    df["shipping_days"] = (
        df["ship_date"] - df["order_date"]
    ).dt.days

    return df


def add_profitability_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add profitability related features.
    """
    if "profit" in df.columns and "sales" in df.columns:
        df["profit_margin"] = np.where(
            df["sales"] != 0,
            df["profit"] / df["sales"],
            0,
        )

    if "profit" in df.columns:
        df["is_loss"] = df["profit"] < 0

    return df


def add_discount_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add discount segmentation features.
    """
    if "discount" not in df.columns:
        return df

    df["discount_level"] = pd.cut(
        df["discount"],
        bins=[-0.01, 0, 0.1, 0.3, 0.6, 1.0],
        labels=[
            "no_discount",
            "low_discount",
            "medium_discount",
            "high_discount",
            "extreme_discount",
        ],
    )

    return df


def build_features(
    df: pd.DataFrame,
    show_progress: bool = True,
) -> pd.DataFrame:
    """
    Apply full feature engineering pipeline.
    """
    from superstore.utils.progress import progress_bar

    featured_df = df.copy()

    with progress_bar(
        total=4,
        description="Building features",
        unit="step",
        disable=not show_progress,
    ) as progress:
        featured_df = add_temporal_features(featured_df)
        progress.set_postfix_str("Temporal features")
        progress.update(1)

        featured_df = add_shipping_features(featured_df)
        progress.set_postfix_str("Shipping features")
        progress.update(1)

        featured_df = add_profitability_features(featured_df)
        progress.set_postfix_str("Profitability features")
        progress.update(1)

        featured_df = add_discount_features(featured_df)
        progress.set_postfix_str("Discount features")
        progress.update(1)

    return featured_df
