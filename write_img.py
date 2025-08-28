
from requests import get as rget
from requests import Response
from requests.exceptions import SSLError

from time import sleep

from asyncio import run, Task, to_thread, create_task
from collections.abc import Coroutine

class Kamio:
    def __init__(self, url: str, img_path: str) -> None:
        self.img_path: str = img_path
        self.url = url
        self.current_image: bytes | None = None

    async def get_img(self) -> None:
        try:
            response: Response = await to_thread(rget, self.url)
            if response.status_code == 200:
                self.current_image = response.content

                with open(self.img_path, "wb") as img_handle:
                    img_handle.write(self.current_image)
                print(response.status_code)
            else:
                with open(self.img_path, "rb") as img_handle:
                    print(f"Failed to fetch from server with response {response.status_code}")
                    self.current_image = img_handle.read()
        except SSLError:
            print("Too many requests, sleeping for a bit")
            with open(self.img_path, "rb") as img_handle:
                self.current_image = img_handle.read()
            sleep(10)




def main() -> None:
    kam_obj: Kamio = Kamio("https://www-sk.icrr.u-tokyo.ac.jp/realtimemonitor/skev.gif", './img/skev.gif')

    kam_obj.get_img()

    print(kam_obj.current_image)

if __name__ == "__main__":
    main()