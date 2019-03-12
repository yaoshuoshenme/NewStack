import baostock as bs
import pandas as pd

lg = bs.login()
#显示登录信息
print('login respond error_code:' + lg.error_code)
print('login respond error_msg:' + lg.error_msg)

#获取历史k线数据
rs = bs.query_history_k_data_plus("sh.600000",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    start_date='2017-06-01', end_date='2019-2-28',
    frequency="d", adjustflag="3")
#显示信息
print('login respond error_code:' + rs.error_code)
print('login respond error_msg:' + rs.error_msg)

#打印结果集
data_list=[]
while(rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并到一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
#结果集输出到csv文件
result.to_csv("D:\gupiaoshuju\history_k_data.csv", encoding="gbk", index=False)
print(result)

#登出
bs.logout()
