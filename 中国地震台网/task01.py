# -*- coding: utf-8 -*-
# @Time : 2022/5/3 19:24
# @Author : 逍遥哥哥每天都要努力啊！
# @File : task01.py
import pandas as pd
import numpy as np
import operator as op
data = pd.read_csv("data/中国地质网.csv")
# 数据清洗
# 数据清洗过程包括:缺失数据处理，数据类型转换，数据排序，异常值处理
#处理缺失值
shape = data.shape
# (10201, 6)
data1 = data.dropna()
shape1 = data1.shape
# (10201, 6)
# @ 统计NaN个数
x = data.isnull().sum().sum()
# @ 第一次sum()算出各个列有几个,第二次算出全部
# print('共有NaN:', x)
# @ 统计重复行个数 #重复行有100行，地区一样时间经纬度不同
x = data.duplicated().sum()
# print('共有重复行:', x)
#数据类型转换
data1["震级M"]=pd.to_numeric(data1["震级M"],errors="coerce")
data1["纬度(°)"]=pd.to_numeric(data1["纬度(°)"],errors="coerce")
data1["经度(°)"]=pd.to_numeric(data1["经度(°)"],errors="coerce")
data1["深度(KM)"]=pd.to_numeric(data1["深度(KM)"],errors="coerce")
def getdate(times):
    dateList = []  # 接受处理后的日期
    for i in times:
        dateList.append(i.split(" ")[0])  # 通过for循环，将销售时间传入list
    datetime = pd.Series(dateList)  # 将list转换成Series
    return datetime
data1.loc[:, "发震时刻(UTC+8)"] = getdate(data1.loc[:, "发震时刻(UTC+8)"])  # 调用getdate函数,处理销售时间
# 转换日期数据时将不能转换的数据转换为nan
data1["发震时刻(UTC+8)"] = pd.to_datetime(data1["发震时刻(UTC+8)"], errors='coerce')
def getarea(area):
    areaList = []
    li = ["新疆", "甘肃", "四川", "西藏", "青海", "云南","内蒙古","日本","台湾","广东"]
    for i in area.astype(str):
        contains=False
        for elem in li:
            if i.startswith(elem):
                areaList.append(elem)
                contains = True
                break
        if not contains:
            areaList.append(i)
    areaList = pd.Series(areaList)
    return areaList
data1["参考位置"] = getarea(data1["参考位置"])
#前十多发地区
topeare=data1.groupby("参考位置").count().sort_values(ascending=False,by="震级M").reset_index().head(10)

#2012-5-11 --2022-5-3 每年每月每天
time1=data1.groupby("发震时刻(UTC+8)").count().sort_values(ascending=False,by="震级M").reset_index()
yeartop=time1.groupby(time1["发震时刻(UTC+8)"].dt.year).sum().sort_values(ascending=False,by="震级M").reset_index()
monthtop=time1.groupby(time1["发震时刻(UTC+8)"].dt.month).sum().sort_values(ascending=False,by="震级M").reset_index()
daytop=time1.groupby(time1["发震时刻(UTC+8)"].dt.day).sum().sort_values(ascending=False,by="震级M").reset_index()
#选取其中两列,分别是经度纬度
jw=data1[["纬度(°)","经度(°)"]].values.tolist()
print(jw)