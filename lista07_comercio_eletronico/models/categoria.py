class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)

    def set_id(self, id):
        if not isinstance(id, int) or id < 0:
            raise ValueError("Id deve ser um inteiro positivo")
        self.__id = id

    def set_descricao(self, descricao):
        if not isinstance(descricao, str) or not descricao.strip():
            raise ValueError("Descrição deve ser informada")
        self.__descricao = descricao.strip()

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao

    def to_json(self):
        return {"id": self.__id, "descricao": self.__descricao}

    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
