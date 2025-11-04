import os
from box.exceptions import BoxValueError
import yaml
from src.Chicken_Disease_Classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content, custom_dict=True)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=False):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content, custom_dict=True)


@ensure_annotations
def save_pin(data: Any, path: Path):
    with open(path, "wb") as f:
        joblib.dump(data, f)
        
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_pin(path: Path) -> Any:
    with open(path, "rb") as f:
        data = joblib.load(f)
        
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(file_path: Path) -> str:
    size_in_kb = round(os.path.getsize(file_path) / 1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    filename = fileName
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64String(imagePath):
    with open(imagePath, "rb") as f:
        return base64.b64encode(f.read())