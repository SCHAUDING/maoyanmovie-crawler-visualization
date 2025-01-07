from pyecharts import options
from pyecharts.charts import Line

line = Line()
line.add_xaxis(['1998','2009', '2010', '2011', '2012', '2013', '2015', '2016', '2017', '2018', '2019', '2020', '2021','2022','2023','2024'])
line.add_yaxis(
    '销售额',
    [136531, 58444, 349841, 281476, 517145, 680945, 1342097, 2847612, 2771087, 3956214, 4404346, 4725760, 1464819, 3305145, 2186504, 4309879, 2415244]
)
line.set_global_opts(
    # 设置图标标题
    title_opts=options.TitleOpts(
        title='各年各电影总票房合折线图',
        pos_left='center',
        pos_top="10px"  # 顶部对齐

    ),
    # 设置图例
    legend_opts=options.LegendOpts(
        is_show=False
    ),
    yaxis_opts=options.AxisOpts(name="票房(单位:万)"),
    xaxis_opts=options.AxisOpts(name="年份"),
)
line.set_series_opts(
    markline_opts=options.MarkLineOpts(
        data=[options.MarkLineItem(name='平均线', type_='average')]
    )
)


# 设置图表宽度为100%
line.width = "100%"
line.height="550px"
line.render('猫眼电影票房榜数据可视化/数据可视化图表/各年各电影票房总合折线图.html')