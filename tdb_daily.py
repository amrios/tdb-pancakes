#!/usr/bin/python3

# Daily module
# Set in cron to run at least once a day.
# 

CHANNEL_ID = 
TOKEN = 

import sqlite3
import discord

class dailyMod(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)
		channel = self.get_channel(somechannel)
		await channel.send('p!daily')
		raise SystemExit

		
	

	
	#async def on_message(self, message):
	#	if str(message.author) in "Pancake#3691":
	#		print('Message from {0.author}: {0.content}'.format(message))


client = dailyMod()
client.run("somekey", bot=False)
