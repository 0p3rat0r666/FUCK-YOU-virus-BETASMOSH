import sysimport winsound

from colorama import Fore, Style

logo = f"""
{Fore.YELLOW}THIS IS THE FUCK YOU VIRUS. FUCK YOU.{Fore.YELLOW}
     ___
     | |
    _| |__
   /|   ' |
   \|_____|
"""

print(logo)
winsound.PlaySound('sound.wav', winsound.SND_FILENAME) # figure out how to do this err
