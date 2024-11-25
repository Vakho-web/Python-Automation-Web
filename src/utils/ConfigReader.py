import yaml
import os

def get_config():
    config_path = os.path.join(os.path.dirname(__file__), "../resources/ConfigFile.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)