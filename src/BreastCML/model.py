from yml_loader import YmlLoader
from data_cleaner import DataCleaner


class Model():
    #contructor
    def __init__(self, config_path):
        self.YML = YmlLoader(config_path)
        self.config = self.YML.load_yml()
        print(self.config["NAME"])
        self.classifier = None
        self.metrics = None
        self.df_list_1 = None

    
    
    def trainmodel(self):
        self.cleanmodel()
    
    def cleanmodel(self):
        data_cleaner = DataCleaner(self.config["FOLDER_PATH"],
                                    self.config["VALID_EXTS"][0])
        df_list_1 = data_cleaner.load_data()
        print(df_list_1)
        self.df_list_1 = df_list_1

        
        
    def testmodel(self):
        raise NotImplementedError
    



