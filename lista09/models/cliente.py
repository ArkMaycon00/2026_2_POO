class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id: int):
        self.__id = id

    def set_nome(self, nome: str):
        if nome == "":
            raise ValueError("Nome inválido")
        self.__nome = nome

    def set_email(self, email: str):
        if email == "":
            raise ValueError("E-mail inválido")
        self.__email = email

    def set_fone(self, fone: str):
        if fone == "":
            raise ValueError("Telefone inválido")
        self.__fone = fone

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_fone(self) -> str:
        return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone
        }

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])
