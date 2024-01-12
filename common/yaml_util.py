'''
@Project ：publicdemo 
@File    ：yaml_util.py
@Author  ：PanMing
@Date    ：2024/1/10 11:26 
'''
import os
import yaml


# 读取yaml文件
def read_yaml(key):
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入yaml文件
def write_yaml(data):
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="a") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空yaml文件
def clear_yaml():
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()


# 读取yaml文件全部内容
def read_test_yaml(yaml_path):
    with open(os.getcwd() + yaml_path, encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value
