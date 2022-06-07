from util import stock_data, stock_graph
from algo.recession import find_recession

from datetime import datetime

ticker = "SPY"
start_date = "2020-01-01"
end_date = datetime.now().strftime("%Y-%m-%d")


data = stock_data.get(ticker=ticker, start_date=start_date, end_date=end_date)
print(data.columns)

recession_list = find_recession(data)

stock_graph.show(data)

# print(data.head())