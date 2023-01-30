from models.database import SenseDB
from viacep import ViaCep
from datetime import datetime
from psycopg2.errors import UniqueViolation
import json


class CepLocationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UniqueCepLocationError(CepLocationError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UFCepLocationError(CepLocationError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Location:
    def __init__(self, cep: str) -> None:
        super().__init__()
        self.viacep = ViaCep()
        self.cep_str = cep
        self.__viacep_ret = self.viacep.cep(self.cep_str)
        self.cep = self.__viacep_ret["cep"]
        self.uf = self.__viacep_ret["uf"]
        self.localidade = self.__viacep_ret["localidade"]
        self.logradouro = self.__viacep_ret["logradouro"]
        self.data_consulta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return json.dumps(
            {
                "cep": self.cep,
                "uf": self.uf,
                "localidade": self.localidade,
                "logradouro": self.logradouro,
                "data_consulta": self.data_consulta,
            },
            indent=4,
            default=str,
        )


class CepLocation:
    UFs = [
        "RO",
        "AC",
        "AM",
        "RR",
        "PA",
        "AP",
        "TO",
        "MA",
        "PI",
        "CE",
        "RN",
        "PB",
        "PE",
        "AL",
        "SE",
        "BA",
        "MG",
        "ES",
        "RJ",
        "SP",
        "PR",
        "SC",
        "RS",
        "MS",
        "MT",
        "GO",
        "DF",
    ]

    def __init__(self) -> None:
        self.__db = SenseDB

    def list(self, uf: str = None):
        filter_str = ""
        filters = []

        if uf:
            if uf.upper() not in CepLocation.UFs:
                raise UFCepLocationError("UF inválida.")
            filters.append(f""" "uf" = '{uf}' """)

        if filters:
            filter_str = "where " + " and ".join(filters)

        sql = f"""
            select
                "cep",
                "uf",
                "localidade",
                "logradouro",
                TO_CHAR("data_consulta", '{self.__db.date_format()}') as "data_consulta"
            from cep_location
            {filter_str}
        """
        self.__db.execute_sql(sql)
        return self.__db.fetch()

    def save(self, location: Location):
        sql = f"""
            insert into cep_location
                ("cep",
                "uf",
                "localidade",
                "logradouro",
                "data_consulta")
            values {location.cep, location.uf, location.localidade, location.logradouro, location.data_consulta};
        """
        try:
            self.__db.execute_sql(sql)
        except UniqueViolation as e:
            self.__db.rollback()
            raise UniqueCepLocationError("Cep já cadastrado.")
        self.__db.commit()
