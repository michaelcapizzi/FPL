import pandas as pd
import numpy as np

def build_X(df, columns_to_exclude=[]):
    """

    :param df:
    :param columns_to_exclude:
    :return:
    """
    # remove columns if required
    if columns_to_exclude:
        all_columns = set(df.columns)
        columns_to_use = all_columns.difference(set(columns_to_exclude))
        df = df[list(columns_to_use)]
    # build array
    # X = np.array(df)
    # print(X)