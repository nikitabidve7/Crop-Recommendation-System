## Crop Recommendation System
A precision agriculture decision-support system that uses supervised machine learning to recommend the most suitable crop to grow based on soil nutrition and environmental conditions. 
This project was developed as part of an M.Tech AI/ML research study and practical deployment framework.

---

## Key Results & Performance
Four supervised machine learning classifiers were evaluated on a standardized agricultural dataset (2,200 samples with an 80-20 train-test split):
* **Random Forest Classifier:** **99.32% Accuracy** (Selected as the optimal model for deployment)
* **Decision Tree Classifier:** 98.64% Accuracy[cite: 1]
* **K-Nearest Neighbors (KNN):** 97.05% Accuracy[cite: 1]
* **Support Vector Machine (SVM):** 96.14% Accuracy[cite: 1]

Feature importance analysis reveals that **rainfall** and **humidity** carry the highest predictive weight in determining crop viability, followed by soil potassium ($\text{K}$) and phosphorus ($\text{P}$)[cite: 3].

---

## Tech Stack & Requirements
* **Language:** Python 3.x[cite: 1]
* **Data Processing:** `pandas`[cite: 1]
* **Machine Learning:** `scikit-learn`[cite: 1]
* **Model Serialization:** `joblib`[cite: 1]
* **Visualization:** `matplotlib` & `shap`[cite: 3]
* **Web Interface:** `streamlit`[cite: 1, 2]
