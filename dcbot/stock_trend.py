import yfinance as yf
import matplotlib.pyplot as plt

def search_ticker(ticker: str):
    """
    搜尋股票代碼的公司資訊。
    """
    stock = yf.Ticker(ticker)
    info = stock.info
    return info

def plot_stock_trend(ticker: str, start_date: str, end_date: str):
    """
    根據給定的股票代碼(ticker)和日期範圍，繪製股票的收盤價走勢圖。

    :ticker: 股票 (例如: 'AAPL')
    :start_date: 開始日期 (例如: '2024-01-01')
    :end_date: 結束日期 (例如: '2024-12-01')
    """
    ticker_info = search_ticker(ticker)
    ticker_symbol = ticker_info.get("symbol")
    company_name = ticker_info.get("longName")
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    if stock_data.empty:
        print(f"無法獲取 {ticker} 的數據")
        return
    
    # 繪製折線圖
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label=f'{company_name} Stock Price', color='blue')
    plt.title(f'{company_name} Stock Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=20)
    plt.show()

plot_stock_trend('2330.TW', '2023-01-16', '2024-12-16')