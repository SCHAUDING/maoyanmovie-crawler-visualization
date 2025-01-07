# 打开文件并读取内容
with open('猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化一个空列表来存储结果
result_list = []

# 遍历每一行数据
for line in lines:
    # 分割每一行的数据
    parts = line.split()
    
    # 提取平均票价和场均人次
    price = float(parts[11])  # 将平均票价转换为浮点数
    num_people = int(parts[13])  # 将场均人次转换为整数
    
    # 将平均票价和场均人次存储为字典，并添加到列表中
    result_list.append({"平均票价": price, "场均人次": num_people})

# 按平均票价降序排序
result_list.sort(key=lambda x: x["平均票价"], reverse=False)

# 将排序后的结果写入文件
with open('猫眼电影票房榜数据可视化/数据/平均票价_场均人次统计.txt', 'w', encoding='utf-8') as file:
    for item in result_list:
        file.write(f"{{'平均票价': {item['平均票价']}, '场均人次': {item['场均人次']}}},\n")

# 打印结果列表
print(result_list)