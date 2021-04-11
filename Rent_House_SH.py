#!/usr/bin/env python
# coding: utf-8
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

# 二手房市场参数
sh_url_dict = {'浦东新区':"https://sh.lianjia.com/ershoufang/pudong/pg",
               '闵行':"https://sh.lianjia.com/ershoufang/minhang/pg",
               '宝山':"https://sh.lianjia.com/ershoufang/baoshan/pg",
               '徐汇':"https://sh.lianjia.com/ershoufang/xuhui/pg",
               '普陀':"https://sh.lianjia.com/ershoufang/putuo/pg",
               '杨浦':"https://sh.lianjia.com/ershoufang/yangpu/pg",
               '长宁':"https://sh.lianjia.com/ershoufang/changning/pg",
               '松江':"https://sh.lianjia.com/ershoufang/songjiang/pg",
               '嘉定':"https://sh.lianjia.com/ershoufang/jiading/pg",
               '黄浦':"https://sh.lianjia.com/ershoufang/huangpu/pg",
               '静安':"https://sh.lianjia.com/ershoufang/jingan/pg",
               '虹口':"https://sh.lianjia.com/ershoufang/hongkou/pg",
               '青浦':"https://sh.lianjia.com/ershoufang/qingpu/pg"}

sh_page_dit = {'浦东新区':"100",
               '闵行':"100",
               '宝山':"96",
               '徐汇':"63",
               '普陀':"58",
               '杨浦':"57",
               '长宁':"45",
               '松江':"57",
               '嘉定':"45",
               '黄浦':"19",
               '静安':"56",
               '虹口':"26",
               '青浦':"28"}

sh_area_list = ['浦东新区','闵行','宝山','徐汇','普陀','杨浦','长宁','松江','嘉定','黄浦','静安','虹口','青浦']

# 获取所有内容的url列表
def Get_pages_url(area_name):
    
    print('获取{}板块的所有页面url.'.format(area_name), datetime.datetime.now())
    area_url = sh_url_dict[area_name]
    page_num = sh_page_dit[area_name]

    Urls_all = []
    for i in range(1, int(page_num)+1):
        Urls_all.append(area_url + str(i))
    
    return Urls_all


# 对每个页面开始爬取需要的字段
def acc_page_msg(page_url):
    
    # 解析数据文件
    web_data = requests.get(page_url).content.decode('utf8')
    soup = BeautifulSoup(web_data, 'html.parser')
    
    # 开始获取小区名字及地址
    position_info = []
    for tag in soup.find_all(attrs='positionInfo'):
        for em in tag:
            for a in em:
                position_info.append(a)

    new_postion_info = []           
    for val in position_info:
        if (val != " ") and (val != '-'):
            new_postion_info.append(val)

    name = []
    loc = []
    for i, val in enumerate(new_postion_info):
        if i % 2 == 0:
            name.append(val)
        else:
            loc.append(val)
            
    # 获取房子的详细信息
    house_info = []
    for tag in soup.find_all(attrs='houseInfo'):
        for em in tag:
            house_info.append(em)

    house_data = []           
    for i, val in enumerate(house_info):
        if i % 2 == 0:
            pass
        else:
            house_data.append(val)
            
    # 获取关注信息
    follow_info = []
    for tag in soup.find_all(attrs='followInfo'):
        for em in tag:
            follow_info.append(em)

    follow_data = []
    for i, val in enumerate(follow_info):
        if i % 2 == 0:
            pass
        else:
            follow_data.append(val)
            
    # 获取价格
    price_info = []
    for tag in soup.find_all(attrs='priceInfo'):
        for em in tag:
            for a in em:
                for i in a:
                    if i == '万':
                        pass
                    else:
                        price_info.append(i)

    price_data = []
    unitprice_data = []
    for i, val in enumerate(price_info):
        if i % 2 == 0:
            price_data.append(val)
        else:
            unitprice_data.append(val)
            
    return name, loc, house_data, follow_data, price_data, unitprice_data


# 开始运行程序
if __name__ == '__main__':
    
#     sh_area_list = ['黄浦', '虹口']
    All_data = pd.DataFrame()
    
    for area_name in sh_area_list:
        urls = Get_pages_url(area_name)
        count = 0
        print('需要爬取的url个数为:', len(urls))

        Area_Name = []
        Area_Loc = []
        Area_House_data = []
        Area_Follow_data = []
        Area_Price_data = []
        Area_Unitprice_data = []

        for url in urls:
            count += 1
            print('开始爬取第{}个页面.'.format(count), end='\r')
            name, loc, house_data, follow_data, price_data, unitprice_data = acc_page_msg(url)
            Area_Name.extend(name)
            Area_Loc.extend(loc)
            Area_House_data.extend(house_data)
            Area_Follow_data.extend(follow_data)
            Area_Price_data.extend(price_data)
            Area_Unitprice_data.extend(unitprice_data)
        
        print('完成页面的爬取.', datetime.datetime.now())

        Area_Data = pd.DataFrame()
        Area_Data['Name'] = Area_Name
        Area_Data['Loc'] = Area_Loc
        Area_Data['Hous_data'] = Area_House_data
        Area_Data['Follow_data'] = Area_Follow_data
        Area_Data['Price'] = Area_Price_data
        Area_Data['UnitPrice'] = Area_Unitprice_data
        Area_Data['Area'] = area_name
        
        All_data = pd.concat([All_data, Area_Data], axis=0)

    All_data.to_csv('上海二手房数据.csv', index=False, header=True, encoding='utf-8-sig')
