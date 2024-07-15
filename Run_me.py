import discord
from discord import app_commands
from discord.ext import commands
import sys
import os
#import custom functions below other above
sys.path.append(os.path.join(os.path.dirname(__file__), 'boring-functions'))
from convert_name_function import convert_userid_to_name # type: ignore
from Email_function import Email_people_func # type: ignore
from googledocsfunc import add_row_to_sheet # type: ignore

#this is for if the bot should dm
send_to_users = True

#whare logs are stored
log_directory = "logs"  

#this is the file that containes all passwords and other settings
Master_file = open("setup\Importentfile.txt")

#and this puts it so that i can read it as an list
Master_file_content = Master_file.readlines()

#This is the bot token
Bot_token:str = str(Master_file_content[3]) #reads the 4th line of the file cause arrays start at 0

#the txt file whare parts are saved.
Parts_list_file:str = str(Master_file_content[9])
Parts_list_file = str(Parts_list_file.strip('\n'))
Parts_list_file = os.path.join(log_directory, Parts_list_file)

#whare to store the message_log
message_log:str = "message_log"
message_log = str(message_log.strip('\n'))
message_log = os.path.join(log_directory, message_log)

# this is the google sheets link that the bot puts the requested parts in.
gsheets_parts_list:str = str(Master_file_content[15])

#for the email list
email_file = open("setup\email_list.txt")
email_list = email_file.readlines()
email_list.pop(0) #removes the instrions on the first line

#this is for the email and password
sender = str(Master_file_content[17])
sender = str(sender.strip('\n'))

password = str(Master_file_content[19])
password = str(password.strip('\n'))

#This is the role id that allows certin commands to be used.
ROLE_ID:int = int(Master_file_content[11])

#this is whare the bot will upload the file
channel_id = int(Master_file_content[13])

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
    # Fetch the guild (server) and the role
    guild = interaction.guild
    role = guild.get_role(ROLE_ID)
    
    if role is None:
        await interaction.response.send_message(f"Role with ID {ROLE_ID} not found.", ephemeral=False)
        return
    
    name = convert_userid_to_name(interaction.user.id)
    message = f"{name} requested we buy this part: {argument}"
    
    #for google docs right now is disabled
    add_row_to_sheet(gsheets_parts_list,message)

    # Create part lists
    with open(Parts_list_file, 'a') as f:
        f.write(f"{message}\n")
    
    # Send a message to each member with the role
    if send_to_users == True:
        for member in role.members:
            try:
                await member.send(message)
            except discord.Forbidden:
                await interaction.channel.send(f"Could not send a message to {member.mention}.", delete_after=10)
        
    await interaction.response.send_message(f"Message sent to all members with the role {role.name} and added to the google sheets.", ephemeral=False)

# Define the slash command for uploading the request log
@tree.command(
    name="upload-parts-list",
    description="Uploads the request txt file"
)
async def upload_command(interaction: discord.Interaction):
    guild = interaction.guild
    channel = guild.get_channel(channel_id)  # Replace CHANNEL_ID with your channel ID

    with open(Parts_list_file, 'rb') as fp:
        await channel.send(file=discord.File(fp, "Parts_list_file"))
    
    await interaction.response.send_message("Request log uploaded.", ephemeral=False)

#allows and disalows the bot to send dms
@tree.command(
    name="help",
    description="Makes it so the bot will either dm when some one requests a part or wont"
)
async def Help(interaction: discord.Interaction):
    
    await interaction.response.send_message(f"ahh sorry code is currently broken gotta change it in the set up file", ephemeral=True)

# Define the slash command for emailing the part list
@tree.command(
    name="email_partslist",
    description="Emails the part list to the adult and youth team leads"
)
async def Email_people(interaction: discord.Interaction):
    Email_people_func(Parts_list_file,email_list,sender,password)
    await interaction.response.send_message("Sent the email", ephemeral=False)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user}")

#Auto mod
log_messages:bool = bool(Master_file_content[21])
@bot.event
async def on_message(message):
    if message.author == bot.user:  # Check if the author of the message is the bot itself
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    #planed to be part of the auto mod currently unused
    if log_messages:
        with open(message_log, 'a') as f:
            f.write(f"{message.author.name}: {message.content}\n")

bot.run(Bot_token)