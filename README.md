# Customer Churn Predictor

## Overview
This project predicts customer churn using machine learning techniques. It includes exploratory data analysis (EDA), preprocessing, and model training.

## Project Structure
```
Customer-Churn-Predictor/
├── app/
│   ├── app.py
│   ├── helpers/
├── data/
│   ├── processed/
│       ├── Telco_customer_churn.csv
├── models/
│   ├── model.py
├── notebooks/
│   ├── EDA/
│       ├── EDA.ipynb
│   ├── Plots/
│       ├── plots.ipynb
├── src/
│   ├── evaluate/
│       ├── evaluate.py
│   ├── predict/
│       ├── predict.py
│   ├── preprocess/
│       ├── preprocess.py
│   ├── train/
│       ├── train.py
├── requirements.txt
├── setup.py
└── README.md
```

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