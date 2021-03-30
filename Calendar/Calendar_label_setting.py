import random
import datetime

from pyecharts import options as opts
from pyecharts.charts import Calendar

begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)

data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)] for i in range((end-begin).days + 1)
]

c = (
    Calendar(init_opts=opts.InitOpts(width="1000px", height="500px"))
    .add(
        series_name="",
        yaxis_data=data,
        calendar_opts=opts.CalendarOpts(
            range_="2017",
            daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
            monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn")
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况(中文 Label)"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000,
            min_=500,
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="100px",
        ),
    )
    .render("Calendar_label_setting.html")
)