import os
import random
# Pycordを読み込む
import discord
import dotenv
import requests

# アクセストークンを設定
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

# 天気
appid = str(os.getenv("APPID"))
url = "https://map.yahooapis.jp/weather/V1/place?coordinates=135.325592,34.374519&appid=" + appid + "&output=json"

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot入門"),  # "〇〇をプレイ中"の"〇〇"を設定,
)

snsUrl =    ["www.youtube.com/shorts/",
            "https://x.com/",
            "https://www.instagram.com/",
            "https://twitter.com/",
            "https://www.tiktok.com/",]


# 起動時に自動的に動くメソッド
@bot.event
async def on_ready():
    # 起動すると、実行したターミナルに"Hello!"と表示される
    print("Hello!")

# Botが見える場所でメッセージが投稿された時に動くメソッド
@bot.event
async def on_message(message: discord.Message):
    # メッセージ送信者がBot(自分を含む)だった場合は無視する
    if message.author.bot:
        return

    # メッセージが"hello"だった場合、"Hello!"と返信する
    if message.content == 'hello':
        await message.reply("Hello!")
    
    if message.content == 'ez':
        await message.reply("ナイスゲーム！みんなこれからも頑張ってね！")

    if message.content == 'lol':
        await message.reply("うん、やっぱ楽しくプレイすることが何よりも大事だよね")
        
    for i in snsUrl:
        if i in message.content:
            result = "これ凄いな。。。"
            word = [
                'まるで未来から来たみたい！',
                'こんなの初めて見たよ。',
                '想像以上のものだね。',
                '技術の進化は本当に驚くべきだ。',
                'これは革命的だ！',
                'さすがにこれは感動する。',
                'これは一体どうやって作られたの？',
                'これを使えば、色々と変わるかもしれないね。',
                '想像を遥かに超えている。',
                'これは記憶に残る体験だ。'
            ]
            result += word[random.randint(0, len(word) - 1)]
            await message.reply(result)
    # オウム返し
    try:
        # await message.channel.send(message.content)
        print(message.content)
    except:
        await message.channel.send("なんかエラー出たわ")

# helpコマンドを実装
@bot.command(name="help", description="機能一覧を表示します")
async def help(ctx: discord.ApplicationContext):
    await ctx.respond(f"/help : 機能一覧を表示します\n/ping : pingを返します。疎通確認ヨシ！\n/greeting User : 挨拶しましょう！Hi!\n/list なんだこれ\n/jyankenn (gu, chi, pa) : じゃんけんポン!\n/tenki : 1時間後までの平野区の降水確率を返します")

# pingコマンドを実装
@bot.command(name="ping", description="pingを返します")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"pong to {ctx.author.mention}")

# greetingコマンドを実装
@bot.command(name="greeting", description="挨拶を行います")
async def greeting(ctx: discord.ApplicationContext, user: discord.Option(discord.User, "対象のユーザー")):
    await ctx.respond(f"Hi, {user.mention}!")

# listコマンドを実装
# 意味はないです。ただのサンプルです。
@bot.command(name="list", description="龴〜氵⦡ㄦ・龴╪氵龴亻卄〜を返します")
async def list(ctx: discord.ApplicationContext, password: discord.Option(str, "パスワードを入力してください")):
    print(f"pass : {password}")
    if password == "マーシャル・マキシマイザー":
        await ctx.respond(f"やるやん\nhttps://www.youtube.com/watch?v=jMKPYg0uhCI")
    else:
        tmp = random.randint(0,  10)
        if tmp == 0:
            await ctx.respond(f"{password}つかってんの？")
        elif tmp == 1:
            await ctx.respond(f"そんなパスワードあるんかいな")
        elif tmp == 2:
            await ctx.respond(f"あー、{password}ね　知ってる知ってる")
        elif tmp == 3:
            await ctx.respond(f"{password}かー　なんか聞いたことあるな")
        elif tmp == 4:
            await ctx.respond(f"{password}やと。。。おしいなぁー")
        else:
            await ctx.respond(f"パスワードは{password}ではありませんでした。")

# jyankennコマンドを実装
# 絶対に勝てません。
@bot.command(name="jyankenn", description="じゃんけんを行います")
async def jyankenn(ctx: discord.ApplicationContext, hand: discord.Option(str, "手を入力してください(gu, chi, pa)")):
    if hand == "gu":
        await ctx.respond(f"あなたの手は **ぐー** ですね！\n私の手は **ぱー** です！\nhttps://img.gifmagazine.net/gifmagazine/images/3585293/original.mp4")
    elif hand == "chi":
        await ctx.respond(f"あなたの手は **ちょき** ですね！\n私の手は **ぐー** です！\nhttps://img.gifmagazine.net/gifmagazine/images/3585293/original.mp4")
    elif hand == "pa":
        await ctx.respond(f"あなたの手は **ぱー** ですね！\n私の手は **ちょき** です！\nhttps://img.gifmagazine.net/gifmagazine/images/3585293/original.mp4")
    else:
        await ctx.respond(f"あなたの手は **{hand}** ですね！\n私の手は **無敵** です！\nhttps://img.gifmagazine.net/gifmagazine/images/3585293/original.mp4")

# tenkiコマンドを実装
# 平野区の天気を返します
@bot.command(name="tenki", description="天気を返します")
async def tenki(ctx: discord.ApplicationContext):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = ""
        for feature in data["Feature"]:
            name = feature["Name"]
            weather_list = feature["Property"]["WeatherList"]["Weather"]
            result += f"Name: {name}\n"
            for weather in weather_list:
                date = weather["Date"][-8:-6] + "/" + weather["Date"][-6:-4] + " " + weather["Date"][-4:-2] + ":" + weather["Date"][-2:]
                rainfall = weather["Rainfall"]
                result += f"Date: {date}、降水確率: {rainfall}\n"
        await ctx.respond(result)
    elif response.status_code == 400:
        await ctx.respond("Bad Request! 渡されたパラメーターがWeb APIで期待されたものと一致しない")
    elif response.status_code == 503:
        await ctx.respond("Bad Request! 内部的な問題によってデータを返すことができない")
    else:
        await ctx.respond("Bad Request! その他のエラー")

# Botを起動
bot.run(token)
