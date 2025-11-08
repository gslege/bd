import csv

# 读取CSV文件
with open('result.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # 提取IP地址和下载速度
    data = [(row['IP Address'], float(row['Download Speed (MB/s)'])) for row in reader]

# 按下载速度从高到低排序
data.sort(key=lambda x: x[1], reverse=True)

# 输出到result.txt文件
with open('result.txt', 'w', encoding='utf-8') as txtfile:
    for ip, speed in data:
        txtfile.write(f"{ip}#Free CFnodes {speed}m/s\n")

print("处理完成！结果已保存到result.txt文件。")