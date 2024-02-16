# Nanyang Technological University Machine Intelligence MA4829 #

<br>

<div align='center' style="text-align:center">

![Sample Image](https://images.scholarschoice.com.sg/wp-content/uploads/2017/06/NTU.png)

</div>

<p align='center' style="font-size: 20px;">
    MA4829 Module from school of MAE, NTU <br>
    AY 2023/24 Semester 2
</p>

## Environment Setup - Conda ##

- Create a virtual environment using the following command
- `cd` into parent directory.
- Run the following commands in the terminal.

    ```
    conda create -n ma4829 python=3.11
    pip install -r requirements.txt
    ```

## What does each scripts/jupyter file do?

### `data_cleaning.ipynb` ###

- This file is used to shorten the column names and remove the unnecessary columns from the dataset.
- Separate numerical and categorical dataset.
- Also added unique ID to each response.

### `data_analysis.ipynb` ###

- Visualise distribution of respondents based on their `Age group`, `gender`, `marital_status` and more.
- Visualise the number of car parts to customise with respect to their budget for customisation
- Created models `Linear regression`, `Polynomial regression`, `SVR`, `DecisionTree`, `SVM`, `ANN`

### `apriori.ipynb` ###

- This file is used to find the association rules between the different car parts that the respondents want to customise.
- Likelihood of customising a car part given that another car part is customised.
- More details in the script markdown itself.

### `pca.ipynb` ###

- This file is used to perform PCA on the dataset to reduce the dimensionality of the dataset.
- Utilise MCA to perform PCA on the categorical data.
- Also visualise the variance explained by each principal component.
- Unable to retain important features as the variance explained by the first few principal components is very low.

### `experiment.ipynb` ###

- Experimented on Random Forest for multiple categorical data and simple scatter plot on budget and parts to customise

### `visualisation.ipynb` ###

- Count plot of the budget groups and CAD experience

### `clustering.ipynb` ###

- Hierarchical clustering on the data to perform analysis.

## Sample Visualisations ##

### <u>Distribution</u> ###
![ditribution](https://github.com/Rzi98/MA4829-AY23-24-S2/assets/84122776/319465ad-5783-4218-b3f0-da3f6d6d0501)

### <u>Polynomial Regression</u> ###
![polynomial](https://github.com/Rzi98/MA4829-AY23-24-S2/assets/84122776/599e3b9e-7504-48de-b184-d4b5fbfb10ec)

### <u>SVR</u> ###
![svr](https://github.com/Rzi98/MA4829-AY23-24-S2/assets/84122776/2d28b9a7-2702-46cf-8f68-f6eda223a389)



## Directory Tree ##

    ├── .gitignore
    ├── data
    │   ├── cleaned_data.csv
    │   ├── cleaned_data.xlsx
    │   ├── data.csv
    │   ├── numerical_data.csv
    │   └── SURVEY RESULTS_2024.xlsx
    ├── docs
    │   ├── MA4829 Group Assignment_S2 23_24.pdf
    │   └── Report_analysis.docx
    ├── images
    │   ├── ditribution.png
    │   ├── NTU.png
    │   ├── polynomial.png
    │   └── svr.png
    ├── README.md
    ├── requirements.txt
    └── src
        ├── apriori.ipynb
        ├── clustering.ipynb
        ├── data_analysis.ipynb
        ├── data_cleaning.ipynb
        ├── experiment.ipynb
        ├── pca.ipynb
        ├── test
        │   └── PCA.py
        ├── utils
        │   └── dir.py
        └── visualisation.ipynb

## Contributors ##

1. `Rzi98`

2. `Brian1707`

3. `junwei999`

4. `nadiahouti`

5. `ViSV29`

6. `TheVine1`
