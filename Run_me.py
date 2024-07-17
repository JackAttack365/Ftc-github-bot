import discord
from discord import app_commands
from discord.ext import commands
import sys
import os
from datetime import datetime
import json
#import custom functions below other above
sys.path.append(os.path.join(os.path.dirname(__file__), 'boring-functions'))
from convert_name_function import convert_userid_to_name # type: ignore
from Email_function import Email_people_func # type: ignore
from googledocsfunc import add_row_to_sheet # type: ignore
from get_secdule_func import get_schedule #type: ignore
from read_jason import find_matches #type: ignore
from get_info import get_info #type: ignore gets information from the master file and it reutrns a streing so make sure to type cast

#whare logs are stored
log_directory = "logs"  

#This is the bot token
Bot_token:str = get_info(3) #reads the 4th line of the file cause arrays start at 0

# this is the google sheets link that the bot puts the requested parts in.
gsheets_parts_list:str = get_info(9)
gsheets_time_line = get_info(6)

# Creates a instince of the bot
intents = discord.Intents.default()
intents.members = True  # Ensure the bot can read member information
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Define a tree for the app commands (slash commands)
tree = bot.tree

# Define the slash command for requesting a part
@tree.command(
    name="request",
    description="A slash command to request a part"
)
@app_commands.describe(argument="The part to be requested")
async def _but(interaction: discord.Interaction, argument: str):   
    
    name = convert_userid_to_name(interaction.user.id)
    message = f"{name} requested we buy this part: {argument}"
    
    #for google docs right now is disabled
    add_row_to_sheet(gsheets_parts_list,message)

    await interaction.response.send_message(f"Message added to the google sheets.\n{gsheets_parts_list}", ephemeral=False)



#time line func
@tree.command(
    name="timeline",
    description="Creates a marker on a timeline"
)
@app_commands.describe(argument="What happened")
async def timeline(interaction: discord.Interaction, argument: str):
    # Fetch the guild (server) and the role
    
    
    
    name = convert_userid_to_name(interaction.user.id)
    the_time = datetime.now()
    year = the_time.year
    month = the_time.month
    day = the_time.day
    message = f"{name} said this happend: {argument} on {year}/{month}/{day}"
    
    #for google docs right now is disabled
    add_row_to_sheet(gsheets_time_line,message)
        
    await interaction.response.send_message(f"The time line has been updated at the google sheets.\n{gsheets_time_line}", ephemeral=False)



#start the clock for auto times
#each match is about 3 mins 10 secends
@tree.command(
    name="get_events",
    description="Gets the events that your team will be in"
)
@app_commands.describe(
    event_code="the code for the current event",
    team_num="the number of your team"
)
async def start_the_clock(interaction: discord.Interaction, event_code: str, team_num: str):
    season: int = 2023
    username = get_info(12)
    password = get_info(15)
    schedule = get_schedule(season, event_code, username, password, team_num)    

    if schedule:
        pretty_schedule = json.dumps(schedule, indent=4)
        message = "Created the JSON file."

        # Write the pretty-printed schedule to a file
        with open("test.json", 'w') as f:
            f.write(pretty_schedule)
    else:
        print("Failed to retrieve schedule")
        message = "Failed to retrieve schedule."

    await interaction.response.send_message(find_matches(int(team_num)), ephemeral=False)



@tree.command(
    name="help",
    description="Shows what all comands do in depth"
)
async def Help(interaction: discord.Interaction):
    
    await interaction.response.send_message(f"Still gotta work on this lol.", ephemeral=True)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        print(f"Server: {guild.name}")

#Auto mod
@bot.event
async def on_message(message):
    if message.author == bot.user:  # Check if the author of the message is the bot itself
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot.run(Bot_token)