#coding=utf-8
import tushare as ts
import mysqlConnect 
from sqlalchemy import create_engine
"""
df = ts.get_hist_data('600489')
df.to_csv('J:/work/data/600489.csv')
"""
"""
df = ts.get_tick_data('600489', date='2016-07-10')
engine = mysqlConnect.get_engine()
df.to_sql('aaa',engine)"""

"""df = ts.get_hist_data('600489', date='2016-07-10')"""
"""df = ts.get_tick_data('600489', date='2016-7-6')"""
"""df =ts.get_hist_data('600848','2016-07-06','2016-07-11')"""
"""df =ts.get_realtime_quotes('600489')"""

df = ts.get_hist_data('600489', start='2016-03-10')
df.to_json('J:/work/data/600489_2016-03-10.json')
print df
"""df.to_json('J:/work/data/600489RealTime.json')"""

