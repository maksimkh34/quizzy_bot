import enum
import colorama


class Type(enum.Enum):
    important = 0
    done = 1
    err = 2
    info = 3
    warn = 4


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


def log(type_print, text) -> None:
    print(calculate(type_print), f" >\t{text}", end="")


def logl(type_print, text) -> None:
    print(calculate(type_print), f" >\t{text}", end='\n')


def log_w(type_print, text) -> None:
    print(calculate(type_print), f"  >>\t{text}", end="")


def logl_w(type_print, text) -> None:
    print(calculate(type_print), f"  >>\t{text}", end='\n')
