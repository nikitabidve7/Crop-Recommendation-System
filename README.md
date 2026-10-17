## Crop Recommendation System
A precision agriculture decision-support system that uses supervised machine learning to recommend the most suitable crop to grow based on soil nutrition and environmental conditions. 
This project was developed as part of an M.Tech AI/ML research study and practical deployment framework.

---

## Key Results & Performance
Four supervised machine learning classifiers were evaluated on a standardized agricultural dataset (2,200 samples with an 80-20 train-test split):
* **Random Forest Classifier:** **99.32% Accuracy** (Selected as the optimal model for deployment)
* **Decision Tree Classifier:** 98.64% Accuracy
* **K-Nearest Neighbors (KNN):** 97.05% Accuracy
* **Support Vector Machine (SVM):** 96.14% Accuracy

Feature importance analysis reveals that **rainfall** and **humidity** carry the highest predictive weight in determining crop viability, followed by soil potassium ($\text{K}$) and phosphorus ($\text{P}$).

---

## Tech Stack & Requirements
* **Language:** Python 3.x
* **Data Processing:** `pandas`
* **Machine Learning:** `scikit-learn`
* **Model Serialization:** `joblib`
* **Visualization:** `matplotlib` & `shap`
* **Web Interface:** `streamlit`
