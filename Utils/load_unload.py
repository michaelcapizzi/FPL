import pickle
import json


def pickle_data(obj, fn):
    """
    Pickles an object
    :param obj: <object> to pickle
    :param fn: path to save pickled object
    :return: None
    """
    f_in = open(fn, "wb")
    pickle.dump(obj, f_in)
    f_in.close()


def unpickle_data(fn):
    """
    Unpickles an object
    :param fn: path to pickled object
    :return: <object>
    """
    f_in = open(fn, "rb")
    obj = pickle.load(f_in)
    f_in.close()
    return obj


def save_json(dict_, fn):
    """
    Saves a <dict> to json
    :param dict_: <dict> to save
    :param fn: path to save json
    :return: None
    """
    with open(fn, "w") as f:
        f.write(json.dumps(dict_))


def load_json(fn):
    """
    Loads a <dict> from json
    :param fn: path to saved json
    :return: <dict>
    """
    with open(fn, "r") as f:
        json_string = f.read()
    return json.load(json_string)