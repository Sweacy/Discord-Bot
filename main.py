import os
import discord
import random
from discord.ext import commands
from webserver import keep_alive

bot = commands.Bot(command_prefix="?")

#hi
@bot.command()
async def hi(ctx):
    await ctx.send("um, hello?")
    print("Command issued")
    print("Waiting for next command")


#rules
@bot.command()
async def rules(ctx):
    await ctx.send("check #rules")
    print("Command issued")
    print("Waiting for next command")


#ping
@bot.command()
async def pingme(ctx):
    await ctx.send(ctx.author.mention)
    print("Command issued")
    print("Waiting for next command")


#get bot info
@bot.command()
async def botinfo(ctx):
    await ctx.send("im just a bot...")
    print("Command issued")
    print("Waiting for next command")


#ask for money
@bot.command()
async def money(ctx):
    await ctx.send("Im broke, ask the bank lmfao")
    print("Command issued")
    print("Waiting for next command")


#jokes
@bot.command()
async def jokes(ctx):
    jokes_responses = [
        'What do birds give out on Halloween? Tweets.',
        'Where did the music teacher leave her keys? In the piano!',
        'How does the ocean say hi? It waves!',
    ]
    await ctx.send(f'{random.choice(jokes_responses)}')
    print("Command issued")
    print("Waiting for next command")


#gamble
@bot.command()
async def gamble(ctx):
    gamble_responses = [
        'You won!',
        'You lost!',
        'Lucky you, its a tie!',
    ]
    await ctx.send(f'{random.choice(gamble_responses)}')
    print("Command issued")
    print("Waiting for next command")


#class list
@bot.command()
async def classes(ctx):
    await ctx.send("Classes : How to make a box(box), How to say hi(hi).")
    print("Command issued")
    print("Waiting for next command")


#box class
@bot.command()
async def class_box(ctx):
    await ctx.send(
        "1.Choose your paper. For this method, rectangular paper works best. If you are making a gift or a party favor, use brightly colored and/or patterned paper. If you are simply practicing your paper folding skills, use some scrap paper instead. 2.Fold the paper vertically in half. If using patterned paper, make sure the pattern is on the outside. Unfold the paper again. 3.Fold each side of the paper to the center crease. Take the edge and line it with the center crease. Once again, the pattern should be on the outside. Unfold the paper. It should now be in quarters sectioned widthwise. 4.Fold the entire paper in half lengthwise. The pattern should be on the outside. Unfold the paper once more. It should now be in eight equal sections. 5.Fold each short side to the center crease. You are doing the same thing with this new lengthwise center crease as you did in Step 3. 6.Fold each corner. Line the corners up with the nearest lengthwise crease. The folded corners should each form right triangles with their bases flush with a lengthwise crease. You should end up with an uneven octagon. 7.Fold the flaps from the middle down over the triangles made in the previous step. This opens the center of the paper so you can see the center crease inside the box. 8.Pull up on the two flaps. You can grip them by the creases in the middle. You should now have a complete box. 9.Make any finishing touches. Use some scotch tape on the corners if you would like them to sit flat. Decorate the bed of the box with markers or pens if you want to. If you're using it to hold a gift, write a surprise message to your giftee that will be covered by the item."
    )
    print("Command issued")
    print("Waiting for next command")


#hi class
@bot.command()
async def class_hi(ctx):
    await ctx.send("1.Say hi")
    print("Command issued")
    print("Waiting for next command")

#bye
@bot.command()
async def bye(ctx):
  await ctx.send("umm, bye? I guess?")
  print("Command issued")
  print("Waiting for next command")

#random cmd
@bot.command()
async def randomcmd(ctx):
  cmd_responses = ['hi', 'bye', 'pingme', 'botinfo', 'money', 'jokes', 'gamble', 'classes', 'swear', 'eightball',]
  await ctx.send(f'{random.choice(cmd_responses)}')
  print("Command issued")
  print("Waiting for next command")

#swear
@bot.command()
async def swear(ctx):
  swear_responses = ['You are not allowed to swear', 'I wont swear L', 'I dont know what to say....']
  await ctx.send(f'{random.choice(swear_responses)}')
  print("Command issued")
  print("Waiting for next command")

#8ball
@bot.command()
async def eightball(ctx):
  ball_responses = ['Yes', 'No', 'Maybe', 'I dont understand',]
  await ctx.send(f'{random.choice(ball_responses)}')
  print("Command issued")
  print("Waiting for next command")

#randomnum
@bot.command()
async def randomnum(ctx):
  num_responses = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',]
  await ctx.send(f'{random.choice(num_responses)}')
  print("Command issued")
  print("Waiting for next command")

keep_alive()
token = os.environ['TOKEN']
bot.run(token)
