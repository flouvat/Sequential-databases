# Datasets for sequential pattern mining

This project transforms several [UCI datasets](http://archive.ics.uci.edu/ml/datasets/) into sequential databases (sequences of itemsets). The main objective is to have benchmark datasets that can be used for sequential pattern mining. The format of the sequential datasets is the one used by the [SPMF library](https://www.philippe-fournier-viger.com/spmf/).

The following datasets were transformed:
- ["Clickstream data for online shopping Data Set"](http://archive.ics.uci.edu/ml/datasets/clickstream+data+for+online+shopping)
- ["microblogPCU Data Set"](http://archive.ics.uci.edu/ml/datasets/microblogPCU)
- ["Online Retail Data Set"](http://archive.ics.uci.edu/ml/datasets/Online+Retail+II)

The "Data/Raw" directory contains original datasets from the UCI archives.

The "Data/CSV" directory contains the datasets in CSV format. Several processing have been done in these datasets (aggregations, removal of bad values, extraction of keywords, etc.). The details can be found in Jupyter Notebook files in the "Code" directory.

The "Data/SPMF" directory contains the preprocessed CSV data transformed in SPMF sequential database format. Since this format only deals with integer values, the initial data has been mapped into integers. The mapping is stored in json files.

