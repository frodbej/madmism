from random import randint, sample, random, choice

import numpy as np
from pymoo.core.crossover import Crossover
from pymoo.core.mutation import Mutation
from pymoo.core.sampling import Sampling

from microbiome_feature_set import MicrobiomeFeatureSet


# === Helper functions ===
def get_n_best_features(n, available_features, feature_scores):
    """Get the N best features based on the relevance scores"""
    # Store the index and the score of the available features
    scored_features = [(i, feature_scores[i]) for i in available_features]

    # Sort the features by score in descending order
    sorted_features = sorted(scored_features, key=lambda x: x[1], reverse=True)

    # Select top N features
    selected_features = [x[0] for x in sorted_features[:n]]

    return selected_features
    
def crossover_selection(parent1, parent2, feature_scores):
    """Generate an offspring selection based on the union of parental features and their relevance scores"""

    # Get pool of features constituting the parents
    pool = sorted(list(set(parent1.selection).union(set(parent2.selection))))
    # Get number of features to select
    if parent1.n_features < parent2.n_features:
        n = randint(parent1.n_features, parent2.n_features)
    else:
        n = randint(parent2.n_features, parent1.n_features)

    # Get N best features
    selected_features = get_n_best_features(
        n=n,
        available_features=pool,
        feature_scores=feature_scores
    )

    return selected_features

# === Mutation operations ===

def add_feature(selection, intelligence, n, problem):
    """Insert a new feature into the selection"""
    # Get available features for selection
    available_features = list(set(problem.all_features) - set(selection))
    new_selection = selection.copy()
    
    if intelligence:
        # Randomly add a new feature from the N best available features
        new_selection.append(choice(get_n_best_features(n, available_features, problem.feature_scores)))

    else:
        # Randomly add a new feature from the available features
        new_selection.append(choice(available_features))

    return MicrobiomeFeatureSet(new_selection, problem).evaluate_solution()


def remove_feature(selection, problem):
    """Remove a feature from the selection"""
    # Remove a random feature from the set
    new_selection = selection.copy()
    new_selection.remove(choice(new_selection))
    
    return MicrobiomeFeatureSet(new_selection, problem).evaluate_solution()
    

def replace_feature(selection, intelligence, n, problem):
    """Remove one feature from the selection and add another one"""
    # Get available features for selection
    available_features = list(set(problem.all_features) - set(selection))
    new_selection = selection.copy()

    # Remove a random feature from the set
    new_selection.remove(choice(new_selection))

    if intelligence:
        # Randomly add a new feature from the N best available features
        new_selection.append(choice(get_n_best_features(n, available_features, problem.feature_scores)))

    else:
        # Randomly add a new feature from the available features
        new_selection.append(choice(available_features))

    return MicrobiomeFeatureSet(new_selection, problem).evaluate_solution()

# === Evolutionary operators ===

class MySampling(Sampling):
    """The initialization operator first generates individuals using N highly ranked features.
    Then, the remaining population is generated from random combinations of highly ranked features."""

    def _do(self, problem, n_samples, **kwargs):

        X = np.full((n_samples, 1), None, dtype=object)
        best_n_features = get_n_best_features(
            n=problem.max_features,
            available_features=problem.all_features,
            feature_scores=problem.feature_scores
        )
        
        for i in range(n_samples):
            if i < problem.max_features:
                # Select the best i+1 features
                selection = best_n_features[:i+1]
                X[i, 0] = MicrobiomeFeatureSet(selection, problem).evaluate_solution()
            else:
                # Get random number of features between min and max
                n_features = randint(problem.min_features, problem.max_features)
                # Select a random combination of features from the best features
                selection = sample(best_n_features, k=n_features)
                X[i, 0] = MicrobiomeFeatureSet(selection, problem).evaluate_solution()

        return X


class MyCrossover(Crossover):
    """The crossover operator combines the features from both parents and selects
    the best N features to constitute the offspring solution."""

    def __init__(self):
        super().__init__(n_parents = 2, n_offsprings = 1)
    
    # return the same population taken as input
    def _do(self, problem, X, **kwargs):

        _, n_matings, n_var = X.shape
        Y = np.empty((self.n_offsprings, n_matings, n_var), dtype=object)

        # for each mating provided
        for k in range(n_matings):
            # get the first and the second parent
            a, b = X[0, k, 0], X[1, k, 0]

            # perform crossover
            new_selection = crossover_selection(a, b, problem.feature_scores)
            Y[0, k, 0] = MicrobiomeFeatureSet(new_selection, problem)

        return Y

class MyMutation(Mutation):
    """The mutation operator applies one of three mutation types: add, remove, or replace.
    It combines intelligent and random variants based on a predefined probability."""

    def __init__(self):
        super().__init__()

    def _do(self, problem, X, **kwargs):

        # Iterate over each individual
        for i in range(len(X)):

            intelligence = False
            if random() < problem.intelligent_mutation_pb:
                intelligence = True
            ind = X[i, 0]

            if ind.n_features == problem.min_features:
                # add or replace
                mut = choice(['replace', 'add'])
                if mut == 'replace':
                    X[i, 0] = replace_feature(ind.selection, intelligence, problem.max_features, problem)
                else:
                    X[i, 0] = add_feature(ind.selection, intelligence, problem.max_features, problem)

            elif ind.n_features == problem.max_features:
                # remove or replace
                mut = choice(['replace', 'remove'])
                if mut == 'replace':
                    X[i, 0] = replace_feature(ind.selection, intelligence, problem.max_features, problem)
                else:
                    X[i, 0] = remove_feature(ind.selection, problem)
            
            else:
                # add, remove or replace
                mut = choice(['add', 'remove', 'replace'])
                if mut == 'add':
                    X[i, 0] = add_feature(ind.selection, intelligence, problem.max_features, problem)
                elif mut == 'remove':
                    X[i, 0] = remove_feature(ind.selection, problem)
                else:
                    X[i, 0] = replace_feature(ind.selection, intelligence, problem.max_features, problem)

        return X