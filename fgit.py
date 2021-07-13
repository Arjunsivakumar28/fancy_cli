from plumbum import cli
from pyfiglet import Figlet
from plumbum.cmd import ls

def print_banner(text):
    print(Figlet(font='slant').renderText(text))

def get_files():
    ls_output = ls()
    print("start", ls_output, "end")
    return []

class FancyGitAdd(cli.Application):
    VERSION = "1.1"

    def main(self):
        print_banner("Git Fancy add")

if __name__ == "__main__":
    FancyGitAdd()