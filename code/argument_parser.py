import argparse

def parse_args():
    # Command line arguments handler
    parser = argparse.ArgumentParser(description="Multi-objective Approach based on Dominance for MIcroorganism Selection on Microbiomes")
    parser.add_argument("-s", "--seed", type=int, default=0, help="Random seed for reproducibility (default=0)")
    parser.add_argument("-g", "--generations", type=int, default=125, help="Number of generations (default=125)")
    parser.add_argument("-p", "--popsize", type=int, default=20, help="Population size (default=20)")
    parser.add_argument("-d", "--dataset", type=str, help="Name of the input dataset", required=True)
    parser.add_argument("--intelligent_mutation_pb", type=float, default=0.25, help="Probability of applying intelligent mutation operator (default=0.25)")
    parser.add_argument("--min_features", type=int, default=1, help="Minimum number of selected microorganisms (default=1)")
    parser.add_argument("--max_features", type=int, default=20, help="Maximum number of selected microorganisms (default=20)")
    parser.add_argument("--output_path", type=str, default="output/scores.tsv", help="Path to the output file")

    args = parser.parse_args()

    if args.max_features <= args.min_features:
        parser.error("--max_features must be greater than --min_features")

    return args