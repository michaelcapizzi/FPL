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
    return json.loads(json_string, object_hook=key_str2int)


def key_str2int(dict_):
    """
    Ensures that a key that *could* be an <int> is made one
    :param dict: <dict> to examine
    :return: new <dict>
    """
    return {int(k):(int(v) if isinstance(v, str) else v) for k,v in dict_.items()}
