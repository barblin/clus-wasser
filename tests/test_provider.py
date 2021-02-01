import pandas as pd

col_feat_1 = 'feat-1'
col_feat_2 = 'feat-2'
col_labels = 'labels'


def load_file_features(filename):
    data = pd.read_csv("./ressources/" + filename, usecols=[1, 2], header=None)
    return data.to_numpy()


def load_file_labels(filename):
    data = pd.read_csv("./ressources/" + filename, usecols=[3], header=None)
    return data.to_numpy()
