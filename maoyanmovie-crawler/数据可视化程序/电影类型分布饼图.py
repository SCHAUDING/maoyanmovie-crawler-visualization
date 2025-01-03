from pyecharts.charts import Pie
from pyecharts import options

p = Pie()
p.add(
    '电影类别占比',
    [('动作', 147), ('剧情', 110), ('冒险', 94), ('喜剧', 88), ('科幻', 64), ('奇幻', 44), ('爱情', 43), ('犯罪', 33), ('动画', 30), ('悬疑', 23), ('惊悚', 17), ('战争', 15), ('历 史', 10), ('灾难', 9), ('家庭', 9), ('古装', 7), ('青春', 6), ('传记', 4), ('谍战', 2), ('武侠', 2), ('神话', 1), ('史诗', 1), ('运动', 1), ('音乐', 1), ('热血', 1), ('西部', 1), ('歌舞', 1), ('校园', 1)],
    rosetype="radius",
    radius=['30%','70%'],
    # center=['%','55%']
)

p.set_global_opts(
    title_opts=options.TitleOpts(
        title='电影类别占比',
        pos_left='center',
        pos_top="10px"  # 顶部对齐
    ),
    legend_opts=options.LegendOpts(
        is_show=False
    ),
)
# 设置数据标志的格式
p.set_series_opts(
    label_opts=options.LabelOpts(
        formatter='{b}:{d}%'
    ),

)
# 设置图表宽度为100%
p.width = "100%"
p.height="550px"
p.render('猫眼电影票房榜数据可视化/数据可视化图表/电影类型分布饼图.html')