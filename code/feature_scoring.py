import numpy as np
from sklearn.feature_selection import chi2

def compute_chi2_scores(dataset, labels):
    scores, _ = chi2(dataset, labels)
    return scores

def filter_features(dataset, scores):
    mean_value = np.mean(scores)
    mask = scores > mean_value
    dataset = dataset.iloc[:, mask]
    scores = scores[mask]
    return dataset, scores