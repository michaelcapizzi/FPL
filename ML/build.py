import numpy as np

columns_ignore = [
    "Unnamed: 0",
    "gw_id",
    "total_points"
]

def build_X_y(df, columns_to_exclude=[]):
    """
    Builds an X matrix for `sklearn` usage
    :param df: <dataframe> of data
    :param columns_to_exclude: <list> of additional columns to exclude
    :return: X matrix
    """
    # build y
    y = np.array(df["total_points"])
    # get non string columns
    df = df.select_dtypes(exclude=["object"])
    # remove more columns
    columns_to_exclude += columns_ignore
    all_columns = set(df.columns)
    columns_to_use = all_columns.difference(set(columns_to_exclude))
    df = df[list(columns_to_use)].astype(float)
    df = df.fillna(0.0)
    # build X
    X = np.array(df)
    print(X.shape)
    print(y.shape)
    return X, y