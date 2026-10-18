import discord
from discord.ext import commands
from discord import app_commands
from database import set_config, get_config

class MainPanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🎮 Solo", style=discord.ButtonStyle.primary, custom_id="btn_solo")
    async def btn_solo(self, interaction: discord.Interaction, button: discord.ui.Button):
        chave_pix = await get_config("pix_key") or "No configurada"
        embed = discord.Embed(
            title="🏆 Inscrição SOLO - Diário Elite",
            description=f"**Valor:** R$ 1,50\n**Chave Pix:** `{chave_pix}`\n\nEnvie o comprovante nesta conversa para confirmar sua vaga!",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="👥 Duo", style=discord.ButtonStyle.success, custom_id="btn_duo")
    async def btn_duo(self, interaction: discord.Interaction, button: discord.ui.Button):
        chave_pix = await get_config("pix_key") or "No configurada"
        embed = discord.Embed(
            title="🏆 Inscrição DUO - Diário Elite",
            description=f"**Valor:** R$ 3,00\n**Chave Pix:** `{chave_pix}`\n\nEnvie o nick dos 2 jogadores e o comprovante para confirmar!",
            color=discord.Color.blue()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

class MainPanel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setup_panel")
    @commands.has_permissions(administrator=True)
    async def setup_panel(self, ctx):
        embed = discord.Embed(
            title="🔥 DIÁRIO ELITE - FREE FIRE 🔥",
            description="Selecione abaixo a modalidade para se inscrever no campeonato!",
            color=discord.Color.gold()
        )
        view = MainPanelView()
        await ctx.send(embed=embed, view=view)

    @app_commands.command(name="config_pix", description="Configura a chave Pix do campeonato")
    async def config_pix(self, interaction: discord.Interaction, chave: str):
        await set_config("pix_key", chave)
        await interaction.response.send_message(f"✅ Chave Pix atualizada para: `{chave}`", ephemeral=True)

async def setup(bot):
    await bot.add_cog(MainPanel(bot))
