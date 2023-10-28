import time
import os

def read_file_lines(file_path):
    with open(file_path, "r") as file:
        return set(line.strip() for line in file)

def save_data_to_html(data, output_path):
    with open(output_path, "w") as file:
        file.write("\n".join(data))

def process_data(initial_realmbase, abc_path, bcd_path):
    # 读取初始 realmbase.txt 和 abc.txt 的数据
    realmbase_data = read_file_lines(initial_realmbase)
    abc_data = read_file_lines(abc_path)

    # 找出仅存在于 abc.txt 中的数据
    new_data = abc_data.difference(realmbase_data)

    # 保存新增数据到 realm1.html
    save_data_to_html(new_data, bcd_path)

def main():
    realmbase_path = os.path.expanduser("~/atom/ok/realmbase.txt")
    abc_path = os.path.expanduser("~/atom/ok/abc.txt")
    bcd_path = os.path.expanduser("~/var/www/html/realm1.html")
    
    # 初始化时处理所有数据
    process_data(realmbase_path, abc_path, bcd_path)

    while True:
        # 处理新增数据每隔 10 秒
        process_data(realmbase_path, abc_path, bcd_path)
        time.sleep(10)

if __name__ == "__main__":
    main()
