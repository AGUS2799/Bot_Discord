from random import choice
import discord
from discord.ext import commands



bot = commands.Bot(command_prefix="!", description="El mejor bot")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def sum(ctx, numOne , numTwo):
    await ctx.send(int(numOne ) + int(numTwo))

@bot.command()
async def champ(ctx):
    campeones = ["Aatrox",
"Ahri",
"Akali",
"Akshan",
"Alistar",
"Amumu",
"Anivia",
"Annie",
"Aphelios",
"Ashe",
"Aurelion Sol",
"Azir",
"Bardo",
"Blitzcrank",
"Brand",
"Braum",
"Caitlyn",
"Camille",
"Cassiopeia",
"Cho’Gath",
"Corki",
"Darius",
"Diana",
"Dr. Mundo",
"Draven",
"Ekko",
"Elise",
"Evelynn",
"Ezreal",
"Fiddlesticks",
"Fiora",
"Fizz",
"Galio",
"Gangplank",
"Garen",
"Gnar",
"Gragas",
"Graves",
"Gwen",
"Hecarim",
"Heimerdinger",
"Illaoi",
"Irelia",
"Ivern",
"Janna",
"Jarvan IV",
"Jax",
"Jayce",
"Jhin",
"Jinx",
"Kai’Sa",
"Kalista",
"Karma",
"Karthus",
"Kassadin",
"Katarina",
"Kayle",
"Kayn",
"Kennen",
"Kha’Zix",
"Kindred",
"Kled",
"Kog’Maw",
"LeBlanc",
"Lee Sin",
"Leona",
"Lillia",
"Lissandra",
"Lucian",
"Lulu",
"Lux",
"Maestro Yi",
"Malphite",
"Malzahar",
"Maokai",
"Miss Fortune",
"Mordekaiser",
"Morgana",
"Nami",
"Nasus",
"Nautilus",
"Neeko",
"Nidalee",
"Nocturne",
"Nunu y Willump",
"Olaf",
"Orianna",
"Ornn",
"Pantheon",
"Poppy",
"Pyke",
"Qiyana",
"Quinn",
"Rakan",
"Rammus",
"Rek’Sai",
"Rell",
"Renata Glasc",
"Renekton",
"Rengar",
"Riven",
"Rumble",
"Ryze",
"Samira",
"Sejuani",
"Senna",
"Seraphine",
"Sett",
"Shaco",
"Shen",
"Shyvana",
"Singed",
"Sion",
"Sivir",
"Skarner",
"Sona",
"Soraka",
"Swain",
"Sylas",
"Syndra",
"Tahm Kench",
"Taliyah",
"Talon",
"Taric",
"Teemo",
"Thresh",
"Tristana",
"Trundle",
"Tryndamere",
"Twisted Fate",
"Twitch",
"Udyr",
"Urgot",
"Varus",
"Vayne",
"Veigar",
"Vel’Koz",
"Vex",
"Vi",
"Viego",
"Viktor",
"Vladimir",
"Volibear",
"Warwick",
"Wukong",
"Xayah",
"Xerath",
"Xin Zhao",
"Yasuo (Que maricon)",
"Yone",
"Yorick",
"Yuumi",
"Zac1",
"Zed",
"Zeri",
"Ziggs",
"Zilean",
"Zoe",
"Zyra"]
    camp_aleatorio = choice(campeones)
    await ctx.send(camp_aleatorio)


#Evento
@bot.event
async def on_ready():
    print("My bot is ready")


bot.run("TOKEN_DISCORD")
