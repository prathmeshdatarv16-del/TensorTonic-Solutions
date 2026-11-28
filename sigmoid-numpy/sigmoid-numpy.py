import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    arr=np.asarray(x, dtype=float)
    result=np.exp(-arr)+1
    result=1/result
    if(result.ndim == 0):
        return float(result)
    return result
    pass