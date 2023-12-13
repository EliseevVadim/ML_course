import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_numeric_columns_distributions(data: pd.DataFrame, columns, plots_in_row, plot_width):
    n_cols = len(columns)
    n_rows = int(np.ceil(n_cols / plots_in_row))

    fig, axes = plt.subplots(n_rows, plots_in_row, figsize=(plot_width * plots_in_row, plot_width * n_rows))

    for i, col in enumerate(columns):
        row_idx = i // plots_in_row
        col_idx = i % plots_in_row
        sns.histplot(data[col], ax=axes[row_idx, col_idx], kde=True, stat="density")

        axes[row_idx, col_idx].set_title(f"Distribution Plot of {col}")
        axes[row_idx, col_idx].set_xlabel(col)

    for i in range(n_cols, n_rows * plots_in_row):
        fig.delaxes(axes.flatten()[i])

    fig.tight_layout()

    plt.show()


def plot_categories_histograms(data: pd.DataFrame, columns):
    for column in columns:
        plt.figure(figsize=(16, 6))
        sns.countplot(data=data, x=column)
        plt.title(f"Histogram for {column} column")
        plt.show()


def plot_categories_correlation_with_target(data: pd.DataFrame, columns, target):
    for column in columns:
        plt.figure(figsize=(16, 6))
        sns.barplot(x=column, y=data[target], data=data, estimator=np.mean)
        plt.title(f"Barplot for {column} column and {target}")
        plt.show()


def plot_pca_cumulative_variance(variance_ratio: np.array):
    cumulative_variance_ratio = np.cumsum(variance_ratio)
    plt.plot(cumulative_variance_ratio)
    plt.xlabel('Number of Principal Components')
    plt.ylabel('Cumulative Variance Ratio')
    plt.title('Cumulative Variance vs. Number of Principal Components')
    plt.show()
