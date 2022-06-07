from model.recession import Recession

def find_recession(df):
    """
    df has 'Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close' columns

    return list of recessions
    """
    local_max = 0
    # Iterate date and find max
    for row_idx in range(len(df.shape[0])):
        local_max = max(df[row_idx]["Close"], local_max)

    # If current close is 10 ~ 20 % lower than max, create recession

    # when the current close is equal or greater than value of recession start, set it as end
    start = datetime.datetime.strptime(row["Date"], "%Y-%m-%d").time()
    Recession(start=start)

    return

def find_crash(df):
    """
    df has 'Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close' columns
    """