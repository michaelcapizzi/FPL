import numpy as np

['Unnamed: 0', 'gw_id', 'player_id', 'last_name', 'first_name', 'team',
 'team_code', 'id', 'kickoff_time', 'kickoff_time_formatted',
 'team_h_score', 'team_a_score', 'was_home', 'round', 'total_points',
 'value', 'transfers_balance', 'selected', 'transfers_in',
 'transfers_out', 'loaned_in', 'loaned_out', 'minutes', 'goals_scored',
 'assists', 'clean_sheets', 'goals_conceded', 'own_goals',
 'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards',
 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat',
 'ict_index', 'ea_index', 'open_play_crosses', 'big_chances_created',
 'clearances_blocks_interceptions', 'recoveries', 'key_passes',
 'tackles', 'winning_goals', 'attempted_passes', 'completed_passes',
 'penalties_conceded', 'big_chances_missed', 'errors_leading_to_goal',
 'errors_leading_to_goal_attempt', 'tackled', 'offside', 'target_missed',
 'fouls', 'dribbles', 'element', 'fixture', 'opponent_team']

columns_ignore_gw_predict_no_history = [
    "Unnamed: 0",
    "gw_id",
    "team_h_score",
    "team_a_score",
    "round",
    "total_points",
    "goals_scored",
    "assists",
    "clean_sheets",
    "goals_conceded",
    "own_goals",
    "penalties_saved",
    "penalties_missed",
    "yellow_cards",
    "red_cards",
    "saves",
    "bonus",
    "bps",
    "winning_goals",
    "penalties_conceded",
    "errors_leading_to_goal",
    "errors_leading_to_goal_attempt"
]

columns_ignore_gw_predict_with_history = [
    "Unnamed: 0",
    "gw_id",
]

def build_X_y(df, columns_to_exclude, label_column):
    """
    Builds an X matrix for `sklearn` usage
    :param df: <dataframe> of data
    :param columns_to_exclude: <list> of columns to exclude
    :param label_column: name of column from df to use as target
    :return: X matrix
    """
    # build y
    y = np.array(df[label_column])
    # ensure that label_column in columns_to_exclude
    columns_to_exclude.append(label_column)
    # get non string columns
    df = df.select_dtypes(exclude=["object"])
    all_columns = set(df.columns)
    columns_to_use = all_columns.difference(set(columns_to_exclude))
    df = df[list(columns_to_use)].astype(float)
    df = df.fillna(0.0)
    # build X
    X = np.array(df)
    print(X.shape)
    print(y.shape)
    return X, y