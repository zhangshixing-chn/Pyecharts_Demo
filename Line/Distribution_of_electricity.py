import pyecharts.options as opts
from pyecharts.charts import Line


x_data = [
    "00:00",
    "01:15",
    "02:30",
    "03:45",
    "05:00",
    "06:15",
    "07:30",
    "08:45",
    "10:00",
    "11:15",
    "12:30",
    "13:45",
    "15:00",
    "16:15",
    "17:30",
    "18:45",
    "20:00",
    "21:15",
    "22:30",
    "23:45",
]
y_data = [
    300,
    280,
    250,
    260,
    270,
    300,
    550,
    500,
    400,
    390,
    380,
    390,
    400,
    500,
    600,
    750,
    800,
    700,
    600,
    400,
]

(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="用电量",
        y_axis=y_data,
        is_smooth=True,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="一天用电量分布", subtitle="纯属虚构"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        xaxis_opts=opts.AxisOpts(boundary_gap=False),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} W"),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            dimension=0,
            pieces=[
                {"lte": 6, "color": "green"},
                {"gt": 6, "lte": 8, "color": "red"},
                {"gt": 8, "lte": 14, "color": "green"},
                {"gt": 14, "lte": 17, "color": "red"},
                {"gt": 17, "color": "green"},
            ],
        ),
    )
    .set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            data=[
                opts.MarkAreaItem(name="早高峰", x=("07:30", "10:00")),
                opts.MarkAreaItem(name="晚高峰", x=("17:30", "21:15")),
            ]
        )
    )
    .render("Distribution_of_electricity.html")
)