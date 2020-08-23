from discord.ext import commands
from settings_files._global import *
import discord
class Torneo(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Porfavor verifique el uso de este comando escribiendo <help o habla con el administrador.")


    @commands.command(brief=": Muestra la moción de la ronda actual.")
    async def moción(self, ctx, *args):
        embed = discord.Embed(description="Moción de la Ronda", colour=discord.Colour.red())
        embed.set_image(url=URL_moc)
        embed.set_footer(text="Moción de Ronda Actual")
        await ctx.send(embed=embed) 
                
    @commands.command(brief=": Muestra el Draw de la ronda actual.")
    async def draw(self, ctx, *args):
        embed = discord.Embed(description="Draw de la Ronda", colour=discord.Colour.red())
        embed.set_image(url=URL_draw)
        embed.set_footer(text="Draw de Ronda Actual")
        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(Torneo(bot))

