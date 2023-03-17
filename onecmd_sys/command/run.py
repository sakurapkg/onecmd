from cleo.commands.command import Command
from cleo.helpers import argument, option
import requests
import logging, os, requests, sys, time
import itertools
import threading
import json
from onecmd_sys.conf import colors
import subprocess

Color = colors.Color

class run(Command):
    name = "run"
    description = "run onecmd json file."
    arguments = [
        argument(
            "cmd",
            description="Name of json file for onecmd",
            optional=False
        )
    ]


    def handle(self):
        cmd = self.argument("cmd")
        path = __file__
        p2 = r"C:\Users\hm74c\OneDrive\デスクトップ\onecmd\extensions\echo.json"
        locate = os.path.exists(path.replace('onecmd_sys\\command\\run.py', f'extensions\\{cmd}.json'))
        if locate:
            try:
                with open(path.replace('onecmd_sys\\command\\run.py', f'extensions\\{cmd}.json'), 'r', encoding='utf-8') as f:
                    load = json.loads(f.read())
                    print(len(load["resp"]["run"]))
                    for i in range(len(load["resp"]["run"])):
                        subprocess.run(load["resp"]["run"][i]["cmd"], shell=True)
                    print(f"{Color.GREEN}[SUCCESS]{Color.RESET} The process of executing the command has ended successfully.")
            except (Exception, BaseException) as e:
                print(f"{Color.RED}[ERROR!]{Color.RESET} An error occurred in the process of onecmd executing the command: {e}")
        else:
            print(f"{Color.BLUE}[INFO]{Color.RESET} The short command {cmd} does not exist.")

        