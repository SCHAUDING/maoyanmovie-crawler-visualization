def get_top_n_movies(n, file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 提取前n行的电影名和票房
    movies = []
    for line in lines[:n]:
        parts = line.strip().split()
        movie_name = parts[3]  # 电影名
        box_office = int(parts[9])  # 票房
        movies.append((movie_name, box_office))
    
    # 按照票房从大到小排序
    movies.sort(key=lambda x: x[1], reverse=True)
    
    return movies

# 示例使用
n = 10  # 统计前10行
file_path = '猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.txt'
top_n_movies = get_top_n_movies(n, file_path)
print(top_n_movies)

# [('长津湖', 577534), ('战狼2', 569454), ('你好，李焕英', 541320), ('哪吒之魔童降世', 503570), ('流浪地球', 468739), ('满江红', 454435), ('唐人街探案3', 452356), ('复仇者联盟4：终局之战', 425015), ('长津湖之水门桥', 406745), ('流浪地球2', 404375)]