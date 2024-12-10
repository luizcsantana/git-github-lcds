# %%
import pandas as pd
import pyreaddbc
from dbfread import DBF
import pyarrow
# %%
pyreaddbc.dbc2dbf("data/rd/dbc/RDTO2301.dbc",
                  outfile="data/rd/dbf/RDTO2301.dbf")
# %%
dbf = DBF("data/rd/dbf/RDTO2301.dbf")
# %%
df = pd.DataFrame(iter(dbf))
# %%
df.to_csv("data/rd/csv/RDTO2301.csv", sep=";", index=False)
# %%
# %%
df.to_parquet("data/rd/parquet/RDTO2301.parquet", index=False)
