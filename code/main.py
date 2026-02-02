from random import seed

import pandas as pd
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.operators.selection.tournament import TournamentSelection
from pymoo.optimize import minimize
from pymoo.util.ref_dirs import get_reference_directions

from argument_parser import parse_args
from banner import print_banner
from binary_tournament import binary_tournament
from evolutionary_operators import MySampling, MyCrossover, MyMutation
from feature_scoring import compute_chi2_scores, filter_features
from microorganism_selection_problem import MicroorganismSelectionProblem
from output_writer import write_population_scores


def main():
    """Executes the MADMISM algorithm for microorganism selection"""

    print_banner()

    args = parse_args()

    # Set seed
    seed(args.seed)
    
    # Load input dataset and labels
    dataset = pd.read_csv(f"../datasets/{args.dataset}-data.csv", index_col=0)
    labels = pd.read_csv(f"../datasets/{args.dataset}-labels.csv", index_col=0)['label']

    scores = compute_chi2_scores(dataset, labels)
    dataset, scores = filter_features(dataset, scores)

    # Problem initialization
    problem = MicroorganismSelectionProblem(
        dataset=dataset,
        labels=labels,
        feature_scores=scores,
        args=args
    )

    # Termination criteria
    termination = ('n_gen', args.generations)

    # Reference directions for the optimization
    ref_dirs = get_reference_directions('das-dennis', n_dim=2, n_partitions=args.popsize - 1)

    # Algorithm initialization with custom operators
    algorithm = NSGA3(
        ref_dirs=ref_dirs,
        pop_size=args.popsize,
        sampling=MySampling(),
        crossover=MyCrossover(),
        mutation=MyMutation(),
        eliminate_duplicates=False,
        selection=TournamentSelection(func_comp=binary_tournament, pressure=2)
    )

    # Optimization
    res = minimize(
        problem=problem,
        algorithm=algorithm,
        termination=termination,
        seed=args.seed,
        verbose=True,
        save_history=False
    )

    # Save final solutions on the output file
    write_population_scores(res.X, args)


if __name__ == "__main__":
    main()
