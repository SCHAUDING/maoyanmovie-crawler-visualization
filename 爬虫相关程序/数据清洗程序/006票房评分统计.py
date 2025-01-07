# 打开文件并读取内容
with open('猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化一个空列表来存储结果
result_list = []

# 遍历每一行数据
for line in lines:
    # 分割每一行的数据
    parts = line.split()
    
    # 提取票房数和评分
    box_office = parts[9]
    rating = parts[7]
    
    # 将票房数和评分存储为字典，并添加到列表中
    result_list.append({"票房数": box_office, "评分": rating})
    
    with open('猫眼电影票房榜数据可视化/数据/票房数_评分统计.txt', 'a', encoding='utf-8') as file:
        file.write(f"{{'票房数': {box_office}, '评分': {rating}}},\n")
# 打印结果列表
print(result_list)