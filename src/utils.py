import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException

import dill
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok= True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
from sklearn.metrics import r2_score

def evaluate_models(X_train, y_train, X_test, y_test, models: dict):
  
    try:
        report = {}
        for model_name, model in models.items():
            # Train
            model.fit(X_train, y_train)
            # Predict
            y_test_pred = model.predict(X_test)
            # Score
            test_model_score = r2_score(y_test, y_test_pred)
            # Record
            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
