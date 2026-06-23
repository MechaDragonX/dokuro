#!/usr/bin/env python

import asyncio
import discord

# Read info file to get any special information
with open('info.txt', 'r') as file:
    info_file = file.readlines()
    # Read the first line to get the client token
    token = token=info_file[0].strip()

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced =  False
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
    
    async def on_ready(self):
        print(f'Logged in as {self.user}')

bot = Client()
bot.run(token)

