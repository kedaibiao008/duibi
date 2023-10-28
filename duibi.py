import time
import os
import re

def read_file_lines(file_path):
    with open(file_path, "r") as file:
        return file.read()

def extract_three_letter_combinations(text):
    # 使用正则表达式提取3位组合（数字和字母）
    return re.findall(r'\b\w{3}\b', text)

def compare_and_save():
    realmbase_path = os.path.expanduser("~/atom/ok/realmbase.txt")
    abc_path = os.path.expanduser("~/atom/ok/abc.txt")
    
    # 读取 realmbase.txt 和 abc.txt 的数据
    realmbase_data = read_file_lines(realmbase_path)
    abc_data = read_file_lines(abc_path)
    
    # 提取3位组合（任意数字和字母）
    realmbase_combinations = set(extract_three_letter_combinations(realmbase_data))
    abc_combinations = set(extract_three_letter_combinations(abc_data))
    
    # 获取仅存在于abc.txt中的数据
    unique_combinations = abc_combinations.difference(realmbase_combinations)
    
    # 保存结果到realm1.html文件，清除之前的文本
    result_path = "/var/www/html/realm1.html"
    with open(result_path, "w") as result_file:
        for combination in unique_combinations:
            result_file.write(combination + "\n")

# 主循环，每10秒比较一次
while True:
    compare_and_save()
    time.sleep(10)
