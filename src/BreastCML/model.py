import random
from yml_loader import YmlLoader
from data_cleaner import DataCleaner
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn import metrics
import pandas as pd
import numpy as np


class Model():
    # contructor
    def __init__(self, config_path):
        self._YML = YmlLoader(config_path)
        self._config = self._YML.load_yml()
        print(self._config["NAME"])
        self._classifier = None
        self._metrics = None
        self._data = None
        self._train_data = None
        self._test_data = None
    
    def train_model(self):
        self._clean_data()
        self._train_data, self._test_data = self._split_data()
        x, y = self._get_xy(self._train_data)
        self._model_init()
        self._classifier.fit(x,y)
            
    def test_model(self):
        x_test, y_test = self._get_xy(self._test_data)
        y_pred = self._classifier.predict(x_test)
        # Model Accuracy, how often is the classifier correct?
        print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
        print(metrics.classification_report(y_test, y_pred))

    def _split_data(self):
        train_data = self._data[0].sample(frac=0.8, random_state = 69)
        test_data = self._data[0].drop(train_data.index)
        
        # return my 80/20 split 
        return train_data, test_data
    
    def _clean_data(self):
        data_cleaner = DataCleaner(self._config["FOLDER_PATH"],
                                    self._config["VALID_EXTS"][0])
        df_list_1 = data_cleaner.load_data()
        self._data = df_list_1
        self._data[0].drop(columns=["id"], inplace=True)

    def _model_init(self):
        if self._config.get("MODEL_TYPE") == 'decision_tree':
            self._classifier = DecisionTreeClassifier()
        elif self._config.get("MODEL_TYPE") == 'ada_boost':
            self._classifier = AdaBoostClassifier()
        elif self._config.get("MODEL_TYPE") == 'random_forest':
            self._classifier = RandomForestClassifier()
        else:
            raise Exception("Couldn't find DT, ADA Boost or RForest, Using DT Model")

    def  _get_xy(self, xy_dataset_to_split):

        y = xy_dataset_to_split['c']
        X = xy_dataset_to_split.drop('c', axis=1)
        return X, y
