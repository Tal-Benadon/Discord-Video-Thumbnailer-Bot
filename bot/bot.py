import asyncio
from discord import Intents, Client, Message, File
import os
import re
import json
from downloader.downloader import download_video
providers_json_path = os.path.join(os.path.dirname(__file__), '..','providers.json')
with open(providers_json_path, 'r') as json_file:
    providers = json.load(json_file)
    
print(providers)

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
standby_message = "Trying to get that video for you"
error_message = "An error eccured getting your video, sorry :("

def is_link(user_input:str):
    
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    url_match = url_pattern.search(user_input)
    
    if url_match:
        link = url_match.group(0)
        return link
    else:
        return None
    
def is_in_list(url:str) -> bool:
    return any(domain in url for domain in providers )
 

async def handle_received_message(message:Message, user_message:str) -> str:
    
    link = is_link(user_message)
    if not link or not is_in_list(link):
        return None
    else:
        try:
            sent_standby_message = await message.channel.send(standby_message)
            file_path = download_video(link)
            if file_path:
                await sent_standby_message.delete()
                return file_path
        except Exception as e:
            print("not a video DEBUG") 
            return None
        
  
    

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
    
    try:
        file_path = await handle_received_message(message, user_message)
    except Exception as e:
        print("Error occured")
    if file_path: 
        try:
            with open(file_path, 'rb') as f:
                await message.channel.send(file=File(f))
                
            os.remove(file_path)
        except Exception as e:
            print(f"An error occured\n{e}")
            sent_error_message = await message.channel.send(error_message)
            await asyncio.sleep(5)
            await sent_error_message.delete()