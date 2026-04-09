# Customer Churn Predictor

## 📌 Overview

The **Customer Churn Predictor** is an end-to-end, production-structured machine learning project built to predict telecom customer churn. This project goes beyond a single-model approach by experimenting with multiple algorithms, handling class imbalance using SMOTE, and incorporating model explainability using SHAP.

It is designed to reflect real-world ML engineering workflows, from experimentation to deployment via an interactive Streamlit application.

---

## 🚀 Key Highlights

* 🔬 Compared multiple models:

  * Logistic Regression
  * Random Forest
  * XGBoost Classifier
  * Neural Networks
* ⚖️ Handled class imbalance using **SMOTE**
* 📊 Performed in-depth **EDA and visualization**
* 🧠 Implemented **model explainability using SHAP**
* 💾 Model persistence using **pickle**
* 🌐 Deployed via **Streamlit UI** for real-time predictions

---

## 🏗️ Project Structure

```
Customer-Churn-Predictor/
├── app/                  # Streamlit app (UI + inference)
│   ├── app.py
│   ├── helpers/
│
├── data/
│   ├── processed/        # Cleaned dataset
│       ├── Telco_customer_churn.csv
│
├── models/               # Model definition / utilities
│   ├── model.py
│
├── notebooks/            # Research and experimentation
│   ├── EDA/
│       ├── EDA.ipynb
│   ├── Plots/
│       ├── plots.ipynb
│
├── src/                  # Core ML pipeline
│   ├── evaluate/
│       ├── evaluate.py
│   ├── predict/
│       ├── predict.py
│   ├── preprocess/
│       ├── preprocess.py
│   ├── train/
│       ├── train.py
│
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ ML Pipeline

### 1. Data Preprocessing

* Handling missing values
* Encoding categorical variables
* Feature transformation
* Preparing dataset for modeling

### 2. Model Training

* Trained multiple models for comparison
* Applied **SMOTE** to address class imbalance
* Stored trained models using **pickle**

### 3. Evaluation

* Compared models across key metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC-AUC
* Final model selected based on performance trade-offs

### 4. Explainability

* Used **SHAP (SHapley Additive exPlanations)**
* Generated feature importance and impact visualizations

### 5. Prediction Pipeline

* Modular inference pipeline in `src/predict/predict.py`
* Supports real-time predictions for new customer data

### 6. Application Layer

* Built using **Streamlit**
* Features:

  * Customer selection dropdown
  * Display of customer attributes
  * Real-time churn prediction

---

## 🧪 Dataset

* **Telco Customer Churn Dataset**
* Location: `data/processed/Telco_customer_churn.csv`

Includes:

* Demographics (gender, senior citizen)
* Account info (tenure, contract)
* Services (phone, internet, etc.)
* Billing and payment details

---

## 🖥️ Running the Project

### 1. Clone the repository

```bash
git clone <repo-url>
cd Customer-Churn-Predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train models

```bash
python src/train/train.py
```

### 4. Launch the Streamlit app

```bash
streamlit run app/app.py
```

---

## 📊 Application Preview

The app allows users to:

* Select a customer ID
* View detailed attributes
* Get churn prediction instantly

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)
* SHAP
* Streamlit

---

## 📈 Future Improvements

* Hyperparameter tuning (Optuna / Grid Search)
* Model versioning (MLflow)
* Deployment via FastAPI + Docker
* CI/CD pipeline integration
* Real-time data ingestion

---

## 🎯 Why This Project Stands Out

This project demonstrates:

* Strong ML fundamentals (model comparison, evaluation)
* Handling real-world issues like class imbalance
* Explainable AI integration (SHAP)
* Clean, production-style code structure
* End-to-end deployment mindset

---

## 👨‍💻 Author

Built as a production-oriented ML engineering project showcasing end-to-end pipeline design, experimentation, and deployment.
# Customer Churn Predictor

## 📌 Overview

The **Customer Churn Predictor** is an end-to-end, production-structured machine learning project built to predict telecom customer churn. This project goes beyond a single-model approach by experimenting with multiple algorithms, handling class imbalance using SMOTE, and incorporating model explainability using SHAP.

It is designed to reflect real-world ML engineering workflows, from experimentation to deployment via an interactive Streamlit application.

---

## 🚀 Key Highlights

* 🔬 Compared multiple models:

  * Logistic Regression
  * Random Forest
  * XGBoost Classifier
  * Neural Networks
* ⚖️ Handled class imbalance using **SMOTE**
* 📊 Performed in-depth **EDA and visualization**
* 🧠 Implemented **model explainability using SHAP**
* 💾 Model persistence using **pickle**
* 🌐 Deployed via **Streamlit UI** for real-time predictions

---

## 🏗️ Project Structure

```
Customer-Churn-Predictor/
├── app/                  # Streamlit app (UI + inference)
│   ├── app.py
│   ├── helpers/
│
├── data/
│   ├── processed/        # Cleaned dataset
│       ├── Telco_customer_churn.csv
│
├── models/               # Model definition / utilities
│   ├── model.py
│
├── notebooks/            # Research and experimentation
│   ├── EDA/
│       ├── EDA.ipynb
│   ├── Plots/
│       ├── plots.ipynb
│
├── src/                  # Core ML pipeline
│   ├── evaluate/
│       ├── evaluate.py
│   ├── predict/
│       ├── predict.py
│   ├── preprocess/
│       ├── preprocess.py
│   ├── train/
│       ├── train.py
│
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ ML Pipeline

### 1. Data Preprocessing

* Handling missing values
* Encoding categorical variables
* Feature transformation
* Preparing dataset for modeling

### 2. Model Training

* Trained multiple models for comparison
* Applied **SMOTE** to address class imbalance
* Stored trained models using **pickle**

### 3. Evaluation

* Compared models across key metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC-AUC
* Final model selected based on performance trade-offs

### 4. Explainability

* Used **SHAP (SHapley Additive exPlanations)**
* Generated feature importance and impact visualizations

### 5. Prediction Pipeline

* Modular inference pipeline in `src/predict/predict.py`
* Supports real-time predictions for new customer data

### 6. Application Layer

* Built using **Streamlit**
* Features:

  * Customer selection dropdown
  * Display of customer attributes
  * Real-time churn prediction

---

## 🧪 Dataset

* **Telco Customer Churn Dataset**
* Location: `data/processed/Telco_customer_churn.csv`

Includes:

* Demographics (gender, senior citizen)
* Account info (tenure, contract)
* Services (phone, internet, etc.)
* Billing and payment details

---

## 🖥️ Running the Project

### 1. Clone the repository

```bash
git clone <repo-url>
cd Customer-Churn-Predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train models

```bash
python src/train/train.py
```

### 4. Launch the Streamlit app

```bash
streamlit run app/app.py
```

---

## 📊 Application Preview

The app allows users to:

* Select a customer ID
* View detailed attributes
* Get churn prediction instantly

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)
* SHAP
* Streamlit

---

## 📈 Future Improvements

* Hyperparameter tuning (Optuna / Grid Search)
* Model versioning (MLflow)
* Deployment via FastAPI + Docker
* CI/CD pipeline integration
* Real-time data ingestion

---

## 🎯 Why This Project Stands Out

This project demonstrates:

* Strong ML fundamentals (model comparison, evaluation)
* Handling real-world issues like class imbalance
* Explainable AI integration (SHAP)
* Clean, production-style code structure
* End-to-end deployment mindset

---

## 👨‍💻 Author

Built as a production-oriented ML engineering project showcasing end-to-end pipeline design, experimentation, and deployment.


## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Customer-Churn-Predictor
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the EDA notebook:
   ```bash
   jupyter notebook notebooks/EDA/EDA.ipynb
   ```
2. Train the model:
   ```bash
   python src/train/train.py
   ```
3. Evaluate the model:
   ```bash
   python src/evaluate/evaluate.py
   ```

## Dependencies
See `requirements.txt` for the full list of dependencies.

## License
This project is licensed under the MIT License.
