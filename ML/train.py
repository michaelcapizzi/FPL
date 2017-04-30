from sklearn import *

def experiment(X, y, clf, cv_folds=100, random_state=1978):
    """

    :param X:
    :param y:
    :param clf:
    :param cv_folds:    If `None`, then train all
                        If "all", then LOO
    :param random_state:
    :return:
    """
    # make CV folds
    folds = model_selection.KFold(cv_folds, random_state=random_state)
    # run CV train/predict
    results = model_selection.cross_val_predict(clf, X, y, cv=folds)
    return results