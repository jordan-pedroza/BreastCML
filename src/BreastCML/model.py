from yml_loader import YmlLoader



class Model():
    #contructor
    def __init__(self, config_path):
        self.YML = YmlLoader(config_path)
        self.config = self.YML.load_yml()
        print(self.config["NAME"])
        self.classifier = None
        self.metrics = None

    def cleanmodel(self):
        raise NotImplementedError

    def trainmodel(self):
        raise NotImplementedError
        
    def testmodel(self):
        raise NotImplementedError
    



