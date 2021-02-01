import pandas as pd

col_feat_1 = 'feat-1'
col_feat_2 = 'feat-2'


def load_file(filename):
    col_names = [col_feat_1, col_feat_2]
    data = pd.read_csv("./ressources/" + filename, names=col_names)
    return data.to_numpy()
