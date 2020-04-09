import yaml
import os

dir_path = os.path.abspath(os.path.dirname(__file__))
print("+++++"+dir_path)
config_path=dir_path+"/confing/conf.yaml"


def read_yaml():
    with open('/Users/potato/PycharmProjects/vipdemo/confing/conf.yaml', 'r', encoding='utf-8') as f:
        data_yaml = yaml.load(f)
        print(data_yaml)
    return data_yaml


read_yaml()
