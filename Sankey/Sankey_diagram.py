import asyncio
from aiohttp import TCPConnector, ClientSession

import pyecharts.options as opts
from pyecharts.charts import Sankey

async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()


# 获取官方的数据
data = asyncio.run(
    get_json_data(url="https://echarts.apache.org/examples/data/asset/data/energy.json")
)

(
    Sankey(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        nodes=data["nodes"],
        links=data["links"],
        itemstyle_opts=opts.ItemStyleOpts(border_width=1, border_color="#aaa"),
        linestyle_opt=opts.LineStyleOpts(color="source", curve=0.5, opacity=0.5),
        tooltip_opts=opts.TooltipOpts(trigger_on="mousemove"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Sankey Diagram"))
    .render("Sankey_diagram.html")
)