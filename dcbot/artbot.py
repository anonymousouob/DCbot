import discord
# 導入commands指令模組
from discord.ext import commands
from googlesearch import search
from bs4 import BeautifulSoup

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "%", intents = intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

    #也可以利用指令, 更改機器人目前在玩的遊戲
    game = discord.Game('Visual Studio Code')
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.command()
# 輸入%Hello呼叫指令
async def Hello(ctx):
    # 回覆Hello, world!
    await ctx.send("Hello, world!")

@bot.command()
async def getstock(ctx):#type %getstock to get coommand
    await ctx.send("https://www.google.com/finance/quote/IX0001:TPE?sa=X&sqi=2&ved=2ahUKEwinkOyaquqJAxVqnq8BHV55EnsQ3ecFegQINhAf")

@bot.command()
async def Help(ctx):
    await ctx.send(" %Hello -> input 'Hello' to get response 'Hello, world!'")
    await ctx.send(" %getstock -> input 'getstock' to get stock news")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")


@bot.command()
async def google(ctx, *, query: str):
    """在 Google 搜尋並回傳前幾個結果"""
    await ctx.send(f"🔍 正在搜尋: `{query}`")
    try:
        results = search(query, num_results=5)  # 搜尋前 5 個結果
        if results:
            response = "\n".join([f"{i+1}. {result}" for i, result in enumerate(results)])
            await ctx.send(f"以下是搜尋結果：\n{response}")
        else:
            await ctx.send("抱歉，找不到相關結果！")
    except:
        await ctx.send("發生錯誤")

if __name__ == "__main__":
    bot.run("YOUR_DISCORD_BOT_TOKEN")