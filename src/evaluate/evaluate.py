from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_models(models, X_train, y_train, X_test, y_test):
    for name, model in models.items():
        print(f"\n{'='*40}")
        print(f" TRAINING & EVALUATING: {name}")
        print(f"{'='*40}")
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")
        print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")
        
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=['Stayed', 'Churned']))
        
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=['Predicted Stayed', 'Predicted Churned'],
                    yticklabels=['Actual Stayed', 'Actual Churned'])
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.title(f'Confusion Matrix: {name}')
        plt.show()