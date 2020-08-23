from discord.ext import commands
import discord
import datetime
from settings_files._global import *

class Servidor(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(brief=": Muestra el estado del bot en este servidor :3")
    async def status(self, ctx, *args):

        guild = ctx.guild
        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)
        
        embed = discord.Embed(description="Server Status", colour=discord.Colour.magenta())

        embed.set_thumbnail(url=URL_log)#LOGO
        embed.set_image(url=URL_log)
        embed.add_field(name="Nombre del Servidor", value = guild.name, inline = False)
        #embed.add_field(name="# de Canales de Voz", value = no_voice_channels)
        #embed.add_field(name="# Text Channels", value = no_text_channels)
        embed.set_author(name=self.bot.user.name)
        embed.set_footer(text=datetime.datetime.now())

        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(Servidor(bot))