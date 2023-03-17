from onecmd_sys.command import get_cmdfile
from onecmd_sys.command import run
from cleo.application import Application

def main():
    application = Application()
    application.add(get_cmdfile.get())
    application.add(run.run())
    application.run()