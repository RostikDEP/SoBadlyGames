import requests


class Controller:
    def __init__(self):
        pass

    def CheckConnection(self) -> bool:
        return True if requests.get("https://google.com").status_code == 200 else False
