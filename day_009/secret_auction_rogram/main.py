import os


def clear():
    """
    Function to clear the terminal on windows, mac and
    linux for a better user experience.
    """
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Mac and Linux (here, os.name is 'posix')
    else:
        os.system('clear')
