from cleo.commands.command import Command
from cleo.helpers import argument, option
import requests
import logging, os, requests, sys, time
import itertools
import threading
import json

def loading():
    global done

    done = False
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done == True:
            break
        sys.stdout.write('\rConnecting... ' + c )
        time.sleep(0.1)

def write(filename, data):
    path = __file__
    if not os.path.exists(path.replace('onecmd_sys\command\get_cmdfile.py', 'extensions')):
        os.makedirs(path.replace('onecmd_sys\command\get_cmdfile.py', 'extensions'))
    with open(__file__.replace('onecmd_sys\command\get_cmdfile.py', 'extensions') + f"\{filename}.json", "w") as f:
        print(__file__.replace('onecmd_sys\command\get_cmdfile.py', 'extensions'))
        dt = data
        f.write(dt.replace("'", '"'))

    print("Installed.")

class get(Command):
    name = "get"
    description = "add onecmd file"
    arguments = [
        argument(
            "name",
            description="file name",
            optional=False
        ),
        argument(
            "url",
            description="To change the index file reference location, enter the URL of the index file here.",
            optional=True
        )
    ]


    def handle(self):
        global done
        name = self.argument("name")
        url = self.argument("url")
        if url:
            t = threading.Thread(target=loading)
            t.start()
            resp = requests.get(url)
            json1 = resp.json()
            try:
                jurl = json1[name]["link"]
            except KeyError:
                print("NotFound.")
            done = True
            resp2 = requests.get(jurl)
            json3 = resp2.json()
            write(filename=name, data=str(json3))
        else:
            t = threading.Thread(target=loading)
            t.start()
            url = "https://raw.githubusercontent.com/sakurapkg/onecmd/index/index.json"
            resp = requests.get(url)
            json1 = resp.json()
            try:
                jurl = json1[name]["link"]
            except KeyError:
                print("NotFound.")
            done = True
            resp2 = requests.get(jurl)
            json3 = resp2.json()
            write(filename=name, data=str(json3))