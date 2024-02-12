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
- Also added unique ID to each response.

### `data_analysis.ipynb` ###

- Visualise distribution of respondents based on their `Age group`, `gender`, `marital_status` and more.
- Visualise the number of car parts to customise with respect to their budget for customisation
- Created models `linear regression`, `SVM`, `ANN`

### `apriori.ipynb` ###

- This file is used to find the association rules between the different car parts that the respondents want to customise.
- Likelihood of customising a car part given that another car part is customised.
- More details in the script markdown itself.

### `pca.ipynb` ###

- This file is used to perform PCA on the dataset to reduce the dimensionality of the dataset.
- Also visualise the variance explained by each principal component.

## Directory Tree ##

    ├── .gitignore
    ├── data
    │   ├── cleaned_data.csv
    │   ├── cleaned_data.xlsx
    │   └── SURVEY RESULTS_2024.xlsx
    ├── docs
    │   └── MA4829 Group Assignment_S2 23_24.pdf
    ├── images
    │   └── NTU.png
    ├── README.md
    ├── requirements.txt
    └── src
        ├── apriori.ipynb
        ├── data_analysis.ipynb
        ├── data_cleaning.ipynb
        ├── pca.ipynb
        └── utils
            └── dir.py

## Contributors ##

1. `Rzi98`
