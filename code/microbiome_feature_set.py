
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import SGDClassifier

class MicrobiomeFeatureSet():

    def __init__(self, selection, problem):

        self.selection = selection
        self.n_features = len(self.selection)
        self.problem = problem
    
    def evaluate_solution(self):

        # Get number of features
        self.n_features = len(self.selection)

        # Get reduced dataset with the selected features
        reduced_dataset = self.problem.dataset.iloc[:, list(self.selection)]

        # Get classification performance on the selected features
        clf = SGDClassifier(random_state=1, loss="log_loss", penalty="l1", max_iter=500)
        scores = cross_val_score(clf, reduced_dataset, self.problem.labels, cv=StratifiedKFold(6), scoring="roc_auc")
        self.auc = np.mean(scores)

        return self

    def get_feature_names(self):
        return [self.problem.dataset.columns[idx] for idx in sorted(self.selection)]
