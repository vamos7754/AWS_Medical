
import pandas as pd
import numpy as np
import pickle
import json
import sys
# sys.path.append(r"D:\Velocity\DataScience\Flask&ML_Deployment\ML_LR_Medical_Insurance_Dataset\ML_Medical_insurance_Charges")
import os

import warnings
warnings.filterwarnings('ignore')


class Insurance():
    def __init__(self,age, sex, bmi,children,smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_' + region

    def load_model(self):
        with open("Linear_Model.pkl",'rb') as f:
            self.model = pickle.load(f)

        with open("Project_data.json",'r') as f:
            self.json_data = json.load(f)

    def get_charges(self):
        self.load_model()
        region_index = self.json_data['columns'].index(self.region)

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.age
        test_array[1] = self.json_data['sex'][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data['smoker'][self.smoker]
        test_array[region_index] = 1

        predicted_charges = self.model.predict([test_array])
        return predicted_charges


if __name__ == '__main__':

    age = 54.0
    sex = 'male'
    bmi = 28.3
    children = 3
    smoker = 'yes'
    region = 'southeast'

    object = Insurance(age, sex, bmi,children,smoker, region)
    print(object.get_charges())