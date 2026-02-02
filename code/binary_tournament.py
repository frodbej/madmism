import numpy as np
from random import choice

def binary_tournament(pop, P, **kwargs):
    # P input defines the tournaments and competitors
    n_tournaments, n_competitors = P.shape

    if n_competitors != 2:
        raise Exception("Only pressure=2 allowed for binary tournament!")
    
    S = np.empty(n_tournaments, dtype=int)
    
    for i in range(n_tournaments):
        a, b = P[i]
        rel = dominates(pop[a].F, pop[b].F)
        if rel == 1:
            S[i] = a
        elif rel == -1:
            S[i] = b
        else:
            S[i] = choice([a, b])

    return S


def dominates(a, b):
    """
    Returns:
    1 if a dominates b
    -1 if b dominates a
    0 otherwise
    Assumes minimization of objectives (e.g: negative AUC)
    """

    better = False
    worse = False

    for ai, bi in zip(a, b):
        if ai < bi:
            better = True
        elif ai > bi:
            worse = True

    if better and not worse:
        return 1
    if worse and not better:
        return -1
    return 0