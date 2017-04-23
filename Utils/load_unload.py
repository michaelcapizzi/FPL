import pickle
import json


def pickle(obj, fn):
    """

    :param obj:
    :param fn:
    :return:
    """
    f_in = open(fn, "wb")
    pickle.dump(obj, f_in)
    f_in.close()


def unpickle(fn):
    """

    :param fn:
    :return:
    """
    f_in = open(fn, "rb")
    obj = pickle.load(f_in)
    f_in.close()
    return obj


def save_json(dict_, fn):
    """

    :param dict_:
    :param fn:
    :return:
    """
    with open(fn, "w") as f:
        f.write(json.dumps(dict_))


def load_json(fn):
    """

    :param fn:
    :return:
    """
    with open(fn, "r") as f:
        json_string = f.read()
    return json.load(json_string)