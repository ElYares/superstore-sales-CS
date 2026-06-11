from __future__ import annotations

from pathlib import Path

import pandas as pd

from superstore.constants import (
    DATE_COLUMNS,
    PROCESSED_DATA_FILENAME,
    RAW_DATA_FILENAME,
)
from superstore.utils.paths import PROCESSED_DATA_DIR, RAW_DATA_DIR


def load_csv(
    path: Path,
    date_columns: list[str] | None = None,
) -> pd.DataFrame:
    """
    Load a CSV file from a given path.

    Parameters
    ----------
    path:
        Path to the CSV file.
    date_columns:
        Optional list of columns to parse as datetime.

    Returns
    -------
    pd.DataFrame
        Loaded dataframe.
    """
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)

    if date_columns:
        for column in date_columns:
            if column in df.columns:
                df[column] = pd.to_datetime(df[column], errors="coerce")

    return df


def load_raw_data(filename: str = RAW_DATA_FILENAME) -> pd.DataFrame:
    """
    Load raw Superstore dataset.
    """
    path = RAW_DATA_DIR / filename
    return load_csv(path)


def load_processed_data(
    filename: str = PROCESSED_DATA_FILENAME,
) -> pd.DataFrame:
    """
    Load processed Superstore dataset.
    """
    path = PROCESSED_DATA_DIR / filename
    return load_csv(path, date_columns=DATE_COLUMNS)


def save_processed_data(
    df: pd.DataFrame,
    filename: str = PROCESSED_DATA_FILENAME,
) -> Path:
    """
    Save dataframe into the processed data directory.
    """
    output_path = PROCESSED_DATA_DIR / filename
    df.to_csv(output_path, index=False)
    return output_path
