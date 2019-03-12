import baostock as bs
import pandas as pd


# 读取所有股票代码
def read_all_code():
    single_code_list = []
    allCodes = pd.read_csv('D:\StockDemo\_allStockCode.csv')
    code_list = allCodes["code"].tolist()
    for c in code_list:
        codeSplit = c.split('.')
        if int(codeSplit[1]) > 600000 and codeSplit[0] == 'sh':
            single_code_list.append(c)
    return single_code_list


# 查询所有涨停板
def get_all_raising_limt_stock(codeStr=[]):
    data_list = []
    current = []
    for s in codeStr:
        rs = bs.query_history_k_data_plus(s,
                                          "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                          start_date='2016-01-01', end_date='2019-03-01', frequency="d", adjustflag="3")
        while (rs.error_code == '0') & rs.next():
            current = rs.get_row_data()
            try:
                if current[12] and 9.0 < float(current[12]) < 11.0:
                    data_list.append(current)
            except:
                print("pctChg error, current pctChg is [" + current[12] + "]")
    result = pd.DataFrame(data_list, columns=rs.fields)
    result.to_csv("D:\StockDemo\_allRaisingStock.csv", encoding="utf-8")
    print("ok")

bs.login()
codeStr = read_all_code()
get_all_raising_limt_stock(codeStr)
bs.logout()