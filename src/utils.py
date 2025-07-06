import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException

import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok= True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
from sklearn.metrics import r2_score

from sklearn.model_selection import GridSearchCV
from sklearn.metrics        import r2_score

def evaluate_models(X_train, y_train, X_test, y_test,
                    models: dict, params: dict) -> dict:
   
    try:
        report = {}

        for model_name, model in models.items():

            grid = params.get(model_name, {})

            if grid:
              
                search = GridSearchCV(
                    estimator = model,
                    param_grid = grid,
                    cv         = 3,
                    n_jobs     = -1      
                )
                search.fit(X_train, y_train)


                best_model = search.best_estimator_
            else:
              
                best_model = model
                best_model.fit(X_train, y_train)


            y_pred = best_model.predict(X_test)
            score  = r2_score(y_test, y_pred)

            report[model_name] = score

        return report

    except Exception as e:
        # wrap in your custom exception
        raise CustomException(e, sys)
    

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)

