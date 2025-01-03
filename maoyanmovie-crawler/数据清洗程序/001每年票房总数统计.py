# 读取文件内容
with open('猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化一个字典来存储每年的票房总和
yearly_box_office = {}

# 遍历每一行
for line in lines:
    # 分割每一行的内容
    parts = line.split(" ")
    # 提取年份和票房
    year = parts[5].split('-')[0]  # 提取年份
    box_office = int(parts[9])     # 提取票房
    # 将票房累加到对应年份的总和中
    if year in yearly_box_office:
        yearly_box_office[year] += box_office
    else:
        yearly_box_office[year] = box_office

year_list = []
box_office_list = []
# 打印每年的票房总和
for year, total_box_office in sorted(yearly_box_office.items()):
    year_list.append(year)
    box_office_list.append(total_box_office)
print(year_list)
print(box_office_list)

# ['1998', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
# [136531, 58444, 349841, 281476, 517145, 680945, 1342097, 2847612, 2771087, 3956214, 4404346, 4725760, 1464819, 3305145, 2186504, 4309879, 2415244]