import os

def write_population_scores(population, args):
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)

    with open(args.output_path, "w") as f:
        f.write("seed\tnum_features\tauc\tfeatures\n")
        for individual in population:
            ind = individual[0]
            f.write(f"{args.seed}\t{ind.n_features}\t{ind.auc}\t{ind.get_feature_names()}\n")
