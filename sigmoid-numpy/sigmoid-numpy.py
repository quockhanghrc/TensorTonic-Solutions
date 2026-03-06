import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    Works with scalars, lists, or NumPy arrays.
    """
    x = np.array(x)
    return 1 / (1 + np.exp(-x))