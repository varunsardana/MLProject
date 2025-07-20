# 🎓 Student Performance Prediction – Machine Learning Project

This project aims to build a machine learning pipeline to predict student academic performance based on various input features such as gender, parental education level, lunch type, and test preparation course. The pipeline follows an end-to-end ML lifecycle including data ingestion, preprocessing, model training using CatBoost, evaluation, and deployment via a Flask application.

---

## 🚀 Project Architecture

MLProject/
├── .ebextensions/ ← AWS Elastic Beanstalk config
├── artifacts/ ← Saved model + data artifacts
├── catboost_info/ ← CatBoost logs and training stats
├── notebook/ ← Jupyter notebooks for EDA and testing
├── src/ ← Source code (pipeline logic, utils, logger)
│ ├── components/ ← Data ingestion, transformation, training
│ ├── pipeline/ ← Training & prediction flow
│ ├── utils.py
│ ├── logger.py
│ └── exception.py
├── templates/ ← HTML templates for Flask
├── application.py ← Flask app
├── requirements.txt ← Project dependencies
├── setup.py ← Packaging script
└── README.md ← Documentation


---

## 🎯 Project Objective

To develop a machine learning system that can predict a student's **Math score out of 100** based on:

- Gender
- Race/ethnicity
- Parental level of education
- Lunch type
- Test preparation status
- Reading & writing scores

The purpose is to support early academic interventions and gain insights into student performance trends.

---

## 🧠 ML Workflow Summary

1. **Data Ingestion**  
   Reads raw CSV → train/test split → saved to `artifacts/`

2. **Data Transformation**  
   - Encodes categorical features  
   - Scales or processes numerics  
   - Saves preprocessor object

3. **Model Training (CatBoostRegressor)**  
   - Fits on training data  
   - Evaluates with metrics (R², MAE, RMSE)  
   - Saves model as `model.pkl`

4. **Prediction Pipeline**  
   - Loads `model.pkl` and `preprocessor.pkl`
   - Transforms new user input
   - Returns math score prediction

5. **Flask Deployment**  
   - Web UI using HTML form  
   - Real-time predictions through `application.py`

---

## 📊 Dataset Used

[Kaggle Dataset: Student Performance](https://www.kaggle.com/spscientist/students-performance-in-exams)

| Feature | Description |
|--------|-------------|
| `gender` | Male / Female |
| `race/ethnicity` | Group A to E |
| `parental level of education` | From High School to Master’s |
| `lunch` | Standard or Free/Reduced |
| `test preparation course` | Completed or None |
| `reading score` | Score out of 100 |
| `writing score` | Score out of 100 |
| `math score` | Target variable |

---

## 🖥️ Web Interface – Flask Demo

Here is a working screenshot of the Flask web UI:


<img width="1204" height="762" alt="image" src="https://github.com/user-attachments/assets/b2e44014-19b8-40a8-a118-1db390ffe8ec" />






---

## 🛠️ Run This Project Locally

### ✅ Step 1: Clone the repo

```bash
git clone https://github.com/varunsardana/MLProject.git
cd MLProject


### Step 2: Install Dependencies
Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Then install the required packages:
pip install -r requirements.txt

### Step 3 Train the model
python src/pipeline/train_pipeline.py

### Step 4 Run the FLask App

python application.py

Go to your browswer and go to: http://127.0.0.1:5000/predictdata

You’ll see a form where you can enter student info. Once submitted, the predicted Math score will appear below.

