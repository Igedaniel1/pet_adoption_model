# 🐾 Pet Adoption Prediction Model

## 📌 Objective

Predict the likelihood of a pet being adopted based on features such as breed, color, age, health status, and other characteristics.  
The goal is to assist shelters and platforms in prioritizing animals with lower adoption likelihood.

---

## 🛠️ Tech Stack

- Python
- Flask (for deployment)
- scikit-learn
- imbalanced-learn
- category_encoders
- pandas / numpy

---

## 🧠 Model Pipeline

A machine learning pipeline was created and trained using a combination of preprocessing, oversampling, and ensemble classification:

### 🔍 Features Used

- **Numerical Features:** Standardized using `StandardScaler`  
  Example: Pet Age, Days at Shelter, Health Score, etc.
  
- **Categorical Features:** Encoded using `OneHotEncoder`  
  Example: Breed, Color, Size, Type

### ⚙️ Pipeline Steps

1. **Preprocessing:**
   - `StandardScaler` for numeric columns
   - `OneHotEncoder` for categorical columns via `ColumnTransformer`

2. **Class Imbalance Handling:**
   - Used `ADASYN` to oversample the minority class (less-adopted pets)

3. **Classifier:**
   - RandomForestClassifier with class_weight='balanced' to account for class imbalance


### The model was deployed using flask:

git clone https://github.com/Igedaniel1/pet_adoption_model.git
cd pet_adoption_model
pip install -r requirements.txt
python pet.py






