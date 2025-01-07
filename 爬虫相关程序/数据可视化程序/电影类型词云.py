from pyecharts.charts import WordCloud
from pyecharts import options
from pyecharts.charts.basic_charts import wordcloud


wc = WordCloud()
wc.add('电影类型',[('动作', 147), ('剧情', 110), ('冒险', 94), ('喜剧', 88), ('科幻', 64), ('奇幻', 44), ('爱情', 43), ('犯罪', 33), ('动画', 30), ('悬疑', 23), ('惊悚', 17), ('战争', 15), ('历 史', 10), ('灾难', 9), ('家庭', 9), ('古装', 7), ('青春', 6), ('传记', 4), ('谍战', 2), ('武侠', 2), ('神话', 1), ('史诗', 1), ('运动', 1), ('音乐', 1), ('热血', 1), ('西部', 1), ('歌舞', 1), ('校园', 1)],
       shape='star'
       )


wc.set_global_opts(
    title_opts=options.TitleOpts(
        title='电影标签词云',
        pos_left='center',
        pos_top="10px"
    ),
    legend_opts=options.LegendOpts(
        is_show=False
    ),
),
# 设置图表宽度为100%
wc.width = "100%"
wc.height="550px"
wc.render('猫眼电影票房榜数据可视化/数据可视化图表/电影类型词云.html')