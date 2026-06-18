import pandas as pd

from superstore.constants import REQUIRED_COLUMNS


def validate_required_columns(
    df: pd.DataFrame,
    required_columns: list[str] | None = None,
) -> None:
    """
    Validate that the dataframe contains all required columns.
    """
    required_columns = required_columns or REQUIRED_COLUMNS

    missing_columns = [
        column for column in required_columns if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )


def validate_not_empty(df: pd.DataFrame) -> None:
    """
    Validate that the dataframe is not empty.
    """
    if df.empty:
        raise ValueError("Dataset is empty.")


def validate_duplicate_rows(df: pd.DataFrame) -> int:
    """
    Return number of duplicated rows.
    """
    return int(df.duplicated().sum())


def validate_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Return missing values count by column.
    """
    return df.isna().sum().sort_values(ascending=False)


def validate_numeric_columns(df: pd.DataFrame, columns: list[str]) -> None:
    """
    Validate that selected columns are numeric.
    """
    invalid_columns = [
        column for column in columns
        if column in df.columns and not pd.api.types.is_numeric_dtype(df[column])
    ]

    if invalid_columns:
        raise TypeError(
            "Columns must be numeric: "
            + ", ".join(invalid_columns)
        )
