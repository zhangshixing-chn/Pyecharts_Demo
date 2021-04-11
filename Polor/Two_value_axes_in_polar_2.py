import math
import pyecharts.options as opts
from pyecharts.charts import Polar

data = []

for i in range(0, 360 + 1):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])

(
    Polar(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="line",
        data=data,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=0,
    )
    .add_schema(
        angleaxis_opts=opts.AngleAxisOpts(
            start_angle=0, type_="value", is_clockwise=True
        ),
        radiusaxis_opts=opts.RadiusAxisOpts(min_=0),
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        title_opts=opts.TitleOpts(title="极坐标双数值轴"),
    )
    .render("Two_value_axes_in_polar_2.html")
)