from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-Markpoint(指定类型)"))
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name='最小值'),
                opts.MarkPointItem(type_='average', name="平均值")
            ]
        )
    )
    .render("Bar_markpoint_type.html")
)