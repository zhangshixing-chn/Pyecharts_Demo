from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType

c = (
    Liquid()
    .add(
        "lq",
        [0.3, 0.7],
        is_outline_show=False,
        shape=SymbolType.DIAMOND
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Lquid-Shape-Dimond")
    )
    .render("Liquid_shape_dimond.html")
)