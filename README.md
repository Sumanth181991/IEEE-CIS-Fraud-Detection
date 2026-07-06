# IEEE-CIS Fraud Detection

## Overview

This project builds an end-to-end Machine Learning pipeline to detect fraudulent online transactions using the IEEE-CIS Fraud Detection dataset.

The project follows a production-oriented workflow including data auditing, preprocessing, model comparison, threshold optimization, explainability, and deployment preparation.

---

## Problem Statement

Online payment fraud causes significant financial losses every year.

The objective of this project is to build a machine learning model capable of identifying fraudulent transactions while minimizing false positives.

---

## Dataset

Competition:

IEEE-CIS Fraud Detection (Kaggle)

Dataset consists of:

- train_transaction.csv
- train_identity.csv
- test_transaction.csv
- test_identity.csv

After validating the relationship between both datasets, they were merged using TransactionID.

---

## Project Workflow

### Phase 1 — Business Understanding

- Business Problem
- Success Metrics
- Fraud Detection Objective

---

### Phase 2 — Dataset Understanding

- Documentation Review
- Data Types
- Missing Values
- Memory Usage
- Feature Categories

---

### Phase 3 — Data Validation

- Transaction Dataset Audit
- Identity Dataset Audit
- Merge Validation
- Duplicate Check
- Primary Key Validation

---

### Phase 4 — Memory Optimization

- Downcasting numeric columns
- Memory reduction
- Performance optimization

---

### Phase 5 — Exploratory Data Analysis

- Target distribution
- Numerical feature analysis
- Categorical feature analysis
- Missing value analysis
- Correlation analysis
- Outlier detection
- Feature relationships

---

### Phase 6 — Data Preprocessing

- Train/Test Split
- Data Leakage Prevention
- Missing Value Imputation
- One Hot Encoding
- Standard Scaling
- ColumnTransformer
- Pipeline

---

### Phase 7 — Model Building

Models implemented:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- CatBoost

---

### Phase 8 — Model Evaluation

Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- Classification Report

---

### Phase 9 — Threshold Optimization

Optimized fraud detection threshold by comparing:

- Precision
- Recall
- F1 Score

across multiple probability thresholds.

---

### Phase 10 — Hyperparameter Tuning

Performed RandomizedSearchCV to improve model performance.

---

### Phase 11 — Explainability

- Feature Importance
- Model Interpretation

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Joblib
- Jupyter Notebook

---

## Repository Structure

```
IEEE-CIS-Fraud-Detection/

├── app/
├── config/
├── data/
├── notebooks/
├── models/
├── app/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Results

Successfully developed an end-to-end fraud detection workflow including:

- Data validation
- Feature engineering
- Production preprocessing pipeline
- Multiple ML model comparison
- Threshold optimization
- Feature importance analysis

The project is structured to be extended into a production-ready ML application.

---

## Future Improvements

- Save final production pipeline
- FastAPI REST API
- Docker containerization
- GitHub Actions CI/CD
- Azure deployment
- Model monitoring

---

## Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Pipeline Design
- Model Evaluation
- Hyperparameter Tuning
- Fraud Detection
- Production ML Workflow

---

## Author

**Sumanth Ashwath**

GitHub: https://github.com/Sumanth181991