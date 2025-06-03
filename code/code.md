# Machine Learning Code for C2 Detection
This directory contains all scripts and notebooks used to train, validate, and evaluate machine learning models for detecting command-and-control (C2) traffic.  

Refer to each individual notebook for detailed explanations of methods, configuration options, and outputs.

> Ensure that all code is executed in a virtual environment with the correct dependencies installed. Refer to [README.md](../README.md) for setup instructions.

---

## Model Training

### `train_model_v1.ipynb`
- Trains a baseline model using logistic regression.
- Generates visualizations
- Used for initial feature testing and pipeline setup.

### `train_model_v2.ipynb`
- Trains the model using logistic regression.
- Reports output to **`experiment_reports/`**

### `train_model_v3.ipynb`
- Trains the model using random forest.
- Reports output to **`experiment_reports/`**

### `train_model_v4.ipynb`
- Trains the model using random forest, this time ensuring a 20:80 C2 to normal traffic ratio
- Reports output to **`experiment_reports_20_80_ratio_enforced/`**
- Trained model outputs to **`experiment_reports_20_80_ratio_enforced/models/`**

---

## Model Evaluation

### `validate_model.ipynb`
Performs the following validations to expose the model's strengths and weaknesses
- Hold-Out
- Stratified K-Fold
- Repeated Stratified K-Fold
- Stratified Shuffle Split
- LOGO (Leave-One-Group-Out)

Reports output to **`validation_reports/`**

### `inference_on_mixed_traffic.ipynb`
- Loads a trained model and runs it on mixed-traffic CSVs (about 10% C2, 90% normal) to see how well it detects C2 traffic in more realistic conditions.
- Applies the model to each mixed dataset and evaluates predictions at multiple thresholds (0.3, 0.4, 0.5).
- Computes performance metrics including accuracy, precision, recall, F1-score, and AUC.
- Outputs markdown report containing detailed per-framework results to **`inference_reports/`**

### `leave_one_framework_out.ipynb`
- Trains a Random Forest model on five C2 frameworks plus normal traffic; tests it on one held-out C2 framework.
- Enforces a consistent 80:20 normal-to-C2 ratio in both train and test sets.
- Computes performance metrics including accuracy, precision, recall, F1-score, and AUC.
- Outputs markdown reports to **`leave_one_out_reports_rf/`**

### `leave_one_framework_out_no_frame_len.ipynb`
- Same as `leave_one_framework_out.ipynb` but without the `frame.len` feature.
- Outputs markdown reports to **`leave_one_out_reports_rf_no_frame_len/`**

### `leave_one_framework_out_v2.ipynb`
- Same as `leave_one_framework_out.ipynb` but with XGBoost.
- Outputs markdown reports to **`leave_one_out_reports_xgboost/`**

---

## Utils
foo

## Feature Extraction
foo


## Notes
- All notebooks assume pre-extracted CSVs from the feature extraction pipeline.
- For training dataset structure, refer to [datasets.md](../data/datasets.md)
