%pyspark
from pyspark.sql.types import *
from pyspark.sql import SQLContext
import pandas as pd
df = pd.read_csv("/tmp/data_result.csv")

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
test = sqlCtx.createDataFrame(df)
test.createOrReplaceTempView("rvwccc")
"""
%sql
create table temp.woojin_test_table_0917 as ( --ds_temp
select *
from rvwccc
)
"""