import plotly.graph_objects as go



# def get_stock_data()
# def show_stock_graph(stock):
#     data = pdr.get_data_yahoo('NVDA')
#     # Display Info
#     print(data.info())



def show(df, recessions=[]):
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])

    # if len(recessions) > 0:
    #     for recession in recessions:
    #         fig.add_trace(
    #             go.Scatter(
    #                 x=df["trace_x"],
    #                 y=df["trace_y"],
    #                 mode="markers+lines",
    #                 name="steepest",
    #                 line=dict(
    #                     color="black"
    #                 )
    #             )
    #         )

    fig.show()