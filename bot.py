import discord
import os
import json


client = discord.Client()



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)


  # if message.content.startswith('$hello'):
  #       await message.channel.send('Hello!')
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

  if message.content.startswith('$hello'):
    msg = 'Kya haal hai {0.author.mention}'.format(message)
    await message.channel.send(msg)


client.run(os.environ['DISCORD_TOKEN'])
