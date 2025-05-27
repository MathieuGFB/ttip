"""RP TTiP entry point script"""
# ttip/__main__.py

from ttip import cli, __app_name__

def main():
    cli.app(prog_name = __app_name__)

if __name__ == "__main__":
    main()