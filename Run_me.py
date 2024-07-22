import discord
from discord import app_commands
from discord.ext import commands
import sys
import os
from datetime import datetime
import json
<<<<<<< HEAD
import asyncio
=======
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98
#import custom functions below other above
sys.path.append(os.path.join(os.path.dirname(__file__), "boring-functions"))
from convert_name_function import convert_userid_to_name # type: ignore
from googledocsfunc import add_row_to_sheet # type: ignore
<<<<<<< HEAD
from get_info import get_info,get_sheets #type: ignore gets information from the master file and it reutrns a streing so make sure to type cast
from fetch_and_find_matches import get_events_into_json, find_matches,get_current_event,find_match_nums #type: ignore
from set_up import set_up #type: ignore gets information from the master file and it reutrns a streing so make sure to type cast
=======
from get_secdule_func import get_schedule #type: ignore
from read_jason import find_matches #type: ignore
from get_info import get_info #type: ignore gets information from the master file and it reutrns a streing so make sure to type cast
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98

#whare logs are stored
log_directory = "logs"  

#This is the bot token
Bot_token:str = get_info(3) #reads the 4th line of the file cause arrays start at 0

# this is the google sheets link that the bot puts the requested parts in.
<<<<<<< HEAD

=======
gsheets_parts_list:str = get_info(9)
gsheets_time_line = get_info(6)
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98

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
    
    server_name = interaction.guild.name
    gsheets_parts_list = get_sheets(0,server_name)
    
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
    
    
    
<<<<<<< HEAD
    name = interaction.user.nick
=======
    name = convert_userid_to_name(interaction.user.id)
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98
    the_time = datetime.now()
    year = the_time.year
    month = the_time.month
    day = the_time.day
    message = f"{name} said this happend: {argument} on {year}/{month}/{day}"
    
<<<<<<< HEAD
    server_name = interaction.guild.name
    gsheets_time_line = get_sheets(1,server_name)


    #for google docs right now is disabled
    add_row_to_sheet(gsheets_time_line,message)
        
    await interaction.response.send_message(f"The time line has been updated at the google sheets.\n{gsheets_time_line}", ephemeral=False)

@tree.command(
    name="start_the_clock",
    description="Creates a reminder"
)
@app_commands.describe(team_num="Your team number",
                       current_match_arg = "what match is it?"
                       )

async def start_the_clock(interaction: discord.Interaction, team_num: str, current_match_arg: int):
    await interaction.response.send_message("Starting timer...", ephemeral=False)
    await interaction.followup.send(find_matches(team_num))
    season: int = 2023
    username = get_info(6)
    password = get_info(9)
    
    get_events_into_json(season, username, password, team_num)
    get_current_event(season, username, password, team_num)
    
    Matches = find_match_nums(team_num)
    greatest_match = max(Matches)
    current_match = current_match_arg
    
    while True:
        if current_match > greatest_match:
            await interaction.followup.send("the timer has ended.")
            break
            
        elif current_match + 1 in Matches:
            await interaction.followup.send(f"Hey match {current_match} is coming up!", ephemeral=False)
            current_match = current_match + 1
            await asyncio.sleep(130) 
            print (current_match)
        else:
            await asyncio.sleep(130) 
            print(current_match)
            current_match = current_match + 1
        


#get events
@tree.command(
    name="get_schdule",
    description="Gets the most resent schdule and sends a message with it"
)
@app_commands.describe(
    team_num="the number of your team"
)
async def get_events(interaction: discord.Interaction, team_num: str):
    await interaction.response.send_message("hang on one sec")
    season: int = 2023
    username = get_info(6)
    password = get_info(9)
    get_events_into_json(season,username,password,team_num)
    get_current_event(season, username, password,team_num)
    print(find_match_nums(team_num))
    await interaction.followup.send(find_matches(team_num))


#help command
=======
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



>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98
@tree.command(
    name="help",
    description="Shows what all comands do in depth"
)
async def Help(interaction: discord.Interaction):
    
<<<<<<< HEAD
    await interaction.response.send_message(f"Welcome To alfradio 3.0 \nIf you need more help join the help server at https://discord.gg/6PVDP9EJvB\nOr you can dig through my source code here https://github.com/blueofficer/Ftc-github-bot\nTo get started use /setup", ephemeral=False)

#the set up command
@tree.command(
    name="setup",
    description="The setup command for the bot"
)
async def the_set_up(interaction: discord.Interaction):
    server_name:str = str(interaction.guild.name)
    file_path = f"team_files\\{server_name}\\{server_name}google_seets.txt"
    if os.path.exists(file_path):
        await interaction.response.send_message("setup does not need to be run")
    else:
        await interaction.response.send_message(f"Creating the google sheets.......", ephemeral=False)
        set_up(server_name)
        await interaction.followup.send(f"Created the google sheets", ephemeral=False)
=======
    await interaction.response.send_message(f"Still gotta work on this lol.", ephemeral=True)
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98

@bot.event
async def on_ready():
    #await tree.sync()
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        print(f"Server: {guild.name}")
<<<<<<< HEAD

=======
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98

#Auto mod
@bot.event
async def on_message(message):
    if message.author == bot.user:  # Check if the author of the message is the bot itself
        return

<<<<<<< HEAD
    if message.content.startswith("$thank you"):
        await message.channel.send("Thank you teams Electric Bacon (13733), Screaming Eagles(13002), Giggle Pickle(24253) for allowing me to build this bot and having them test it. :D")
    elif message.content.startswith("ester"):
        await message.channel.send("Thank you teams Electric Bacon (13733), Screaming Eagles(13002), Giggle Pickle(24253) for allowing me to build this bot and having them test it. :D")
=======
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98
bot.run(Bot_token)