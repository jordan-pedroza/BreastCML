from yml_loader import YmlLoader
from data_cleaner import DataCleaner
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier



class Model():
    #contructor
    def __init__(self, config_path):
        self._YML = YmlLoader(config_path)
        self._config = self.YML.load_yml()
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
            
    def test_model(self):
        raise NotImplementedError
    
    def _clean_data(self):
        data_cleaner = DataCleaner(self.config["FOLDER_PATH"],
                                    self.config["VALID_EXTS"][0])
        df_list_1 = data_cleaner.load_data()
        print(df_list_1)
        self._data = df_list_1

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
        raise NotImplementedError
