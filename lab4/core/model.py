import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


class AdvancedLinearRegression:
    def __init__(self, name=None, scale=False, use_pca=False, n_pca_components=None):
        self.__name = name
        self.__use_pca = use_pca
        self.__model = LinearRegression()
        self.__scaler = StandardScaler() if scale else None
        self.__pca = PCA(n_components=n_pca_components) if use_pca else None

    def __str__(self):
        return self.__name

    def fit(self, X, y):
        if self.__scaler is not None:
            X = self.__scaler.fit_transform(X)
        if self.__pca is not None:
            X = self.__pca.fit_transform(X)
        self.__model.fit(X, y)

    def predict(self, X):
        if self.__scaler is not None:
            X = self.__scaler.transform(X)
        if self.__pca is not None:
            X = self.__pca.transform(X)
        return np.round(self.__model.predict(X))

    @property
    def pca(self):
        return self.__pca

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
