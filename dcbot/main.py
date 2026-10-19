import discord
<<<<<<< Updated upstream
import artbot#call artbot.py

# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

# 調用event函式庫
@client.event
# 當機器人完成啟動
=======
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import urllib.parse
import tokenfile
from showstock import gettopstock
from forex_python.converter import CurrencyRates
import twder 
#from stock_trend import plot_stock_trend
from stock_trend_origin import plot_stock_trend
import matplotlib.pyplot as plt
from currency_converter import convert_currency, get_error_message
from stock_search import search_stock, format_stock_results
from bot_help import get_help_message
import os  # 加入這個 import
from datetime import datetime, timedelta, date

# intents 是要求機器人的權限
intents = discord.Intents.all()
# command_prefix 是前綴符號，可以自由選擇 ($, #, &...)
bot = commands.Bot(command_prefix="%", intents=intents)
now_date = datetime.now()
now_date = now_date.strftime("%Y-%m-%d")
# 匯率查詢初始化
currency_rates = CurrencyRates()
@bot.event
>>>>>>> Stashed changes
async def on_ready():
    print(f"目前登入身份 --> {client.user}")

<<<<<<< Updated upstream
@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
=======
@bot.command()
async def helps(ctx):
    """列出機器人的指令清單"""
    await ctx.send(get_help_message())

@bot.command()
async def load(ctx, extension):
    """加載指定的擴展模組"""
    try:
        await bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"模組 `{extension}` 加載完成!")
    except Exception as e:
        await ctx.send(f"無法加載模組 `{extension}`: {e}")

@bot.command()
async def today(ctx, count: int = 10):
    """獲取今日熱門股票，預設顯示 10 個"""
    try:
        if count > 50:
            await ctx.send("請輸入小於等於 50 的數量！")
            return
        await ctx.send(f"今日熱門的前 {count} 支股票")
        stocks = gettopstock(count)
        response = f"今日熱門前 {len(stocks)} 支股票：\n"
        for stock in stocks:
            name, price, change, change_percent = stock
            response += f"股票名: {name} | 成交價: {price} | 漲跌: {change} | 漲跌%: {change_percent}\n"
        print(type(stocks))
            
        
        await ctx.send(response)
        
    except Exception as e:
        await ctx.send(f"發生錯誤：{str(e)}")

@bot.command()
async def getstock(ctx, *, stock_name: str = None):
    """搜尋股票相關資訊"""
    results, error = search_stock(stock_name)
    
    if error:
        await ctx.send(error)
>>>>>>> Stashed changes
        return
<<<<<<< Updated upstream
    # 新訊息包含Hello，回覆Hello, world!
    if message.content == "Hello":
        await message.channel.send("Hello, world!")
=======
        
    if results:
        await ctx.send(format_stock_results(stock_name, results))
    else:
        await ctx.send(f"找不到 `{stock_name}` 的相關資訊")
@bot.command()
async def currency(ctx, from_currency: str, to_currency: str, amount: float):
    """匯率轉換指令"""
    try:
        result = convert_currency(from_currency, to_currency, amount)
        if result['success']:
            await ctx.send(
                f"匯率換算結果：\n"
                f"{result['from_amount']:,.2f} {result['from_currency']} = "
                f"{result['to_amount']:,.2f} {result['to_currency']}\n"
                f"當前匯率：1 {result['from_currency']} = {result['rate']:,.4f} {result['to_currency']}"
            )
        else:
            await ctx.send(get_error_message())
            
    except Exception as e:
        await ctx.send(f"轉換過程中發生錯誤: {str(e)}")

'''@bot.command()
async def trend(ctx, ticker: str, start_date: str = None, end_date: str = None):
    """查看股票走勢圖"""
    try:
        if not start_date:
            start_date = '2024-01-01'
        if not end_date:
            end_date = '2024-12-31'
        
        # 等待訊息
        await ctx.send(f"正在獲取 {ticker} 的股票走勢圖")
        
        # 繪製圖表
        success = plot_stock_trend(ticker, start_date, end_date)
        
        if success:
            # 發送圖片
            await ctx.send(file=discord.File('stock_trend.png'))
            # 發送完成後刪除圖片
            os.remove('stock_trend.png')
        else:
            await ctx.send(f"無法獲取 {ticker} 的走勢圖")
            
    except Exception as e:
        await ctx.send(f"獲取股票走勢圖時發生錯誤：{str(e)}")
        # 如果發生錯誤，也要確保圖片被刪除
        if os.path.exists('stock_trend.png'):
            os.remove('stock_trend.png')
'''

now_date = datetime.now()
now_y = int(now_date.strftime("%Y"))
now_m = int(now_date.strftime("%m"))
now_d = int(now_date.strftime("%d"))
now_date = now_date.strftime("%Y-%m-%d")
custom_date = date(now_y, now_m, now_d)
@bot.command()
async def trend(ctx, ticker: str, scope: str):
    ''' 輸入格式 trend <股票代碼> <範圍:可輸入 week, month, year>'''
    new_date = custom_date
    match scope:
        case "week":
            new_date -= timedelta(days=7)
        case "month":
            new_date -= timedelta(days=30)
        case "year":
            new_date -= timedelta(days=365)
    plot_stock_trend(ticker, new_date, now_date)
    


@bot.event
async def on_member_join(member):
    """當新成員加入伺服器時觸發"""
    try:
        # 發送歡迎訊息和指令說明
        welcome_message = (
            f"歡迎 {member.mention} 加入伺服器！\n"
        )
        
        # 從 bot_help.py 獲取指令說明
        help_message = get_help_message()
        
        # 找到一個適合發送訊息的頻道
        # 可以是指定的歡迎頻道或是一般聊天頻道
        default_channel = member.guild.system_channel  # 系統訊息頻道
        
        if default_channel:
            await default_channel.send(welcome_message + help_message)
        
    except Exception as e:
        print(f"發送歡迎訊息時發生錯誤：{str(e)}")

if __name__ == "__main__":
    # 從 tokenfile 中讀取機器人的 Token
    bot.run(tokenfile.token)
>>>>>>> Stashed changes

artbot.bot.run('YOUR_DISCORD_BOT_TOKEN')#run artbot's function