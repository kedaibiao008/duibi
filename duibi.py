import time
import os
import re

def read_file_lines(file_path):
    with open(file_path, "r") as file:
        return file.read()

def extract_three_letter_combinations(text):
    # 使用正则表达式提取3位组合（数字和字母）
    return re.findall(r'\b\w{3}\b', text)

def main():
    realmbase_path = os.path.expanduser("~/atom/ok/realmbase.txt")
    
    # 读取 realmbase.txt 的数据
    realmbase_data = read_file_lines(realmbase_path)
    
    # 提取3位组合（任意数字和字母）并打印
    combinations = extract_three_letter_combinations(realmbase_data)
    for combination in combinations:
        print(combination)

if __name__ == "__main__":
    main()
