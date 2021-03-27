# xlabel旋转操作
from pyecharts import options as opts
from pyecharts.charts import Bar

c = (Bar()
     .add_xaxis(["名字很长的X轴标签1"
                ,"名字很长的X轴标签2"
                ,"名字很长的X轴标签3"
                ,"名字很长的X轴标签4"
                ,"名字很长的X轴标签5"
                ,"名字很长的X轴标签6"]
                )
     .add_yaxis("商家A", [10, 20, 30, 40, 50, 40])
     .add_yaxis("商家B", [20, 10, 30, 40, 60, 30])
     .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))
                      ,title_opts=opts.TitleOpts(title="Bar-旋转x轴标签", subtitle="解决标签名字过长问题")
                      )
     .render("bar_rotate_xaxis_label.html")
     )