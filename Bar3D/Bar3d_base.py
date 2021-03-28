import random

from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.faker import Faker

data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
c = (
    Bar3D(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        "",
        [[d[1], d[0], d[2]] for d in data],
        xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=20),
        title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
    )
    .render("Bar3d_base.html")
)