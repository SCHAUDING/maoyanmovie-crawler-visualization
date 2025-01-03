from collections import Counter

# 读取文件内容
with open('猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化一个列表来存储所有电影标签
all_tags = []

# 解析每一行，提取电影标签
for line in lines:
    if '电影标签:' in line:
        # 提取电影标签部分
        tags_part = line.split('电影标签: ')[1].split(' 出品地区:')[0]
        # 将标签按逗号分隔，并去除空格
        tags = [tag.strip() for tag in tags_part.split(',')]
        # 将标签添加到所有标签列表中
        all_tags.extend(tags)

# 使用Counter统计每个标签出现的次数
tag_counts = Counter(all_tags)

# 将标签和次数存储为元组，并放入列表中
tag_count_list = [(tag, count) for tag, count in tag_counts.items()]

# 按照元组第二个数值（出现次数）从大到小排序
sorted_tag_count_list = sorted(tag_count_list, key=lambda x: x[1], reverse=True)

print(sorted_tag_count_list)
# # 输出排序后的结果
# for tag, count in sorted_tag_count_list:
#     print(f"{tag}: {count}")

# [('动作', 147), ('剧情', 110), ('冒险', 94), ('喜剧', 88), ('科幻', 64), ('奇幻', 44), ('爱情', 43), ('犯罪', 33), ('动画', 30), ('悬疑', 23), ('惊悚', 17), ('战争', 15), ('历 史', 10), ('灾难', 9), ('家庭', 9), ('古装', 7), ('青春', 6), ('传记', 4), ('谍战', 2), ('武侠', 2), ('神话', 1), ('史诗', 1), ('运动', 1), ('音乐', 1), ('热血', 1), ('西部', 1), ('歌舞', 1), ('校园', 1)]