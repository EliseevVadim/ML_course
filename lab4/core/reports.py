import numpy as np
import pandas as pd

from sklearn.decomposition import PCA


def generate_pca_report(pca: PCA, columns: np.array):
    return pd.DataFrame(pca.components_, columns=columns)


def print_pca_components_with_feature_importance(pca: PCA, report: pd.DataFrame, num_components_display=None,
                                                 num_features_display=None):
    components = pca.components_
    num_components_display = len(components) if num_components_display is None else min(len(components),
                                                                                        num_components_display)
    for i in range(num_components_display):
        displaying_component = report.iloc[i]
        sorted_component = displaying_component.abs().sort_values(ascending=False)
        top_features = sorted_component if num_features_display is None else sorted_component.head(num_features_display)
        print(f"Top features for PCA Component {i + 1}:")
        print(top_features)
        print()
