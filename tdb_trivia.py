#!/usr/bin/python3

# Daily module
# Set in cron to run at least once a day.
#

import discord
import api.tdb_lookup

CHANNEL_ID = chan_int
TOKEN = "token"
PANCAKE_ID = 239631525350604801


class DailyMod(discord.Client):
    client = discord.Client
    lookup = api.tdb_lookup()
    channel = None

    async def on_ready(self):
        print('Logged on as', self.user)
        self.channel = self.get_channel(CHANNEL_ID)
        await self.channel.send('p!trivia hard')

    async def on_message(self, message):
        content = message.content

        if message.author.id == PANCAKE_ID:
            if "You must wait" in content:  # Within cooldown
                print("You must wait until you can use the bot again.\n")
                print(content)
                await self.logout()
                return
            if len(message.embeds) == 0:  # Has no embeds
                print("Non-trivia message recieved.")
                await self.logout()
                return

            embed = message.embeds[0]
            body = embed.description.splitlines()
            question = body[0]
            print(question)
            answer = self.lookup.get_answer(question)
            print(answer)

            if answer is None:  # Lookup failed
                print("Question recieved isn't indexed")
                await self.client.logout()
                return

            for i in range(1, 5):
                if answer in body[i + 1]:
                    await self.channel.send(str(i))
                    await self.client.logout()
                    return

            print("Answer couldn't be found, maybe it's not indexed?")
            await self.logout()


client = DailyMod()
client.run(TOKEN, bot=False)
