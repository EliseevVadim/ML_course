from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

from core.model import AdvancedLinearRegression


def evaluate_model(model: AdvancedLinearRegression, test_data, ground_truth):
    predictions = model.predict(test_data)
    mse = mean_squared_error(ground_truth, predictions)
    mae = mean_absolute_error(ground_truth, predictions)
    r2 = r2_score(ground_truth, predictions)
    return {'MSE': mse, 'MAE': mae, 'R2': r2}


def calculate_mse(model: AdvancedLinearRegression, test_data, ground_truth):
    predictions = model.predict(test_data)
    mse = mean_squared_error(ground_truth, predictions)
    return mse


def calculate_mae(model: AdvancedLinearRegression, test_data, ground_truth):
    predictions = model.predict(test_data)
    mae = mean_absolute_error(ground_truth, predictions)
    return mae


def calculate_r2_score(model: AdvancedLinearRegression, test_data, ground_truth):
    predictions = model.predict(test_data)
    r2 = r2_score(ground_truth, predictions)
    return r2
