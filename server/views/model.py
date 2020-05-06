import pickle

from sklearn.pipeline import Pipeline

from server import config


def load() -> Pipeline:
    with open(config.CONFIG['model_path'], 'rb') as model_file:
        return pickle.load(model_file)  # type: Pipeline
