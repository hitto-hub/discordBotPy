import dotenv
import os
# Pycordを読み込む
import discord

# アクセストークンを設定
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot入門"),  # "〇〇をプレイ中"の"〇〇"を設定,
)


# 起動時に自動的に動くメソッド
# #03で詳しく説明します
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


# pingコマンドを実装
@bot.command(name="ping", description="pingを返します")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"pong to {ctx.author.mention}")

@bot.command(name="greeting", description="挨拶を行います")
async def greeting(ctx: discord.ApplicationContext, user: discord.Option(discord.User, "対象のユーザー")):
    await ctx.respond(f"Hi, {user.mention}!")

@bot.command(name="list", description="listを返します")
async def list(ctx: discord.ApplicationContext, password: discord.Option(str, "パスワードを入力してください")):
    await ctx.respond(f"パスワードは{password}ですね！")

@bot.command(name="jyankenn", description="じゃんけんを行います")
async def jyankenn(ctx: discord.ApplicationContext, hand: discord.Option(str, "手を入力してください（ぐー、ちょき、ぱー）")):
    if hand == "ぐー":
        await ctx.respond(f"あなたの手は **{hand}** ですね！\n私の手は **ぱー** です！\nhttps://img.gifmagazine.net/gifmagazine/images/3585293/original.mp4")
    elif hand == "ちょき":
        await ctx.respond(f"あなたの手は **{hand}** ですね！\n私の手は **ぐー** です！\nhttps://img.gifmagazine.net/gifmagazine/images/3585293/original.mp4")
    elif hand == "ぱー":
        await ctx.respond(f"あなたの手は **{hand}** ですね！\n私の手は **ちょき** です！\nhttps://img.gifmagazine.net/gifmagazine/images/3585293/original.mp4")
    else:
        await ctx.respond(f"あなたの手は **{hand}** ですね！\n私の手は **無敵** です！\nhttps://img.gifmagazine.net/gifmagazine/images/3585293/original.mp4")

# Botを起動
bot.run(token)
