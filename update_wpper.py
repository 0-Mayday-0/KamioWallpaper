import ctypes
from write_img import Kamio
from time import sleep
from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')

def perma_update(absolute_path: str) -> None:
    kam_obj: Kamio = Kamio(getenv("URL"), getenv("RELATIVE_PATH"))
    while True:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 0)
        sleep(4)
        kam_obj.get_img()

def main():
    perma_update(getenv("ABSOLUTE_PATH"))

main()