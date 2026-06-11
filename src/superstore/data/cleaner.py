from __future__ import annotations

import pandas as pd

from superstore.constants import COLUMN_RENAME_MAP, UNUSED_COLUMNS
from superstore.utils.progress import track_iterable


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename raw dataset columns to snake_case.
    """
    return df.rename(columns=COLUMN_RENAME_MAP)


def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop columns that are not required for analysis.
    """
    columns_to_drop = [
        column for column in UNUSED_COLUMNS if column in df.columns
    ]
    
    return df.drop(columns=columns_to_drop)


def parse_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert date columns to datetime.
    """
    date_columns = ["order_date", "ship_date"]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    return df


def normalize_text_columns(
    df: pd.DataFrame,
    show_progress: bool = True
) -> pd.DataFrame:
    """
    Strip text columns and normalize extra spaces.
    """
    from superstore.utils.progress import track_iterable

    text_columns = df.select_dtypes(include=["object"]).columns
    
    for column in track_iterable(
        text_columns,
        description = "Normalizing text columns",
        unit = "column",
        disable=not show_progress,
    ):
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
            .str.replace(r"\s+"," ", regex=True)
        )
    return df

def clean_superstore_data(
    df: pd.DataFrame,
    show_progress: bool = True,
) -> pd.DataFrame:
    """
    Apply full cleaning pipeline to Superstore dataset.
    """

    cleaned_df = df.copy()

    cleaned_df = drop_unused_columns(cleaned_df)
    cleaned_df = rename_columns(cleaned_df)
    cleaned_df =  parse_date_columns(cleaned_df)
    cleaned_df =  normalize_text_columns(
        cleaned_df,
        show_progress = show_progress,
    )

    return cleaned_df
