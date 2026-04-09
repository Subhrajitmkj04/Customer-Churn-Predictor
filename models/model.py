import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import numpy as np
import pickle

def preprocess_data(df):
    """Preprocess the data for training."""
    df = df.drop(columns=['customerID'])
    df['Churn'] = df['Churn'].replace({'Yes': 1, 'No': 0})
    object_columns = df.select_dtypes(include='object').columns
    df = pd.get_dummies(df, columns=object_columns, drop_first=True)

    X = df.drop(columns=['Churn'])
    y = df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    smote = SMOTE(random_state=42)
    X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

    return X_train_smote, X_test, y_train_smote, y_test

def train_models(X_train, y_train):
    """Train multiple models and return them with their cross-validation scores."""
    models = {
        "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(random_state=42)),
        "Random Forest": RandomForestClassifier(random_state=42),
        "XGBoost": XGBClassifier(random_state=42),
        "Neural Network": make_pipeline(
            StandardScaler(), 
            MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42))
    }

    cv_scores = {}

    for model_name, model in models.items():
        print(f"Training {model_name} with default parameters")
        scores = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")
        cv_scores[model_name] = np.mean(scores)
        print(f"{model_name} cross-validation accuracy: {np.mean(scores):.2f}")
        print("-"*70)

    return models, cv_scores

def save_model(model, filename="final_model.pkl"):
    """Save the trained model to the location where it is loaded."""
    filepath = r"C:/Users/91629/ML Projects/Customer-Churn-Predictor/models/" + filename
    with open(filepath, 'wb') as file:
        pickle.dump(model, file)

def main():
    # Load the dataset
    data_path = "../../data/processed/Telco_customer_churn.csv"
    df = pd.read_csv(data_path)

    # Preprocess the data
    X_train, X_test, y_train, y_test = preprocess_data(df)

    # Train the models
    models, cv_scores = train_models(X_train, y_train)

    # Save the best model (example: Random Forest)
    best_model = models["Random Forest"]
    save_model(best_model)

if __name__ == "__main__":
    main()