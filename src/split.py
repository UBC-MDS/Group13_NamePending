"""This script splits the raw data into 4 csv's.
Usage: split.py <input_path> <output_location>

Options:
<input_path>         input path
<output_location>     output location

Example: python src/split.py data/raw/winequality/winequality-white.csv data/processed

"""

from sklearn.model_selection import train_test_split
import pandas as pd
from docopt import docopt
from pathlib import Path

opt = docopt(__doc__)


def split_test_data(path: str):
    """
    Reads in the data from a csv file and splits into a train and test set.

    Parameters
    ----------
    path : string
        The path to the csv file

    Returns
    -------
    train_df, test_df :
        The train and test datasets
    """
    data = pd.read_csv(path, sep=";")
    train_df, test_df = train_test_split(data, random_state=522, test_size=0.2)
    return train_df, test_df


def main():

    input_path = opt['<input_path>']
    output_location = opt['<output_location>']
    output_path = Path(output_location)
    output_path.mkdir(parents=True, exist_ok=True)


    train_df, test_df = split_test_data(input_path)

    X_train, y_train = train_df.drop(columns=["quality"]), train_df["quality"]
    X_test, y_test = test_df.drop(columns=["quality"]), test_df["quality"]

    X_train.to_csv(f"{output_location}/X_train.csv", index=False)
    y_train.to_csv(f"{output_location}/y_train.csv", index=False)
    X_test.to_csv(f"{output_location}/X_test.csv", index=False)
    y_test.to_csv(f"{output_location}/y_test.csv", index=False)


if __name__ == "__main__":
    main()
