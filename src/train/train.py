from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
import numpy as np

def train_models(X_train, y_train):
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
        cv_scores[model_name] = scores
        print(f"{model_name} cross-validation accuracy: {np.mean(scores):.2f}")
        print("-"*70)

    return models, cv_scores