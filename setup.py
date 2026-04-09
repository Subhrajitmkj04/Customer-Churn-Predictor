from setuptools import setup, find_packages

setup(
    name="customer-churn-predictor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "imbalanced-learn",
        "xgboost",
        "shap"
    ],
    entry_points={
        "console_scripts": [
            "train=src.train.train:main",
            "evaluate=src.evaluate.evaluate:main",
            "predict=src.predict.predict:main"
        ]
    },
    author="Your Name",
    description="A machine learning project to predict customer churn.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/customer-churn-predictor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)