from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker

c = (
    EffectScatter()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        series_name="",
        y_axis=Faker.values()
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="EffectScatter-基本示例")
    )
    .render("Effectscatter_base.html")
)