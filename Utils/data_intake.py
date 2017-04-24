import requests
from collections import OrderedDict


def load_data_url(url):
    """
    Loads generic data from FPL site
    :param url: url to parse
    :return: <dict> of json data
    """
    web_file = requests.get(url)
    return web_file.json()


def load_data_summary(url="https://fantasy.premierleague.com/drf/bootstrap-static"):
    """
    Loads summary data from FPL site
    :param url: url housing summary data
    :return: <dict> of json data
    """
    return load_data_url(url)


def build_player_lookups(data_summary_json):
    """
    Builds lookup dicts for player->id and id->player
    :param data_summary_json: output of load_summary_data()
    :return: <tuple> (p2i, i2p)
    """
    p2i_lookup = {}
    i2p_lookup = OrderedDict()
    # build
    for player_dict in data_summary_json["elements"]:
        id = player_dict["id"]
        first = player_dict["first_name"].encode("utf-8", "replace").decode("utf-8")
        second = player_dict["second_name"].encode("utf-8", "replace").decode("utf-8")
        p2i_lookup[(second, first)] = id
        i2p_lookup[id] = (second, first)
    # sort p2i
    p2i_sorted = OrderedDict(sorted(p2i_lookup.items()))
    return p2i_sorted, i2p_lookup


def build_player2team_lookup(summary_dataframe):
    p2t = OrderedDict()
    for player in summary_dataframe["elements"]:
        p2t[player["id"]] = player["team_code"]
    return p2t


# TODO build
def build_team_id2team_lookup():
    pass


def load_data_player(player_id, url_base="https://fantasy.premierleague.com/drf/element-summary/"):
    """
    Loads player data from FPL site
    :param player_id: id to represent player
    :param url_base: base url for player data
    :return: <dict> of json data
    """
    url = "{}/{}".format(url_base, player_id)
    return load_data_url(url)


def load_data_all_players(max_player_id,
                          url_base="https://fantasy.premierleague.com/drf/element-summary/"):
    """
    Loads player data for *all* players
    :param max_player_id: highest id in player data
    :param url_base: base url for player data
    :return: <dict> of <dict> of json data
    """
    all_players = OrderedDict()
    for i in range(1, max_player_id + 1):
        player_data = load_data_player(i, url_base)
        all_players[i] = player_data
    return all_players


