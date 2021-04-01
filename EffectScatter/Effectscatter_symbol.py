from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType

c = (
    EffectScatter()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        series_name="",
        y_axis=Faker.values(),
        symbol=SymbolType.DIAMOND
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="EffectScatter-不同Symbol")
    )
    .render("EffectScatter_symbol.html")
)