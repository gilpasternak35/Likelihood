# Likelihood
Likelihood is an open source data quality monitoring engine that uses a variety of statistical techniques to answer several simple questions:
1) *Is there a problem with my data?*
2) *If there is a problem with my data, then where is it?*
3) *Is there a potential explanation for the problem with my data?*

The metric of anomaly, called **surprise**, is a probabilistic metric of measuring the potential of an anomaly.

Currently, Likelihood makes use of the following statistical methods:

**Bootstrapping:**:
The Statistical method of bootstrapping is utilized to see if expected counts for categorical values are anomalous

**Time-Series Anomaly Detection using Facebook Prophet:**
Utilizing Time-Series tools imported from facebook prophet, Likelihood tests whether anomalous values are truly surprising, or whether they are more normal when put in the context of time.

**Kernel Density:**
To be combined with PCA (explained next), Kernel Density fits numerical column values under certain density kernels based on their variability and uses this to test for outliers column wise.

**PCA:**
PCA utilizes intelligent dimensionality reduction to reduce the data to a minimal number of dimensions and check for anomalous systematic bias within rows based on the cross-column correlation that is provided by the new and reduced dimensions. Since this is a row based approach and Kernel Density is a column based approach, the two are combined in matrix like fashion (row, column) to pin-point the exact location of outliers to the exact cell of data, finding both systematic bias within rows and column outliers.

**Categorical Metadata:**
As for the categorical columns, their metadata is tracked so that we can track the probability of new columns defying the metadata and use this to find categorical outliers. 

Likelihood is currently in development and will be available as a pip installable package towards the end of summer 2020.






