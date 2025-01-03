# 爬取 电影名字 上映时间 评分 票房 平均票价 电影详细信息链接 电影标签 出品地区
import requests
import lxml
import csv
from bs4 import BeautifulSoup

# 爬取 电影标签 出品地区 评分
def get_tags_region(sublink, headers_dic):
    # 发起请求
    response_html = requests.get(sublink, headers=headers_dic).text

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response_html, 'lxml')

    # 提取标签信息
    tags_element = soup.select_one('div.detail-list > div > p')
    tags = soup.select_one('div.detail-list > div > p').text.strip().split(' ')[0].strip() if tags_element else "未找到标签"

    # 提取地区信息
    region_element = soup.select_one('div.detail-list > div > div.info-source-duration > div > p')
    region = soup.select_one('div.detail-list > div > div.info-source-duration > div > p').text.strip().split(' ')[0].strip() if region_element else "未找到地区信息"
    
    # 提取评分信息
    score_element = soup.select_one('div.score-block-content > div.score-detail > div > span.rating-num')
    score = float(soup.select_one('div.score-block-content > div.score-detail > div > span.rating-num').text) if score_element else "未找到评分信息"

    return tags, region, score


# 爬取 电影名字 上映时间 票房 平均票价 电影详细信息链接
def get_movie_info(url,headers_dic):

    response_html = (requests.get(url, headers=headers_dic)).text

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response_html, 'lxml')

    # 查找所有电影条目
    movies = soup.select('#ranks-list > ul')

    # 在开始循环前清空文件内容
    with open('猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.txt', 'w', encoding='utf-8') as f:
        pass 
    
    with open('猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        # 写入 CSV 文件的标题行
        csv_writer.writerow(['排名', '电影名', '上映时间', '评分', '票房', '平均票价', '场均人次', '电影标签', '出品地区'])

        num = 0
        # 遍历每个电影条目
        for movie in movies:
            # 提取电影信息
            # 电影标题
            title = movie.select_one('li.col1 > p.first-line').text
            # 上映时间
            time = movie.select_one('li.col1 > p.second-line').text[:10]
            # 票房
            box_office = int(movie.select_one('li.col2.tr').text)
            # 平均票价
            average_box_office = float(movie.select_one('li.col3.tr').text)
            # 场均人次
            average_people = int(movie.select_one('li.col4.tr').text)
            
            # 提取 data-com 属性 - 对应的电影详细介绍链接 # 若无该属性，则返回 '无'
            sublink = movie.get('data-com', '无')[13:-1]
            movie_info_url = str('https://piaofang.maoyan.com'+ sublink)
            tags, region, score = get_tags_region(movie_info_url,headers_dic)

            num += 1
            # 打印爬取信息
            print(f"排名: {num} 电影名: {title} 上映时间: {time} 评分: {score} 票房: {box_office} 平均票价: {average_box_office} 电影标签: {tags} 出品地区: {region}")
            
            # 信息写入文本
            with open('猫眼电影票房榜数据可视化/数据/猫眼电影票房榜数据.txt', 'a', encoding='utf-8') as f:
                f.write(f"排名: {num} 电影名: {title} 上映时间: {time} 评分: {score} 票房: {box_office} 平均票价: {average_box_office} 场均人次: {average_people} 电影标签: {tags} 出品地区: {region}\n")

            # 写入 CSV 文件
            csv_writer.writerow([num, title, time, score, box_office, average_box_office, average_people, tags, region])

    print('爬取完成！')

if __name__ == '__main__':
    url = 'https://piaofang.maoyan.com/rankings/year'
    headers_dic = {
        # 浏览器标识
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'
        }
    get_movie_info(url,headers_dic)