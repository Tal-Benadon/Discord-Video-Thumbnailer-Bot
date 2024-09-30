from typing import Final
from discord import Intents, Client, Message, File
from dotenv import load_dotenv
import os
import re

domain_check_list = ["reddit", "instagram","twitter", "tiktok"] # // Temporary list of a domain where a video extraction will happen // 

def is_link(user_input:str):
    url_pattern = re.compile(r'hhtps?://\S+|www\.\S+')
    url_match = url_pattern.search(user_input)
    
    if url_match:
        url = url_match.group(0)
        return url

load_dotenv()
TOKEN:Final[str] = os.getenv('DISCORD_TOKEN2')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

@client.event
async def on_message(message: Message) -> None: 
    if message.author == client.user: # // if the bot is the one sending the message, do nothing. //
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    
    file_path = await handle_received_message(message, user_message)



    
    
    


     
    
    
    
    
    

# def main() -> None:
#     Client.run(token=TOKEN)