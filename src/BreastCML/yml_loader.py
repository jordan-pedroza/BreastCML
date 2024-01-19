import yaml



class YmlLoader():
    def __init__(self,path) -> None:
        self.path = path

    def load_yml(self):
        with open(self.path) as file:
            return yaml.safe_load(file)