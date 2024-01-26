import pandas
from glob import glob

class DataCleaner():
    def __init__(self, path, exts):
        self._csv_list = self._path_plus_ext(path, exts)
        

    def load_data(self):
        """
        return: csv_df (list): List of cleaned DataFrames
        """
        csv_df_list =[]
        for path in self._csv_list:
            csv_df = pandas.read_csv(path)
            csv_df_list.append(self._clean_data(csv_df))
        
        return csv_df_list


    def _path_plus_ext(self,folder_path, ext_name):
        csv_path_str = folder_path + "*" + ext_name
        csv_list = glob(csv_path_str)
        return csv_list

    
    def _clean_data(self,df_to_clean):
        return df_to_clean.dropna().drop_duplicates()

