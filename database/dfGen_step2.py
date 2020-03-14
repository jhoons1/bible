import pandas_access as mdb
import pandas as pd

# Listing the tables.
for tbl in mdb.list_tables("./bible.mdb"):
    print(tbl)
    df = mdb.read_table("./bible.mdb", tbl)
    df.to_pickle('./'+tbl+'.pkl')
