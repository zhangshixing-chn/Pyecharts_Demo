from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge(init_opts=opts.InitOpts(width="1200px", height="600px"))
    .add(
        series_name="业务指标",
        data_pair=[['完成率', 55.5]]
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%")
    )
    .set_series_opts(
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[[0.3, "#67e0e3"], [0.7, "#37a2da"], [1, "#fd666d"]], width=30
            )
        )
    )
    .render("Gauge_change_color.html")
)