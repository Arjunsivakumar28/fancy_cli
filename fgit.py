from plumbum import cli

class FancyGitAdd(cli.Application):
    def main(self):
        print("Welcome to Fancy Git Add!")
if __name__ == "__main__":
    FancyGitAdd()