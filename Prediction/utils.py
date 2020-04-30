# This is utils file for inprove presentation for jupyter notebooks
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def _func_exp(x, a, b, c):
    #c = 0
    return a * np.exp(b * x) + c


def exponential_regression(x_data, y_data):
    popt, pcov = curve_fit(_func_exp, x_data, y_data, maxfev=50000)
    puntos = plt.plot(x_data, y_data, 'o', color='xkcd:maroon', label="data")
    curva_regresion = plt.plot(x_data, _func_exp(
        x_data, *popt), color='xkcd:teal', label="fit: {:.3f}, {:.3f}".format(*popt))
    plt.legend()
    plt.show()


def _func_logistic(t, a, b, c):
    return c / (1 + a * np.exp(-b*t))


def logistic_regression(x_data, y_data):
    bounds = (0, [100000., 1000., 1000000000.])
    p0 = np.random.exponential(size=3)
    popt, cov = curve_fit(_func_logistic, x_data, y_data,
                          bounds=bounds, p0=p0, maxfev=1000000)
    puntos = plt.plot(x_data, y_data, 'o', color='red', label="data")
    curva_regresion = plt.plot(x_data, _func_logistic(
        x_data, *popt), color='blue', label="logistic")
    plt.legend()
    plt.show()


def _func_hill(t, a, b, c):
    return a * np.power(t, b) / (np.power(c, b) + np.power(t, b))


def hill_regression(x_data, y_data):
    bounds = (0, [100000., 1000., 1000000000.])
    p0 = np.random.exponential(size=3)
    popt, cov = curve_fit(_func_hill, x_data, y_data,
                          bounds=bounds, p0=p0, maxfev=1000000)
    puntos = plt.plot(x_data, y_data, 'o', color='red', label="data")
    curva_regresion = plt.plot(x_data, _func_hill(
        x_data, *popt), color='blue', label="hill")
    plt.legend()
    plt.show()


def graph_lyh(x_data, y_data):
    bounds = (0, [100000., 1000., 1000000000.])
    p0 = np.random.exponential(size=3)
    popt, cov = curve_fit(_func_hill, x_data, y_data,
                          bounds=bounds, p0=p0, maxfev=1000000)
    puntos = plt.plot(x_data, y_data, 'o', color='red', label="data")
    curva_regresion = plt.plot(x_data, _func_hill(
        x_data, *popt), color='blue', label="hill")
    popt0, cov = curve_fit(_func_logistic, x_data, y_data,
                           bounds=bounds, p0=p0, maxfev=1000000)
    curva_regresion2 = plt.plot(x_data, _func_logistic(
        x_data, *popt0), color='green', label="logistic")
    plt.legend()
    plt.show()
