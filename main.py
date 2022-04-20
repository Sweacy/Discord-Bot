import os
import discord 
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="?")

#commands list
@bot.command()
async def cmdlist(ctx):
  await ctx.send("cmdlist(list all cmds), hi(say hi to the boy), rules(tell u where to find to rules), pingme(ping the person executing the command), botinfo(tell u this bot's info), money(ask the bot for money), jokes(tell u a joke), gamble(gamble, but no money needed), classes(list all classes the bot provides)")

#hi
@bot.command()
async def hi(ctx):
  await ctx.send("um, hello?")

#rules
@bot.command()
async def rules(ctx):
  await ctx.send("check #rules")

#ping
@bot.command()
async def pingme(ctx):
  await ctx.send(ctx.author.mention)

#get bot info
@bot.command()
async def botinfo(ctx):
  await ctx.send("im just a bot...")
#ask for money
@bot.command()
async def money(ctx):
  await ctx.send("Im broke, ask the bank lmfao")

#jokes
@bot.command()
async def jokes(ctx):
  jokes_responses = ['What do birds give out on Halloween? Tweets.',
  'Where did the music teacher leave her keys? In the piano!',
  'How does the ocean say hi? It waves!',]
  await ctx.send(f'{random.choice(jokes_responses)}')

#gamble
@bot.command()
async def gamble(ctx):
  gamble_responses = ['You won!', 'You lost!', 'Lucky you, its a tie!',]
  await ctx.send(f'{random.choice(gamble_responses)}')

#class list
@bot.command()
async def classes(ctx):
  await ctx.send("Classes : How to make a box(box), How to say hi(hi).")
#box class
@bot.command()
async def class_box(ctx):
  await ctx.send("1.Choose your paper. For this method, rectangular paper works best. If you are making a gift or a party favor, use brightly colored and/or patterned paper. If you are simply practicing your paper folding skills, use some scrap paper instead. 2.Fold the paper vertically in half. If using patterned paper, make sure the pattern is on the outside. Unfold the paper again. 3.Fold each side of the paper to the center crease. Take the edge and line it with the center crease. Once again, the pattern should be on the outside. Unfold the paper. It should now be in quarters sectioned widthwise. 4.Fold the entire paper in half lengthwise. The pattern should be on the outside. Unfold the paper once more. It should now be in eight equal sections. 5.Fold each short side to the center crease. You are doing the same thing with this new lengthwise center crease as you did in Step 3. 6.Fold each corner. Line the corners up with the nearest lengthwise crease. The folded corners should each form right triangles with their bases flush with a lengthwise crease. You should end up with an uneven octagon. 7.Fold the flaps from the middle down over the triangles made in the previous step. This opens the center of the paper so you can see the center crease inside the box. 8.Pull up on the two flaps. You can grip them by the creases in the middle. You should now have a complete box. 9.Make any finishing touches. Use some scotch tape on the corners if you would like them to sit flat. Decorate the bed of the box with markers or pens if you want to. If you're using it to hold a gift, write a surprise message to your giftee that will be covered by the item.")

#hi class
@bot.command()
async def class_hi(ctx):
  await ctx.send("1.Say hi")

token = os.environ['TOKEN']
bot.run(token)
