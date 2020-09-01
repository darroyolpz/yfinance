import yfinance as yf
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

# Using API
stock = yf.download("KODK", start="2020-06-01", end=datetime.now())
df = pd.DataFrame(stock)

excel_file = 'Stock.xlsx'
df = pd.read_excel(excel_file)
print(df.head())

'''
df['Close'].plot(figsize=(16, 9))
sns.distplot(df['Volume'])
plt.show()
'''

# Export to Excel
name = 'Stock.xlsx'
writer = pd.ExcelWriter(name)
df.to_excel(writer, index=False)
writer.save()
