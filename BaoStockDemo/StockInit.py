import baostock as bs
import pandas as pd


#获取所有证券信息
def getAllStockCode():
    rs = bs.query_all_stock(day="2019-03-01")
    data_list = []
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    result.to_csv("D:\StockDemo\_allStockCode.csv", encoding="utf-8")

bs.login()
getAllStockCode()
print("All code have download")
bs.logout()