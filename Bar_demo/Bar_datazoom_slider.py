from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.faker import Faker

c = (Bar()
     .add_xaxis(Faker.days_attrs)
     .add_yaxis("商家A", Faker.days_values)
     .set_global_opts(title_opts=opts.TitleOpts(title="Bar_DataZoom(silder-水平)"),
                      datazoom_opts=opts.DataZoomOpts())
     .render("Bar_datazoom_slider.html")
     )