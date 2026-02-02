# Code

This folder contains all the scripts required to run MADMISM.

## Input

MADMISM requires:
1. Data file: samples as rows, OTUs as columns (`<dataset>-data.csv`)
2. Labels file: one column with sample labels (`<dataset>-labels.csv`)

Example for the YB-GG dataset in the `../datasets/` directory:
- `YB-GG-data.csv`
- `YB-GG-labels.csv`

## Usage

Show all arguments:

```bash
python3 main.py -h
```

Run MADMISM with a population size of 20, 125 generations, and a maximum of 11 features for the YB-GG dataset:

```bash
python3 main.py -d YB-GG -p 20 -g 125 --max_features 11
```

## Output

After running MADMISM, the final solutions are saved in `output/scores.tsv`. This file includes the following columns:
- `seed`: random seed used.
- `num_features`: number of features selected.
- `auc`: classification performance of the subset.
- `features`: feature names.