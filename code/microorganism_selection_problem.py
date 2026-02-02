import numpy as np
from pymoo.core.problem import ElementwiseProblem

class MicroorganismSelectionProblem(ElementwiseProblem):
    """
    Multi-objective problem for microorganism (OTU) selection.
    Objectives:
        - Maximize the number of discarded features
        - Maximize classification performance (AUC)
    Both objectives are transformed to be minimized.
    """

    def __init__(self, dataset, labels, feature_scores, args):
        super().__init__(n_var=1, n_obj=2)

        self.dataset = dataset
        self.labels = labels
        self.n_total_features = dataset.shape[1]
        self.all_features = list(range(self.n_total_features))
        self.max_features = args.max_features
        self.min_features = args.min_features
        self.feature_scores = feature_scores
        self.intelligent_mutation_pb = args.intelligent_mutation_pb

    def _evaluate(self, x, out, *args, **kwargs):
        
        solution = x[0]
        f1 = - (self.n_total_features - solution.n_features) / self.n_total_features
        f2 = - solution.auc

        out['F'] = np.array([f1, f2])
