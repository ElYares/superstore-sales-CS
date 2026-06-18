# scripts/run_cleaning.py

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

sys.path.append(str(SRC_DIR))

from superstore.data.cleaner import clean_superstore_data
from superstore.data.loader import load_raw_data, save_processed_data
from superstore.data.validator import (
    validate_duplicate_rows,
    validate_missing_values,
    validate_not_empty,
    validate_required_columns,
)
from superstore.features.build_features import build_features
from superstore.utils.paths import ensure_project_dirs
from superstore.utils.progress import progress_bar


def main() -> None:
    """
    Run complete data cleaning pipeline.
    """
    ensure_project_dirs()

    with progress_bar(
        total=6,
        description="Running data pipeline",
        unit="step",
    ) as progress:
        progress.set_postfix_str("Loading raw dataset")
        raw_df = load_raw_data()
        progress.update(1)

        progress.set_postfix_str("Validating dataset")
        validate_not_empty(raw_df)
        validate_required_columns(raw_df)
        progress.update(1)

        progress.set_postfix_str("Checking data quality")
        duplicate_count = validate_duplicate_rows(raw_df)
        missing_values = validate_missing_values(raw_df)
        progress.update(1)

        progress.set_postfix_str("Cleaning dataset")
        clean_df = clean_superstore_data(
            raw_df,
            show_progress=False,
        )
        progress.update(1)

        progress.set_postfix_str("Building features")
        final_df = build_features(
            clean_df,
            show_progress=False,
        )
        progress.update(1)

        progress.set_postfix_str("Saving processed dataset")
        output_path = save_processed_data(final_df)
        progress.update(1)

    print("\nData quality summary")
    print("--------------------")
    print(f"Rows: {len(raw_df):,}")
    print(f"Columns: {len(raw_df.columns):,}")
    print(f"Duplicated rows: {duplicate_count:,}")

    missing_values = missing_values[missing_values > 0]

    if missing_values.empty:
        print("Missing values: none")
    else:
        print("\nMissing values:")
        print(missing_values)

    print("\nOutput")
    print("------")
    print(f"Processed dataset saved at: {output_path}")
    print(f"Final rows: {len(final_df):,}")
    print(f"Final columns: {len(final_df.columns):,}")


if __name__ == "__main__":
    main()
