from Chicken_Disease_Classifier.config.configuration import ConfigManager
from Chicken_Disease_Classifier.components import data_ingestion
from Chicken_Disease_Classifier import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingest = data_ingestion.DataIngestion(data_ingestion_config)
        data_ingest.download_file()
        data_ingest.extract_zip_file()
        
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e