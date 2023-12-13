from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

from core.model import AdvancedLinearRegression


def evaluate_model(model: AdvancedLinearRegression, test_data, ground_truth):
    predictions = model.predict(test_data)
    mse = mean_squared_error(ground_truth, predictions)
    mae = mean_absolute_error(ground_truth, predictions)
    return {'MSE': mse, 'MAE': mae}


def calculate_mse(model: AdvancedLinearRegression, test_data, ground_truth):
    predictions = model.predict(test_data)
    mse = mean_squared_error(ground_truth, predictions)
    return mse


def calculate_mae(model: AdvancedLinearRegression, test_data, ground_truth):
    predictions = model.predict(test_data)
    mae = mean_absolute_error(ground_truth, predictions)
    return mae
