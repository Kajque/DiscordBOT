from discord import app_commands
import discord; from discord.ext import commands
from discord.ext.commands import bot
from discord import ui
from key import token



intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = token.get("TOKEN")

server_id = 1040828734791483544

@client.event
async def on_ready():
	print(f"{client.user} Esta online. Tudo atualizado")

@app_commands.guild_only()
class MyGroup(app_commands.Group):
    pass




class Modal(discord.ui.Modal):
	def __init__(self):
		super().__init__(title="Painel de criacao.")

	titulo = discord.ui.TextInput(label='Titulo da embed:', style=discord.TextStyle.short)
	descricao = discord.ui.TextInput(label='Descricao da embed:', style=discord.TextStyle.short)
	
	async def on_submit(self, interaction):
		embed = discord.Embed(title=self.titulo, description=self.descricao)
		await interaction.response.send_message("Embed enviada com sucesso", ephemeral=False)
		await interaction.response.send(embed=embed)


class criarembed(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@discord.app_commands.command(name='criar_embed', description='aprendendo criar embed')
	async def createembed(self, interaction):
		await interaction.response.send_modal(Modal())

async def setup(bot):
	await bot.add_cog(Criarembed(bot))

@client.event
async def on_message(message):

	conteudo = message.content
	l_conteudo = conteudo.lower()

	if message.author == client.user:		# Se o autor for o bot da um return
		return

	if l_conteudo.startswith("!online"):
		await message.channel.send(f"Estou online {message.author.name}")

	if '!a' in l_conteudo:
		await message.channel.send(f"Quem me criou foi o kaique")




client.run(TOKEN)