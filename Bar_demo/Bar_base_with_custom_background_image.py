from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker

c = (
    Bar(
        init_opts=opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"}
        )
    )
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Bar-背景图基本示例",
            subtitle="我是副标题",
            title_textstyle_opts=opts.TextStyleOpts(color="white"),
        )
    )
)
c.add_js_funcs()

c.render("bar_base_with_custom_background_image.html")