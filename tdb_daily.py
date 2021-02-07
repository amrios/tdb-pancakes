#!/usr/bin/python3

# Daily module
# Set in cron to run at least once a day.
#

import discord

CHANNEL_ID = chan_int
TOKEN = "token"


class DailyMod(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        channel = self.get_channel(CHANNEL_ID)
        await channel.send('p!daily')
        await self.logout()


client = DailyMod()
client.run(TOKEN, bot=False)
