from pyecharts import options as opts
from pyecharts.charts import Map

# 创建地图对象
map = Map(init_opts=opts.InitOpts(width="100%", height="550px"))  # 设置画布大小为全屏

# 添加数据
map.add(
    series_name="电影发行地区地图",
    data_pair=[
        ('China', 228),
        ('United States', 97),
        ('Japan', 6),
        ('Australia', 1),
        ('United Arab Emirates', 1),
        ('Czech Republic', 1),
        ('Russia', 1),
        ('India', 1),
        ('United Kingdom', 1),
        ('加拿大', 4)
    ],
    maptype="world",
    zoom=1,  # 设置地图默认缩放级别
    is_map_symbol_show=False,  # 不显示地图标记
    label_opts=opts.LabelOpts(is_show=False)  # 不显示国家名称
)

# 设置全局配置
map.set_global_opts(
    title_opts=opts.TitleOpts(
        title="电影发行地区地图",
        pos_left="center",  # 标题居中
        pos_top="10px"  # 顶部对齐
    ),
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        max_=250,
        min_=1,
        is_piecewise=False,  # 是否分段显示
        pos_left="10%",  # 将色谱条放置在左侧
        pos_top="middle",  # 将色谱条放置在中间
    ),
    legend_opts=opts.LegendOpts(is_show=False),  # 不显示图例
)



# 渲染为 HTML 文件
map.render("猫眼电影票房榜数据可视化/数据可视化图表/电影发行地区地图.html")