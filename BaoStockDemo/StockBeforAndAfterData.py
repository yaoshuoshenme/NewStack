import datetime

import baostock as bs
import pandas as pd

class RaisingStock:
    def __init__(self, code, date):
        self.code = code
        self.date = date


#获取前后七天日期
def date_util(raising_limit_date):
    date_list = []
    # date_list.append()
    l = raising_limit_date.split("/")
    y = int(l[0])
    m = int(l[1])
    d = int(l[2])
    old_date = datetime.datetime(y, m, d)
    date_list.append(old_date.strftime("%Y-%m-%d"))
    before = after = 1;
    beforeCount = afterCount = 0;
    while beforeCount < 7:
        before_date = old_date + datetime.timedelta(days=(0 - before))
        if(before_date.weekday() <= 4):
            date_list.append(before_date.strftime("%Y-%m-%d"))
            beforeCount += 1
        before += 1
    while afterCount < 7:
        after_date = old_date + datetime.timedelta(days=after)
        if (after_date.weekday() <= 4):
            date_list.append(after_date.strftime("%Y-%m-%d"))
            afterCount += 1
        after += 1
    return date_list

def raising_limit_before_after():
    #读取所有涨停数据
    allRaisingStock = pd.read_csv("D:\StockDemo\_allRaisingStock.csv", encoding="utf-8")
    paramList = ['code', 'date']
    for index, row in allRaisingStock.iterrows():
        #获取日期数据
        dateList = date_util(row["date"])
        for d in dateList:
            rs = bs.query_history_k_data_plus(row['code'],"turn",start_date=d, end_date=d, frequency="d", adjustflag="3")
            print(rs.get_row_data(), d, row['tradestatus'])

    # print(allRaisingStock[paramList].convert_objects())
    # for c in allRaisingStock:

bs.login()
raising_limit_before_after()
bs.logout()
