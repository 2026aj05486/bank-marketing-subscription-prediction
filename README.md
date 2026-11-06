# Bank Marketing Subscription Prediction

A Streamlit application for evaluating five saved machine-learning classifiers on the UCI Bank Marketing dataset.

## Repository

https://github.com/2026aj05486/bank-marketing-subscription-prediction

## Dataset and preparation

- Dataset: UCI Bank Marketing (`bank-full.csv`), 45,211 records.
- Target: `y` (term-deposit subscription: yes/no).
- `duration` is excluded to avoid target leakage.
- 15 input features are used (6 numerical and 9 categorical).
- Stratified 80/20 train/test split with random_state=42 (36,168 train; 9,043 test).
- Numerical features use StandardScaler; categorical features use OneHotEncoder.
- The preprocessor is fitted on the training set only; transformed feature count: 50.
- Target distribution is imbalanced (approximately 88.3% no, 11.7% yes).

## Baseline test results

| Model | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8933 | 0.7717 | 0.6632 | 0.1786 | 0.2815 | 0.3065 |
| Decision Tree | 0.8309 | 0.6132 | 0.2982 | 0.3289 | 0.3128 | 0.2170 |
| K-Nearest Neighbors | 0.8874 | 0.7027 | 0.5529 | 0.1975 | 0.2911 | 0.2833 |
| Gaussian Naive Bayes | 0.8452 | 0.7514 | 0.3708 | 0.4641 | 0.4123 | 0.3271 |
| Linear SVM | 0.8932 | 0.7682 | 0.6513 | 0.1871 | 0.2907 | 0.3101 |

Gaussian Naive Bayes has the highest recall, F1 and MCC in the baseline comparison. Logistic Regression has the highest accuracy, AUC and precision. Accuracy should be interpreted with care because the target is imbalanced.

## Application

The app evaluates saved models; it does not retrain them. It provides model selection, CSV upload, accuracy, AUC, precision, recall, F1, MCC, a confusion matrix and a classification report. Uploaded CSVs must contain the 15 model input features and target column `y`.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Open https://share.streamlit.io/ and sign in with GitHub.
2. Select this repository, branch `main`, and main file `app.py`.
3. Click Deploy.

The saved model artifacts are packaged in `project_bundle.zip`. The root `app.py` extracts the bundle at startup and runs the application code included in it.
