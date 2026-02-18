The datasets used in the experiments are publicly available and derived from previously published microbiome studies.

- The sequencing data for the YB-GG dataset was generated in the following [study](https://doi.org/10.1128/msystems.00195-16). The data was preprocessed using Qiime2. Specifically, raw sequencing reads were trimmed and quality filtered, and a closed-reference alignment with the GreenGenes database was performed to generate the OTU table. Then, centered log-ratio transformation was applied, OTUs with zero variance were discarded, and the data was scaled. The OTU table and sample labels for YB-GG are available in `YB-GG-data.csv` and `YB-GG-labels.csv`, respectively.
- The OTU tables and sample labels for CRC-GG and CRC-RS are available [here](https://knightslab.org/MLRepo/docs/kostic_healthy_tumor.html).
- The OTU tables and sample labels for LH-GG and LH-RS are available [here](https://knightslab.org/MLRepo/docs/ravel_nugent_category.html).
- The OTU tables and sample labels for BW-GG and BW-RS are available [here](https://knightslab.org/MLRepo/docs/ravel_white_black.html).
- The OTU table and sample labels for the CH-RS are available [here](https://knightslab.org/MLRepo/docs/qin_healthy_cirrhosis.html).
