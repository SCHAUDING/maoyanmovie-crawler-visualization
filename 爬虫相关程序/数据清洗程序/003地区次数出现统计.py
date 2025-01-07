# 读取文件内容
with open('猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

# 初始化一个字典来存储国家及其出现次数
country_count = {}

# 遍历每一行
for line in content:
    # 找到出品地区的信息
    if '出品地区' in line:
        # 提取出品地区的内容
        countries = line.split('出品地区: ')[1].strip()
        # 按逗号分隔国家
        for country in countries.split(','):
            country = country.strip()  # 去除多余的空格
            # 统计国家出现次数
            if country in country_count:
                country_count[country] += 1
            else:
                country_count[country] = 1

# 将国家及其次数转换为元组，并按次数从大到小排序
sorted_countries = sorted(country_count.items(), key=lambda x: x[1], reverse=True)

# 输出排序后的结果
# for country, count in sorted_countries:
#     print(f"{country}: {count}")
print(sorted_countries)

# [('中国大陆', 194), ('美国', 97), ('中国香港', 29), ('日本', 6), ('中国台湾', 5), ('印度', 4), ('英国', 4), ('加拿大', 4), ('澳大利亚', 1), ('德国', 1), ('新西兰', 1), ('阿联酋', 1), ('捷克', 1), ('俄罗斯', 1), ('芬兰', 1)]