from SwiftBot import *
from dotenv import load_dotenv



def main():
    load_dotenv()
    colorama.init()
    
    TOKEN   = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True
    
    client  = SwiftBotClient(intents=intents)

    client.run(TOKEN)

if __name__ == "__main__": main()