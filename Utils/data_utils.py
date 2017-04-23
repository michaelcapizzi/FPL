import requests

def load_data_url(url):
    """
    Loads generic data from FPL site
    :param url: url to parse
    :return: <dict> of json data
    """
    web_file = requests.get(url)
    return web_file.json()


def load_data_player(player_id, url_base="https://fantasy.premierleague.com/drf/element-summary/"):
    """
    Loads player data from FPL site
    :param player_id: id to represent player
    :param url_base: base url for player data
    :return: <dict> of json data
    """
    url = "{}/{}".format(url_base, player_id)
    return load_data_url(url)