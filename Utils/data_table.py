import pandas as pd


def initialize_player_dataframe(columns):
    """
    Initializes the player dataframe
    :param columns: which keys to add
    :return: Empty <dataframe>
    """
    return pd.DataFrame(columns=columns)


def get_player_keys(player_dict):
    """
    Extracts the keys (columns) for the player dataframe
    :param player_dict: Any player <dict>
    :return: <list> of keys
    """
    return list(player_dict["history"][0].keys())


def update_player_dataframe(existing_df, gw_dict):
    """
    Updates values in players dataframe
    :param existing_df: Existing copy of players dataframe
    :param gw_dict: Single <dict> representing a player's single GW data
    :return: <dataframe>
    """
    return existing_df.append(
        gw_dict,
        ignore_index=True
    )


