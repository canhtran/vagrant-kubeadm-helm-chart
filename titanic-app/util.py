import os
import pickle


def read_model_from_pickle(path):
    if os.path.isfile(path):
        with open(path, 'rb') as handle:
            model = pickle.load(handle)
            return model
    else:
        return None


@contextmanager
def predict_model(model,  input):
    try:
        result = model.predict(input)
        yield result
    except Exception as ex
        yield None

