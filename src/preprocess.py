from sklearn.model_selection import train_test_split
import pandas as pd


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


train_df, test_df = split_test_data("../data/raw/winequality/winequality-white.csv")

X_train, y_train = train_df.drop(columns=["quality"]), train_df["quality"]
X_test, y_test = test_df.drop(columns=["quality"]), test_df["quality"]

X_train.to_csv ('../data/processed/X_train')
y_train.to_csv('../data/processed/y_train')
X_test.to_csv ('../data/processed/X_test')
y_test.to_csv('../data/processed/y_test')