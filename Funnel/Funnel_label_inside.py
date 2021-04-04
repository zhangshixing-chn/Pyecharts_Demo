from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Funnel

c = (
    Funnel()
    .add(
        "商品",
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        label_opts=opts.LabelOpts(position='inside')
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Funel-Label (inside)"))
    .render("Funnel_label_inside.html")
)