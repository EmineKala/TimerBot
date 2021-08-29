import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.utils import get_expire_time

TOKEN ="ODc5ODE5NDY3NjgzNjgwMjk3.YSVRuw.sv2qnWIQAheeZoDlCZoC6V0ebKc"

version = '1.0.0'
bot = commands.Bot(command_prefix='.', status=discord.Status.online,
                   help_command=None)

counter = AsyncIOScheduler()

@bot.event
async def on_ready():
    print("Timer Started")
    counter.start()

@bot.command(name='help')
async def send_help_message(ctx):
    #Timer bot help command
    await ctx.channel.send(
        f"```css\n[Timer Bot]\n - Start command : .start Work_min \n     ex) .start 25 "
        f"\n -  Stop command : .stop```")

@bot.command(name='start')
async def start_timer(ctx, work_time: int):
    """ Args:
        work_time : work timer (minute)
    """
    if len(counter.get_jobs()) > 0:
        await ctx.channel.send(
            f"```css\n[Timer already working!]\n - stop command : .stop```")
        return

    async def work_schedule(work_time):
        print('Timer Started')
        await ctx.channel.send(
            f"{ctx.author.mention}```css\n[Work time end!] Let's break :)```")
        pass

    work_expire_time = get_expire_time(work_time)
    counter.add_job(work_schedule, run_date=work_expire_time,
                  args = [work_time])

    await ctx.channel.send(
        f"```css\n{work_time} min Timer STARTED.\n - stop command : .stop```")

@bot.command(name='stop')
async def stop_timer(ctx):
    
     counter.remove_all_jobs()
     await ctx.channel.send(
        f"```css\nTimer STOPPED.\n - start command : .start work_min```")


bot.run(TOKEN)
