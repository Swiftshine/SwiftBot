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

        command: str = message.content

        if (not message.content.startswith("-s ")) and (not message.content.startswith("-S ")): return 

        do_ping: bool = False
        if command.startswith("-S "): do_ping = True


        command = command.replace("-s ", "").replace("-S ", "")


        if "ping" == command:
            await message.reply("pong!", mention_author = do_ping)
            print(f"User " + Fore.CYAN + f"{message.author}" + Style.RESET_ALL + " used the " + Fore.GREEN + "ping" + Style.RESET_ALL + " command", end = "\n\n")
            return
        
        if command.startswith("get-file"):
            # check if syntax is valid
            if "get-file" == command:
                await message.reply("please specify a file", mention_author = do_ping)
                return
            
            index = command.find(" ")
            filename = command[index + 1 : ]
            filename.strip("..")
            print(f"User " + Fore.CYAN + f"{message.author}" + Style.RESET_ALL + " used the " + Fore.GREEN + "get-file" + Style.RESET_ALL + " command for file " + Fore.GREEN + f"{filename}" + Style.RESET_ALL, end = "\n\t")

            if not os.path.exists("files/" + filename):
                await message.reply(f"the filename **{filename}** doesn't exist", mention_author = do_ping)
                print(Fore.RED + f"Failed. File {filename} does not exist." + Style.RESET_ALL)
                return
            
            try:
                await message.reply(file = discord.File("files/" + filename), mention_author = do_ping)
            except discord.errors.Forbidden:
                print(Fore.RED + "Failed. Forbidden." + Style.RESET_ALL)
                await message.reply("Failed. Forbidden.", mention_author = do_ping)
                return
            except discord.errors.HTTPException:
                print(Fore.RED + f"Failed. File too large." + Style.RESET_ALL)
                await message.reply("Failed. File needs to be less than 25 megabytes.", mention_author = do_ping)
                return
            return

        if command == "source-code":
            await message.reply("https://github.com/Swiftshine/SwiftBot", mention_author = do_ping)
            return