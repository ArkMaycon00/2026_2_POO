class Categoria:
    def __init__(self, id: int, descricao: str):
        self.set_id(id)
        self.set_descricao(descricao)

    def set_id(self, id: int):
        self.__id = id

    def set_descricao(self, descricao: str):
        if descricao == "":
            raise ValueError("Descrição inválida")
        self.__descricao = descricao

    def get_id(self) -> int:
        return self.__id

    def get_descricao(self) -> str:
        return self.__descricao

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao
        }

    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])
