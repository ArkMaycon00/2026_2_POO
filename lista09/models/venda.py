from datetime import datetime


class Venda:
    def __init__(self, id: int, data: datetime = None, carrinho: bool = True, total: float = 0.0, id_cliente: int = 0):
        self.set_id(id)
        self.set_data(data if data is not None else datetime.now())
        self.set_carrinho(carrinho)
        self.set_total(total)
        self.set_id_cliente(id_cliente)

    def set_id(self, id: int):
        self.__id = id

    def set_data(self, data: datetime):
        self.__data = data

    def set_carrinho(self, carrinho: bool):
        self.__carrinho = carrinho

    def set_total(self, total: float):
        if total < 0:
            raise ValueError("Total inválido")
        self.__total = total

    def set_id_cliente(self, id_cliente: int):
        self.__id_cliente = id_cliente

    def get_id(self) -> int:
        return self.__id

    def get_data(self) -> datetime:
        return self.__data

    def get_carrinho(self) -> bool:
        return self.__carrinho

    def get_total(self) -> float:
        return self.__total

    def get_id_cliente(self) -> int:
        return self.__id_cliente

    def __str__(self):
        data_str = self.__data.strftime("%d/%m/%Y %H:%M") if isinstance(self.__data, datetime) else str(self.__data)
        return f"{self.__id} - {data_str} - Carrinho: {self.__carrinho} - Total: R$ {self.__total:.2f}"

    def to_json(self):
        data_str = self.__data.strftime("%Y-%m-%d %H:%M:%S") if isinstance(self.__data, datetime) else str(self.__data)
        return {
            "id": self.__id,
            "data": data_str,
            "carrinho": self.__carrinho,
            "total": self.__total,
            "id_cliente": self.__id_cliente
        }

    @staticmethod
    def from_json(dic):
        data = dic["data"]
        if isinstance(data, str):
            data = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        return Venda(dic["id"], data, dic["carrinho"], dic["total"], dic["id_cliente"])
