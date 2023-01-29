from requests import Session
from urllib import parse
import json


class ViaCepException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ViaCep:
    def __init__(
        self, base_url: str = "https://viacep.com.br/ws", encoding: str = "UTF-8"
    ) -> None:
        super().__init__()
        self.base_url = base_url
        self.__encoding = encoding
        self.__session = Session()

    def __decode(self, data: bytes):
        return json.loads(data.decode(self.__encoding))

    def cep(self, cep: str):
        endpoint = self.base_url + f"/{cep}/json"
        ret = self.__session.get(endpoint)
        if ret.status_code != 200:
            raise ViaCepException(f"Viacep API Error: {ret.status_code}")
        return self.__decode(ret.content)
