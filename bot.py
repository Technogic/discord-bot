import discord
import os
#from dotenv import load_dotenv
#from oauth2client.service_account import ServiceAccountCredentials

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
'''
# table data
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
gClient = gspread.authorize(creds)
'''
@client.event
async def on_ready():
    print('i\'m ready to get back to work')

@client.event
async def on_message(message):
    if message.content.startswith('$k2 about'):
        embed = discord.Embed(title='Thanks for adding me to your server! :heart:', description='To get started, simply share your google sheet with me at `mihir-462@tablot-280404.iam.gserviceaccount.com`, and type `$ts help` for a list of commands', colour=1499502)\
        .add_field(
            name='K2Tech Bot',
            value='K2-Bot helps you conveniently display your google sheets data on a discord server.',
            inline=False).add_field(
            name='Contribute',
            value='We gladly accept contributions. To get started, ' +
            'check out [Tablot\'s GitHub repo](https://github.com/techsyndicate/tablot).',
            inline=False
        ).set_footer(text='Made by Tech Syndicate', icon_url='https://techsyndicate.co/img/logo.png')
        await message.channel.send(embed=embed)

    if message.content.startswith("/help") :
        embed = discord.Embed(
        title="Tablot's commands:",
        colour=1499502,
        description="""
> To use a  command type `$ts <command>`.

**General**
`about` - To know about the bot.
`stats` - To check the bot's stats.

**Google Sheets **
`show "file name"` - To display the whole table
`show "file name" value` - To display rows of specific value
""")
        await message.channel.send(embed=embed)
client.run("NzQxMTc2NDk4Njg5NDA5MDk0.XyzwZw.f89LumDx_nQzBucmZrOVhyGkhRE")


