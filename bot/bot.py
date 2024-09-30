from typing import Final
import asyncio
from discord import Intents, Client, Message, File
from dotenv import load_dotenv
from downloader.downloader.py import download_video
import os
import re

load_dotenv()
TOKEN:Final[str] = os.getenv('DISCORD_TOKEN2')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
standby_message = "Trying to get that video for you"
error_message = "An error eccured getting your video, sorry :("

domain_check_list = ["reddit", "instagram","twitter", "tiktok"] # // Temporary list of a domain where a video extraction will happen // 

def is_link(user_input:str):
    
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    url_match = url_pattern.search(user_input)
    
    if url_match:
        link = url_match.group(0)
        return link
    else:
        return None
    
def is_in_list(url:str) -> bool:
    for domain in domain_check_list:
        if domain in url:
            return True
        else:
            return None

async def handle_received_message(message:Message, user_message:str) -> str:
    link = is_link(user_message)
    if not link or not is_in_list(link):
        return None
    else:
        try:
            standby_message = await message.channel.send(standby_message)
            file_path = download_video(link)
            if file_path:
                standby_message.delete()
                return file_path
        
        except Exception as e:
            print(e)
            await standby_message.delete()
            error_message = await message.channel.send(error_message) 
            await asyncio.sleep(5)
            await error_message.delete()
    

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
  
    if file_path: 
        try:
            with open(file_path, 'rb') as f:
                await message.channel.send(file=File(f))
                
            os.remove(file_path)
        except Exception as e:
            print(f"An error occured\n{e}")
            error_message = await message.channel.send(error_message)
            await asyncio.sleep(5)
            await error_message.delete()
            
    
def activate_bot() -> None:
    client.run(token=TOKEN)
    
activate_bot()



    
    
    


     
    
    
    
    
    

# def main() -> None:
#     Client.run(token=TOKEN)