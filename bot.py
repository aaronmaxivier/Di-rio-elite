import os
import discord
from discord.ext import commands
from database import init_db

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await init_db()
    print(f"Bot conectado como: {bot.user.name}")
    try:
        synced = await bot.tree.sync()
        print(f"Comandos sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")

# Cargar cogs/módulos
async def load_extensions():
    initial_extensions = [
        'cogs.main_panel',
    ]
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
        except Exception as e:
            print(f"Error cargando {extension}: {e}")

async def main():
    async with bot:
        await load_extensions()
        token = os.getenv("DISCORD_TOKEN")
        await bot.start(token)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  
