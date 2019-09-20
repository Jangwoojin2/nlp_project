import pandas as pd
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
 
#pandas dataframe인 경우
df = pd.read_excel("/tmp/all_feature_test_0701_10000.xlsx")
#engine 생성 (hive 인경우 presto 대신 hive)
engine = create_engine('presto://presto.david2.ds.woowa.in:12304/hive/temp') #temp 스키마에 생성 됨(공용 제플린과 접근 가능)
#
df[['review_cont', 'label', 'max_probaility']].to_sql(name="table_name", #생성하고자 하는 테이블 명
                                                      con=engine, index=false, if_exists='replace', #replace면 덮어쓰기
                                                      index_label='idx', chunksize=1000)