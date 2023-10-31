# Heart Disease
This project aims to determine whether someone can repay a loan that has been submitted or not. The model is made based on a dataset taken from Kaggle (Home Credit) and goes through several processes such as handling missing values, outliers, data visualization, feature selection using lgbm, resampling and finally create a model.

The project uses the following steps:

1. `Data preprocessing:` The data is cleaned and preprocessed to ensure that it is in a format that can be used by the machine learning model. This includes missing value imputation, feature scaling, and categorical encoding.
2. `Feature selection:` A subset of features is selected that are most relevant to the prediction task. This is done using a variety of feature selection techniques, such as correlation analysis and recursive feature elimination.
3. `Model training:` A machine learning model is trained on the selected features. The model is evaluated using a variety of metrics, such as accuracy, precision, recall, and F1 score.
4. `Model evaluation:`  The trained model is evaluated on a held-out test set to assess its generalizability.

The project uses the following machine learning models:
1. `Logistic regression`
2. `Random forest`
3. `Gradient boosted trees`
4. `XGBoost`

The best performing model is the `XGBoost` model, which achieves an accuracy of 77% on the test set.

## Usage
To use the model, simply provide the following inputs:

Applicant's demographics (e.g., age, gender, marital status)
Applicant's income (e.g., salary, bonuses, investments)
Applicant's assets (e.g., savings, real estate, vehicles)
Applicant's credit history (e.g., credit score, payment history)
The model will then output a prediction of whether the applicant is likely to repay their loan.
