from typing import Final
from discord import Intents, Client, Message, File
from dotenv import load_dotenv
import os

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