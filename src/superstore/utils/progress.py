# src/superstore/utils/progress.py

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterable, Iterator, TypeVar

from tqdm import tqdm


T = TypeVar("T")


DEFAULT_PROGRESS_CONFIG = {
    "unit": "step",
    "ncols": 100,
    "leave": True,
    "dynamic_ncols": True,
}


def track_iterable(
    iterable: Iterable[T],
    description: str = "Processing",
    unit: str = "item",
    total: int | None = None,
    leave: bool = True,
    disable: bool = False,
) -> Iterator[T]:
    """
    Wrap any iterable with a tqdm progress bar.

    Useful for loops over columns, files, records or tasks.

    Example
    -------
    for column in track_iterable(columns, description="Cleaning columns"):
        ...
    """
    yield from tqdm(
        iterable,
        desc=description,
        unit=unit,
        total=total,
        leave=leave,
        dynamic_ncols=True,
        disable=disable,
    )


@contextmanager
def progress_bar(
    total: int,
    description: str = "Processing",
    unit: str = "step",
    leave: bool = True,
    disable: bool = False,
):
    """
    Create a manual tqdm progress bar.

    Useful when you want to manually call progress.update().

    Example
    -------
    with progress_bar(total=3, description="Pipeline") as progress:
        step_1()
        progress.update(1)

        step_2()
        progress.update(1)

        step_3()
        progress.update(1)
    """
    progress = tqdm(
        total=total,
        desc=description,
        unit=unit,
        leave=leave,
        dynamic_ncols=True,
        disable=disable,
    )

    try:
        yield progress
    finally:
        progress.close()


def progress_steps(
    steps: list[tuple[str, callable]],
    description: str = "Running pipeline",
    leave: bool = True,
    disable: bool = False,
) -> list:
    """
    Execute a list of named steps with a global progress bar.

    Each step must be a tuple:

        ("Step name", function)

    The function must not require arguments.

    Returns
    -------
    list
        Results returned by each step function.

    Example
    -------
    results = progress_steps([
        ("Load data", load_data),
        ("Clean data", clean_data),
        ("Save data", save_data),
    ])
    """
    results = []

    with progress_bar(
        total=len(steps),
        description=description,
        unit="step",
        leave=leave,
        disable=disable,
    ) as progress:
        for step_name, step_function in steps:
            progress.set_postfix_str(step_name)
            result = step_function()
            results.append(result)
            progress.update(1)

    return results


def update_progress_description(progress, description: str) -> None:
    """
    Update progress bar description safely.
    """
    if progress is not None:
        progress.set_description(description)


def update_progress_status(progress, status: str) -> None:
    """
    Update progress bar status safely.
    """
    if progress is not None:
        progress.set_postfix_str(status)
