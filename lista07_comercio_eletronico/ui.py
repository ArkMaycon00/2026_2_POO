from service import Service


class UI:
    @staticmethod
    def main():
        op = -1
        while op != 0:
            try:
                op = UI.menu()
                if op == 1: UI.cliente_inserir()
                elif op == 2: UI.cliente_listar()
                elif op == 3: UI.cliente_atualizar()
                elif op == 4: UI.cliente_excluir()
                elif op == 5: UI.categoria_inserir()
                elif op == 6: UI.categoria_listar()
                elif op == 7: UI.categoria_atualizar()
                elif op == 8: UI.categoria_excluir()
                elif op == 9: UI.produto_inserir()
                elif op == 10: UI.produto_listar()
                elif op == 11: UI.produto_atualizar()
                elif op == 12: UI.produto_excluir()
                elif op == 13: UI.produto_reajustar()
                elif op == 0: print("Aplicação finalizada.")
                else: print("Opção inválida.")
            except (ValueError, TypeError) as erro:
                print(f"Erro: {erro}")
            except KeyboardInterrupt:
                print("\nAplicação finalizada.")
                break

    @staticmethod
    def menu():
        print("\n===== SISTEMA DE COMÉRCIO ELETRÔNICO =====")
        print("CLIENTES:  1-Inserir  2-Listar  3-Atualizar  4-Excluir")
        print("CATEGORIAS: 5-Inserir  6-Listar  7-Atualizar  8-Excluir")
        print("PRODUTOS:  9-Inserir 10-Listar 11-Atualizar 12-Excluir")
        print("13-Reajustar preço de todos os produtos")
        print("0-Finalizar")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Telefone: ")
        Service.cliente_inserir(nome, email, fone)
        print("Cliente cadastrado.")

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Id do cliente: "))
        if Service.cliente_listar_id(id) is None:
            print("Cliente não encontrado.")
            return
        Service.cliente_atualizar(id, input("Novo nome: "),
                                  input("Novo e-mail: "), input("Novo telefone: "))
        print("Cliente atualizado.")

    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Id do cliente: "))
        print("Cliente excluído." if Service.cliente_excluir(id) else "Cliente não encontrado.")

    @staticmethod
    def categoria_inserir():
        Service.categoria_inserir(input("Descrição: "))
        print("Categoria cadastrada.")

    @staticmethod
    def categoria_listar():
        for obj in Service.categoria_listar(): print(obj)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Id da categoria: "))
        if Service.categoria_listar_id(id) is None:
            print("Categoria não encontrada.")
            return
        Service.categoria_atualizar(id, input("Nova descrição: "))
        print("Categoria atualizada.")

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Id da categoria: "))
        print("Categoria excluída." if Service.categoria_excluir(id) else "Categoria não encontrada.")

    @staticmethod
    def produto_inserir():
        UI.categoria_listar()
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        id_categoria = int(input("Id da categoria: "))
        Service.produto_inserir(descricao, preco, estoque, id_categoria)
        print("Produto cadastrado.")

    @staticmethod
    def produto_listar():
        for obj in Service.produto_listar(): print(obj)

    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Id do produto: "))
        if Service.produto_listar_id(id) is None:
            print("Produto não encontrado.")
            return
        UI.categoria_listar()
        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: "))
        estoque = int(input("Novo estoque: "))
        id_categoria = int(input("Id da categoria: "))
        Service.produto_atualizar(id, descricao, preco, estoque, id_categoria)
        print("Produto atualizado.")

    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Id do produto: "))
        print("Produto excluído." if Service.produto_excluir(id) else "Produto não encontrado.")

    @staticmethod
    def produto_reajustar():
        percentual = float(input("Percentual (positivo = reajuste; negativo = promoção): "))
        Service.produto_reajustar(percentual)
        print("Preços atualizados.")

if __name__ == "__main__":
    UI.main()
