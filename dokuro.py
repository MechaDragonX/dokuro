#!/usr/bin/env python


import asyncio
import discord
import re


# Read info file to get any special information
with open('info.txt', 'r') as file:
    info_file = file.readlines()
    # Read the first line to get the client token
    token = token=info_file[0].strip()


class Client(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.synced =  False
        self.tree = discord.app_commands.CommandTree(self)


    async def setup_hook(self):
        await self.tree.sync()

    
    async def on_ready(self):
        print(f'Logged in as {self.user}')


    async def on_message(self, message):
        # Don't reply to self
        if message.author == self.user:
            return

        # Create vars
        msg = message.content
        msg_lower = msg.lower()
        mod_msg = "".join(re.findall(r'[a-z]', msg))

        # Handle skull alone while ignoring non alpha chars
        if 'sku' in mod_msg:
            if mod_msg == 'sku':
                await message.channel.send('https://en.wikipedia.org/wiki/Stock_keeping_unit')
            elif mod_msg == 'skull':
                await message.channel.send('https://youtu.be/HejoBEPCDCk')
            elif mod_msg == 'skul':
                await message.channel.send('💀')

        # Handle mambo if present in general
        if 'mambo' in mod_msg:
            await message.channel.send('<:mambo:1490734126142193824>')

        # Replace road with kirk (skull)
        new_msg = msg
        if 'road' in msg_lower:
            new_msg = msg.replace('road', '**kirk**')
            await message.channel.send(new_msg)
            


bot = Client()
bot.run(token)

