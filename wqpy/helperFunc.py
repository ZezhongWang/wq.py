import os
import json
import traceback


def get_temp_path(name):
    """获取存放临时文件的路径"""
    temp_path = os.path.join(os.getcwd(), 'temp')
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    path = os.path.join(temp_path, name)
    return path


def get_global_setting():
    file_name = 'GlobalSetting.json'
    current_folder = os.getcwd()
    setting_path = os.path.join(current_folder, file_name)
    try:
        with open(setting_path, 'rb') as f:
            setting = f.read()
            if type(setting) is not str:
                setting = str(setting, encoding='utf8')
            global_setting = json.loads(setting)
            return global_setting
    except FileNotFoundError:
        traceback.print_exc()
