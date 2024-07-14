import discord
from discord import app_commands
from discord.ext import commands
from convert_name_function import convert_userid_to_name
from Email_function import Email_people_func
from googledocsfunc import add_row_to_sheet

#this is the file that containes all passwords and other settings
Master_file = open("Importentfile.txt")

#and this puts it so that i can read it as an list
Master_file_content = Master_file.readlines()

#This is the bot token
Bot_token:str = str(Master_file_content[3]) #reads the 4th line of the file cause arrays start at 0

#the txt file whare parts are saved.
Parts_list_file = Master_file_content[10]

# this is the google sheets link that the bot puts the requested parts in.
gsheets_parts_list = ''

#This is the role id that allows certin commands to be used.
ROLE_ID:int = None

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
        await interaction.response.send_message(f"Role with ID {ROLE_ID} not found.", ephemeral=True)
        return
    
    name = convert_userid_to_name(interaction.user.id)
    message = f"{name} requested we buy this part: {argument}"
    
    #for google docs
    add_row_to_sheet(gsheets_parts_list,message)

    # Create part lists
    with open('Part list.txt', 'a') as f:
        f.write(f"{message}\n")
    
    # Send a message to each member with the role
    for member in role.members:
        try:
            await member.send(message)
        except discord.Forbidden:
            await interaction.channel.send(f"Could not send a message to {member.mention}.", delete_after=10)
    
    await interaction.response.send_message(f"Message sent to all members with the role {role.name} and added to the google sheets.", ephemeral=True)

# Define the slash command for uploading the request log
@tree.command(
    name="upload",
    description="Uploads the request txt file"
)
async def upload_command(interaction: discord.Interaction):
    guild = interaction.guild
    channel = guild.get_channel(1210415444037603359)  # Replace CHANNEL_ID with your channel ID

    with open('Part list.txt', 'rb') as fp:
        await channel.send(file=discord.File(fp, 'Part list.txt'))
    
    await interaction.response.send_message("Request log uploaded.", ephemeral=True)

# Define the slash command for emailing the part list
@tree.command(
    name="email_partslist",
    description="Emails the part list to the adult and youth team leads"
)
async def Email_people(interaction: discord.Interaction):
    Email_people_func(Parts_list_file)
    await interaction.response.send_message("Sent the email", ephemeral=True)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user}")

#Auto mod
@bot.event
async def on_message(message):
    if message.author == bot.user:  # Check if the author of the message is the bot itself
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    #planed to be part of the auto mod currently unused
    if False:
        with open('message_log.txt', 'a') as f:
            f.write(f"{message.author.name}: {message.content}\n")

#put the token blow this and yes i know hard coded tokens are bad but im lazy
bot.run(Bot_token)
