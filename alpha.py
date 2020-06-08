import discord
import asyncio
from discord.ext import commands
import random

TOKEN = (process.env.TOKEN):
bot = commands.Bot(command_prefix="&")



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('&info créé par Maxx#7044'))
    print("Bot prêt")




@bot.command()
async def info(channel):
    await channel.send("Mon créateur : Max#7044.\nEnvoyez lui un MP si vous avez une question.\nFaîtes &commandes pour connaître la liste des commandes du bot. :wink:")
  
    
   
    
@bot.command()
async def commandes(channel):
    await channel.send("Voici la liste des commandes (mon préfixe est &) :\n\ninfo : pour l'id de mon créateur\nping : pour connaître la latence exacte du bot\nclear [nombre de message à supprimer] (si vous avez les permissions)\nsay [message à faire dire au bot]\nkick : pour exclure un membre (si vous avez les permissions)\ncommencer : pour commencer le jeu de rôle.")


import discord 
import time
Client = commands.Bot(commands.when_mentioned_or('...'))


@bot.command() 
async def ping(ctx): 
    await ctx.send(f'Ping : {round(bot.latency * 1000)}ms')


@bot.command()
@commands.has_permissions(manage_messages = True) 
async def clear(ctx, nombre : int):
  await ctx.channel.purge(limit = nombre + 1)


@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))
    await ctx.message.delete()

@bot.command() 
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} a été kické.')


 




@bot.command()
async def commencer(channel):
    await channel.send("Dès que vous verrez le signe & cela indique que c'est une commande utilisable.\nVous êtes un chasseur de prime à la recherche d'un criminel. Vous avez eu comme information une adresse et vous vous y êtes rendu. C'est un très vieux manoir.\n__&aller__ (pour rentrer dans la maison) __&partir__ (pour rentrer chez vous)")

@bot.command()
async def partir(channel):
    await channel.send("Fin : vous n'êtes pas aller très loin...")

@bot.command()
async def aller(channel):
    await channel.send("Vous rentrez dans le manoir et appercevez des épées en guise de décoration puis un revolver. Vous choisissez : __&revolver__ __&épée__ ou votre vieux __&couteau__")

@bot.command()
async def couteau(channel):
    await channel.send("En le sortant de votre poche la lame se brise et s'enfonce dans votre cuisse.... Vous devez impérativement trouver de quoi faire un __&garrot__")

@bot.command()
async def garrot(channel):
    await channel.send("Vous avez trouvé un torchon pour en faire un garrot mais un homme rentre dans la pièce avec un poignard et vous fonce dessus. __&résister__ ou se laisser __&mourrir__ ?")

@bot.command()
async def résister(channel):
    await channel.send("Vous résistez tant bien que mal mais vous finissez par fatiguer et l'homme vous tue. Fin.")

@bot.command()
async def mourrir(channel):
    await channel.send("Vous n'avez sûrement pas fait le bon choix... A moins que ce soit une faute de frappe ?? Fin...")

@bot.command()
async def revolver(channel):
    await channel.send("Vous avez un revolver avec vous. Un homme arrive avec un poignard et vous fonce dessus. Vous sortez votre arme mais il n'est pas chargé.... Fin. ")

@bot.command()
async def épée(channel):
    await channel.send("Vous avez une épée. Un homme arrive avec un poignard et vous fonce dessus. __&attaquer__ ou __&parer__ ?")

@bot.command()
async def attaquer(channel):
    await channel.send("Vous coupez la jambe de l'inconnu mais il vous atteint au coeur.... Fin.")

@bot.command()
async def parer(channel):
    await channel.send("Vous esquivez ses attaques puis vous le tuez avec votre arme. __&avancer__")

@bot.command()
async def avancer(channel):
    await channel.send("Vous vous trouvez devant une cage d'escalier très sombre mais au dessus de vous se trouve une trappe avec une échelle pour y accèder. __&trappe__ ou __&escalier__ ?")

@bot.command()
async def escalier(channel):
    await channel.send("Vous descendez les escaliers sombres et vous retrouvez nez à nez avec un crâne humain...__&continuerdescendre__")

@bot.command()
async def trappe(channel):
    await channel.send("Vous montez dans la trappe et vous vous retrouvez dans un vieux salon. Vous entendez des bruits de pas et des gens qui parlent. __&cacher__ pour écouter ce qu'ils disent. __&tuer__ pour les attaquer")

@bot.command()
async def tuer(channel):
    await channel.send("Vous les attaquez mais ils sont 3, vous ne faîtes pas le poids.... Fin.")

@bot.command()
async def cacher(channel):
    await channel.send("Vous les entendez parler d'une cargaison de drogue, qui se trouve dans un bunker, à livrer dès l'aube, vous comprenez que vous êtes dans leur repère et qu'il reste beaucoup de leurs complices. Vos informateurs ne vous avaient pas  parler de ça...A suivre")


@bot.command()
async def continuerdescendre(channel):
    await channel.send("Vous vous retrouvez devant une porte blindée et vous comprenez qu'il y a un bunker sous cette maison... Vos informateurs ne vous avaient pas  parler de ça..... A suivre.")



try: 
    bot.run(TOKEN)
except keybordInterrupt: 
    print("")

