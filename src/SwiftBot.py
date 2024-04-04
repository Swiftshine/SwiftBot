import os, sys
import discord
import colorama
from colorama import Fore, Style

class SwiftBotClient(discord.Client):
    async def on_ready(self):
        print(Fore.CYAN + f"ON_READY: {self.user}" + Style.RESET_ALL + " is connected to the following guilds: ")

        for guild in self.guilds:
            print(Fore.CYAN + f"{guild.name}" + Style.RESET_ALL+ " (ID: " + Fore.CYAN + f"{guild.id}" + Style.RESET_ALL + ")")

        print(Fore.GREEN + f"ON_READY: {self.user} is online.\n" + Style.RESET_ALL)
    
    async def on_message(self, message: discord.Message):
        if message.author == self.user: return

        if message.content == ";ping;":
            await message.reply("pong!", mention_author = False)
            print(f"User " + Fore.CYAN + f"{message.author}" + Style.RESET_ALL + " used the " + Fore.GREEN + "ping" + Style.RESET_ALL + " command\n")
            return
        
        if message.content.startswith(";get-file;"):
            if message.content == ";get-file;" or message.content == ";get-file; ":
                await message.reply("you need to specify a file", mention_author = False)
                return

            index = message.content.find(" ")
            filename = message.content[index + 1:]
            filename.strip("..")
            print(f"User " + Fore.CYAN + f"{message.author}" + Style.RESET_ALL + " used the " + Fore.GREEN + "get-file" + Style.RESET_ALL + " command for file " + Fore.GREEN + f"{filename}" + Style.RESET_ALL)


            if not os.path.exists("files/" + filename):
                await message.reply(f"the file {filename} doesn't exist", mention_author = False)
                print(Fore.RED + f"Failed. File {filename} does not exist.\n" + Style.RESET_ALL)
                return

            try:
                await message.reply(file=discord.File("files/" + filename), mention_author = False)
            except discord.errors.Forbidden:
                await message.reply(f"couldn't send file")
                print(Fore.RED + f"Failed. Forbidden.\n" + Style.RESET_ALL)
                return
            
            print(Fore.GREEN + "Succeeded.\n" + Style.RESET_ALL)
            return
        

        if message.content == ";github;":
            await message.reply("https://github.com/Swiftshine/SwiftBot", mention_author = False)
            return