import pandas as pd
from pathlib import Path


def generate_df_by_time_section(time_section="original", save_path=None):
    """
    This function returns the dataframe or energy usage
    with all the values grouped by the time section wanted
    (hour, day, week, month, year).

    Parameters
    ----------
    - time_section: str = "original"

        What time section the original DataFrame should be
        grouped by. If "original", returns the original unprocessed
        DataFrame.
        Possible values:
            "original",
            "hour",
            "day",
            "week",
            "month",
            "year"

    - save_path : str | pathlib.Path | None = None

        Add a path to a csv file if you want to save the
        DataFrame.

    Returns
    -------
    - df_result: pd.DataFrame

        The DataFrame resulting from the groupby.
    """

    url = 'https://drive.google.com/file/d/14rWJ6OKc_aZbAcb6h220vQP0xfitLgHM/view?usp=sharing'
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    df_original = pd.read_csv(path, sep=";")
    return df_original

    if time_section == "original":
        pass


if __name__ == "__main__":
    pass