import datetime
import enum
import colorama
import data

from const import file_logging

class Type(enum.Enum):
    important = 0
    done = 1
    err = 2
    info = 3
    warn = 4


class Logger:

    file = None

    def __init__(self):
        if file_logging:
            path = data.LOG_FILE_PATH.split(".")[0] + '.' + \
                   str(datetime.datetime.now()).split(".")[0].replace(" ", "_").replace(":", ".")\
                   + '.' + data.LOG_FILE_PATH.split(".")[1]
            self.file = open(path, "w")

    @staticmethod
    def calculate(type_p) -> colorama.Fore:
        match type_p:
            case 0:
                return colorama.Fore.CYAN
            case 1:
                return colorama.Fore.GREEN
            case 2:
                return colorama.Fore.RED
            case 3:
                return colorama.Fore.BLUE
            case 4:
                return colorama.Fore.YELLOW
            case _:
                return colorama.Fore.MAGENTA

    def log(self, type_print, text) -> None:
        print(self.calculate(type_print), f" >\t{text}\"", end="")
        if file_logging:
            self.file.write(f" >\t{text}\n")

    def logl(self, type_print, text) -> None:
        print(self.calculate(type_print), f" >\t{text}", end='\n')
        if file_logging:
            self.file.write(f" >\t{text}\n")

    def log_w(self, type_print, text) -> None:
        print(self.calculate(type_print), f"  >>\t{text}", end="")
        if file_logging:
            self.file.write(f"  >>\t{text}\n")

    def logl_w(self, type_print, text) -> None:
        print(self.calculate(type_print), f"  >>\t{text}", end='\n')
        if file_logging:
            self.file.write(f"  >>\t{text}\n")
