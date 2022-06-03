from speedtest import *
from pprint import pprint
import colorama


download = 0
upload = 0
servers = 0

colorama.init()


def res_color():
    print(colorama.Style.RESET_ALL, end='')


try:
    a = Speedtest()
    servers = a.get_servers()
    servers = list(servers.values())

    print(colorama.Fore.GREEN, "All servers:\t\t\t\t")
    res_color()

    for item in servers:
        print(colorama.Fore.YELLOW, item[0]['sponsor'], end='\t')
    res_color()

    print(colorama.Fore.GREEN, "\nNearest server:\t\t\t\t")
    print(colorama.Fore.YELLOW, a.get_closest_servers()[0]['sponsor'])

    print(colorama.Fore.GREEN, "Calculation download...")
    res_color()
    download = a.download()

    print(colorama.Fore.GREEN, f"\t\t\tDOWNLOAD\n")

    print(colorama.Fore.MAGENTA, f"Bit/s:\t{download}\n"
                                 f"Mbit/s:\t{download / 1_000_000}\n"
                                 f"\t\t\tBYTES\n"
                                 f"SENT:\t{a.results.bytes_sent}\n"
                                 f"RECEIVED:\t{a.results.bytes_received}\n")

    print(colorama.Fore.GREEN, "Calculating upload...")
    upload = a.upload()

    print(colorama.Fore.GREEN, f"\t\t\tUPLOAD\n")

    print(colorama.Fore.MAGENTA, f"Bit/s:\t{upload}\n"
                                 f"Mbit/s:\t{upload / 1_000_000}\n"
                                 f"\t\t\tBYTES\n"
                                 f"SENT:\t{a.results.bytes_sent}\n"
                                 f"RECEIVED:\t{a.results.bytes_received}\n")

    print(colorama.Fore.GREEN, "PING:", a.results.ping)
except:
    print(colorama.Fore.RED, "Error... Something get wrong")
