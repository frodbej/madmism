# MADMISM: Multi-objective Approach based on Dominance for MIcroorganism Selection on Microbiomes

## Citation

If you use this code in your research or project, please cite the following publication:

"Multi-Objective Genetic Algorithm with Maximum-Entropy Classification and Domain-Specific Evolutionary Operators for Microorganism Selection on Microbiomes". Fernando M. Rodríguez-Bejarano, Sergio Santander-Jiménez, Miguel A. Vega-Rodríguez. Applied Soft Computing, Volume 189, 114526, Elsevier, Amsterdam, Netherlands, 2026, pp. 1-17, ISSN: 1568-4946. DOI: [10.1016/j.asoc.2025.114526](https://doi.org/10.1016/j.asoc.2025.114526).

```bibtex
@article{rodriguez26,
  title={Multi-objective genetic algorithm with maximum-entropy classification and domain-specific evolutionary operators for microorganism selection on microbiomes},
  author={Rodr{\'\i}guez-Bejarano, Fernando M. and Santander-Jim{\'e}nez, Sergio and Vega-Rodr{\'\i}guez, Miguel A.},
  journal={Applied Soft Computing},
  volume={189},
  pages={114526},
  year={2026},
  publisher={Elsevier},
  doi={10.1016/j.asoc.2025.114526}
}
```

## Overview

**MADMISM** is a multi-objective evolutionary approach based on dominance that performs microorganism selection on microbiome data. In this framework, microorganism selection is formulated as a multi-objective optimization problem where classification performance (AUC) is maximized while the number of OTUs employed is minimized. MADMISM is built upon NSGA-III and incorporates three domain-specific operators for initialization, crossover, and mutation. These operators leverage statistical information to identify relevant OTUs for the classification task.

## Datasets

The datasets used in the experiments are publicly available and derived from previously published microbiome studies.

- The sequencing data for the YB-GG dataset was generated in the following [study](https://doi.org/10.1128/msystems.00195-16). The data was preprocessed using Qiime2. Specifically, raw sequencing reads were trimmed and quality filtered, and a closed-reference alignment with the GreenGenes database was performed to generate the OTU table. Then, centered log-ratio transformation was applied, OTUs with zero variance were discarded, and the data was scaled. The processed dataset used as input to MADMISM is located in the `datasets` folder.
- The OTU tables and sample labels for CRC-GG and CRC-RS are available [here](https://knightslab.org/MLRepo/docs/kostic_healthy_tumor.html).
- The OTU tables and sample labels for LH-GG and LH-RS are available [here](https://knightslab.org/MLRepo/docs/ravel_nugent_category.html).
- The OTU tables and sample labels for BW-GG and BW-RS are available [here](https://knightslab.org/MLRepo/docs/ravel_white_black.html).
- The OTU table and sample labels for the CH-RS are available [here](https://knightslab.org/MLRepo/docs/qin_healthy_cirrhosis.html).

## Code

The source code for MADMISM is available on the `code/` directory. See `code/README.md` for execution instructions.
