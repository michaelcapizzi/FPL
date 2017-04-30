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
    return ["gw_id", "player_id", "last_name", "first_name", "team", "team_code"] + list(player_dict["history"][0].keys())


def update_player_dataframe(existing_df, gw_dict, player_id, i2p_lookup, p2t_lookup, ti2t_lookup):
    """
    Updates values in players dataframe
    :param existing_df: Existing copy of players dataframe
    :param gw_dict: Single <dict> representing a player's single GW data
    :param player_id: id for player whose gw_dict it is
    :param i2p_lookup: index -> player
    :param p2t_lookup: player -> team
    :param ti2t_lookup: team_id -> team
    :return: <dataframe>
    """
    gw_id = gw_dict["id"]
    if ((existing_df["id"] == gw_id) & (existing_df["player_id"] == player_id)).any():
        print("data for player id {}, gw {} already present".format(
            player_id, gw_id
            )
        )
        return existing_df
    else:
        # add columns
        last, first = i2p_lookup[player_id]
        team = p2t_lookup[player_id]
        gw_dict["gw_id"] = gw_id
        gw_dict["player_id"] = player_id
        gw_dict["last_name"] = last
        gw_dict["first_name"] = first
        gw_dict["team"] = ti2t_lookup[team]
        gw_dict["team_code"] = team
        return existing_df.append(
            gw_dict,
            ignore_index=True
        )




