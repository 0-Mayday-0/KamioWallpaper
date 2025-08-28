import ctypes
from write_img import Kamio
from time import sleep
from os import getenv
from dotenv import load_dotenv
from asyncio import run, Task, create_task

load_dotenv('.env')

async def perma_update(absolute_path: str) -> None:
    kam_obj: Kamio = Kamio(getenv("URL"), getenv("RELATIVE_PATH"))
    while True:
        get_img_task: Task[None] = create_task(kam_obj.get_img())
        await get_img_task
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 0)
        sleep(4)



async def main():
    await perma_update(getenv("ABSOLUTE_PATH"))

if __name__ == '__main__':
    run(main())