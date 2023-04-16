import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# initialize the data ingestion configration 

@dataclass
class DataIngestionConfig():
    train_data_path:str()=os.path.join('artifcats', 'train.csv')
    test_data_path:str()=os.path.join('artifcats', 'test.csv')
    raw_data_path:str()=os.path.join('artifcats', 'raw.csv')

# class for data ingestion
class DataIngestion():
    def __init__(self):
        self.ingestionConfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion methods Starts.")
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info("Dataset reed as pandas df")
            os.makedirs(os.path.dirname(self.ingestionConfig.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestionConfig.raw_data_path, index=False)
            logging.info("Going to spilt the data into trian test split")

            train_set, test_set = train_test_split(df, test_size=.30)

            train_set.to_csv(self.ingestionConfig.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestionConfig.test_data_path, index=False, header=True)
            logging.info("Training set and  test set is created!")
            logging.info("Data ingestion is completed!")

            return (
                self.ingestionConfig.train_data_path, 
                self.ingestionConfig.test_data_path
            )
        except Exception as e:
            logging.info("Exception occuerd at Data Ingestion stage")
            raise CustomException(e, sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path, test_data_path=obj.initiate_data_ingestion()