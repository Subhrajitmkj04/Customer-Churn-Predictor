import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def preprocess_data(df):
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