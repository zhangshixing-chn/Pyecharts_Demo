from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-显示Toolbox"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .render("Bar_toolbox.html")
)