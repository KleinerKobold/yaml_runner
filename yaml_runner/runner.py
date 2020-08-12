import yaml
from pathlib import Path 
import importlib


def main():
    
    config_file = None
    if len(sys.argv) < 1:
        config_file = Path.cwd() / sys.argv[1]
    else:
        config_file = Path.cwd() / 'example.yaml'
    
    with open(config_file) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)
        for item in yaml_list:
            full_module_name = item["command"]["import"]
            method_name = item["command"]["method"]
            args = item["command"]["arguments"]
            print(f"full_module_name: {full_module_name}")
            mymodule = importlib.import_module(full_module_name)

            method_to_call = getattr(mymodule, method_name)
            result = method_to_call()

if __name__ == '__main__':
    main()
