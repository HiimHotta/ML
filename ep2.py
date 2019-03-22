# all imports
import numpy as np
import time
from util.util import get_housing_prices_data, r_squared
from util.plots import plot_points_regression 

//%matplotlib inline

X, y = get_housing_prices_data(N=100)

plot_points_regression(X,
                       y,
                       title='Real estate prices prediction',
                       xlabel="m\u00b2",
                       ylabel='$')

def normal_equation_weights(X, y):
    """
    Calculates the weights of a linear function using the normal equation method.
    You should add into X a new column with 1s.

    :param X: design matrix
    :type X: np.ndarray(shape=(N, d))
    :param y: regression targets
    :type y: np.ndarray(shape=(N, 1))
    :return: weight vector
    :rtype: np.ndarray(shape=(d+1, 1))
    """
    
    # START OF YOUR CODE:
    raise NotImplementedError("Falta implementar normal_equation_weights()")
    # END YOUR CODE

    return w

# teste da função normal_equation_weights()

w = 0  # isto é desnecessário
w = normal_equation_weights(X, y)
print("Estimated w = ", w)

def normal_equation_prediction(X, w):
    """
    Calculates the prediction over a set of observations X using the linear function
    characterized by the weight vector w.
    You should add into X a new column with 1s.

    :param X: design matrix
    :type X: np.ndarray(shape=(N, d))
    :param w: weight vector
    :type w: np.ndarray(shape=(d+1, 1))
    :param y: regression prediction
    :type y: np.ndarray(shape=(N, 1))
    """
    
    # START OF YOUR CODE:
    raise NotImplementedError("Falta implementar normal_equation_prediction()")
    # END YOUR CODE
    
    return prediction

# teste da função normal_equation_prediction()
prediction = normal_equation_prediction(X, w)
r_2 = r_squared(y, prediction)
plot_points_regression(X,
                       y,
                       title='Real estate prices prediction',
                       xlabel="m\u00b2",
                       ylabel='$',
                       prediction=prediction,
                       legend=True,
                       r_squared=r_2)