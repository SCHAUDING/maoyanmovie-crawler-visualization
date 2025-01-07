import os
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

# 数据准备
movies = [('长津湖', 577534), ('战狼2', 569454), ('你好，李焕英', 541320), ('哪吒之魔童降世', 503570), ('流浪地球', 468739), ('满江红', 454435), ('唐人街探案3', 452356), ('复仇者联盟4', 425015), ('长津湖之水门桥', 406745), ('流浪地球2', 404375)]

# 提取电影名和票房数据
movie_names, box_office = zip(*movies)

# 创建Bar实例
bar = Bar()

# 添加X轴数据
bar.add_xaxis(movie_names)

# 添加Y轴数据，并设置颜色渐变和数据标签
bar.add_yaxis(
    "票房（单位：万）",
    box_office,
    label_opts=opts.LabelOpts(is_show=True, position="top", formatter=JsCode("function(params){return params.value[1];}")),
    itemstyle_opts=opts.ItemStyleOpts(
        color=JsCode(
            "function(params) {"
            "var colorList = ['#5470C6', '#91CC75', '#EE6666', '#73C0DE', '#3BA272', '#FC846B', '#9A60B4', '#EA7CCC'];"
            "return colorList[params.dataIndex % colorList.length];"
            "}"
        )
    )
)

# 设置全局配置
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title="票房最高的电影排名",
        pos_left="center",  # 水平居中
        pos_top="10px"  # 顶部对齐
    ),
    xaxis_opts=opts.AxisOpts(
        name="电影名",
        axislabel_opts=opts.LabelOpts(rotate=-45)  # 设置标签旋转角度为-45度，负值表示逆时针旋转
    ),
    yaxis_opts=opts.AxisOpts(name="票房(单位:万)"),
    legend_opts=opts.LegendOpts(
        pos_right="10%",
        pos_top="10px")  # 设置图例居右
)

# 设置图表宽度为100%
bar.width = "100%"
bar.height="550px"

# 设置目标路径
output_path = '猫眼电影票房榜数据可视化/数据可视化图表/电影票房榜前10柱状图.html'

# 渲染到HTML文件
bar.render(output_path)