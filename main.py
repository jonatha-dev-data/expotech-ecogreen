from conexao import conectar, limpar_tela, pausar
import crud_fazendaaaaaaaaa as crud 

def menu_fazendas(conexao):
    while True:
        limpar_tela()
        print("=== GERENCIAR FAZENDAS ===")
        print("1 - Cadastrar Fazenda")
        print("2 - Listar Fazendas")
        print("3 - Atualizar Estoque")
        print("4 - Remover Fazenda")
        print("0 - Voltar")
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            nome = input("Nome da Fazenda: ")
            estoque = float(input("Estoque Inicial: "))
            cnpj = input("CNPJ da Fazenda: ")
            crud.criar_fazenda(conexao, nome, estoque, cnpj)
            pausar()
        elif op == "2":
            fazendas = crud.listar_fazendas(conexao)
            print("\n--- FAZENDAS CADASTRADAS ---")
            for f in fazendas:
                print(f"ID: {f[0]} | Nome: {f[1]} | Estoque: {f[2]} | CNPJ: {f[3]}")
            pausar()
        elif op == "3":
            id_f = int(input("ID da Fazenda que deseja atualizar: "))
            novo_est = float(input("Novo valor de estoque: "))
            crud.atualizar_estoque(conexao, id_f, novo_est)
            pausar()
        elif op == "4":
            id_f = int(input("ID da Fazenda que deseja remover: "))
            crud.deletar_fazenda(conexao, id_f)
            pausar()
        elif op == "0":
            break

def menu_plantas(conexao):
    while True:
        limpar_tela()
        print("=== GERENCIAR CATÁLOGO DE PLANTAS ===")
        print("1 - Cadastrar Planta")
        print("2 - Listar Plantas")
        print("3 - Atualizar Nome da Planta")
        print("4 - Remover Planta")
        print("0 - Voltar")
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            nome = input("Nome da Planta: ")
            especie = input("Espécie da Planta: ")
            id_fazenda = int(input("ID da Fazenda associada: "))
            crud.criar_planta(conexao, nome, especie, id_fazenda)
            pausar()
        elif op == "2":
            plantas = crud.listar_planta(conexao)
            print("\n--- PLANTAS CADASTRADAS ---")
            for p in plantas:
                print(f"ID: {p[0]} | Nome: {p[1]} | Espécie: {p[2]} | ID Fazenda: {p[3]}")
            pausar()
        elif op == "3":
            id_p = int(input("ID da Planta que deseja atualizar: "))
            novo_nome = input("Novo nome da Planta: ")
            crud.atualizar_planta(conexao, id_p, novo_nome)
            pausar()
        elif op == "4":
            id_p = int(input("ID da Planta que deseja remover: "))
            crud.deletar_planta(conexao, id_p)
            pausar()
        elif op == "0":
            break

def menu_motoristas(conexao): # Ajustado de Transportadoras para Motoristas igual ao SQL
    while True:
        limpar_tela()
        print("=== GERENCIAR MOTORISTAS ===")
        print("1 - Cadastrar Motorista")
        print("2 - Listar Motoristas")
        print("3 - Atualizar Nome do Motorista")
        print("4 - Remover Motorista")
        print("0 - Voltar")
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            nome = input("Nome do Motorista: ")
            cnh = input("CNH do Motorista: ")
            telefone = input("Telefone do Motorista: ")
            crud.criar_transportadora(conexao, nome, cnh, telefone)
            pausar()
        elif op == "2":
            motoristas = crud.listar_transportadora(conexao)
            print("\n--- MOTORISTAS CADASTRADOS ---")
            for m in motoristas:
                print(f"ID: {m[0]} | Nome: {m[1]} | CNH: {m[2]} | Telefone: {m[3]}")
            pausar()
        elif op == "3":
            id_m = int(input("ID do Motorista para atualizar: "))
            novo_nome = input("Novo Nome: ")
            crud.atualizar_motorista(conexao, id_m, novo_nome)
            pausar()
        elif op == "4":
            id_m = int(input("ID do Motorista que deseja remover: "))
            crud.deletar_motorista(conexao, id_m)
            pausar()
        elif op == "0":
            break

def menu_hortifruti(conexao):
    while True:
        limpar_tela()
        print("=== GERENCIAR HORTIFRÚTIS ===")
        print("1 - Cadastrar Hortifrúti")
        print("2 - Listar Hortifrútis")
        print("3 - Atualizar Nome do Hortifrúti")
        print("4 - Remover Hortifrúti")
        print("0 - Voltar")
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            nome = input("Nome do Hortifrúti: ")
            cnpj = input("CNPJ: ")
            telefone = input("Telefone: ") # Batendo com a coluna telefone_hortifruti do seu SQL
            crud.criar_hortifruti(conexao, nome, cnpj, telefone)
            pausar()
        elif op == "2":
            hortis = crud.listar_hortifruti(conexao)
            print("\n--- HORTIFRÚTIS CADASTRADOS ---")
            for h in hortis:
                print(f"ID: {h[0]} | Nome: {h[1]} | CNPJ: {h[2]} | Telefone: {h[3]}")
            pausar()
        elif op == "3":
            id_h = int(input("ID do Hortifrúti que deseja atualizar: "))
            novo_nome = input("Novo nome do Hortifrúti: ")
            crud.atualizar_hortifruti(conexao, id_h, novo_nome)
            pausar()
        elif op == "4":
            id_h = int(input("ID do Hortifrúti que deseja remover: "))
            crud.deletar_hortifruti(conexao, id_h)
            pausar()
        elif op == "0":
            break

def menu_principal():
    conexao = conectar()
    if not conexao:
        print("Não foi possível iniciar o sistema sem conexão com o banco de dados MySQL.")
        return

    while True:
        limpar_tela()
        print("========================================")
        print("       EXOTECH AGRONEGÓCIO - SISTEMA")
        print("========================================")
        print("1 - Gerenciar Fazendas")
        print("2 - Gerenciar Catálogo de Plantas")
        print("3 - Gerenciar Motoristas")
        print("4 - Gerenciar Hortifrútis")
        print("5 - REGISTRAR ENVIO (Carga para Hortifrúti)")
        print("6 - Relatório de Envios Realizados")
        print("0 - Sair")
        print("========================================")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_fazendas(conexao)
        elif opcao == "2":
            menu_plantas(conexao)
        elif opcao == "3":
            menu_motoristas(conexao)
        elif opcao == "4":
            menu_hortifruti(conexao)
        elif opcao == "5":
            limpar_tela()
            print("=== REGISTRAR ENVIO ===")
            id_f = int(input("ID da Fazenda de Origem: "))
            id_h = int(input("ID do Hortifrúti de Destino: "))
            id_m = int(input("ID do Motorista: "))
            id_p = int(input("ID da Planta enviada: "))
            id_s = int(input("ID da Safra: "))
            qtd = float(input("Quantidade Enviada: "))
            crud.registrar_envio(conexao, id_f, id_h, id_m, id_p, id_s, qtd)
            pausar()
        elif opcao == "6":
            limpar_tela()
            print("=== RELATÓRIO DE ENVIOS REALIZADOS ===")
            envios = crud.relatorio_envios(conexao)
            for e in envios:
                print(f"Envio ID: {e[0]} | Origem: {e[1]} -> Destino: {e[2]} | Motorista: {e[3]} | Produto: {e[4]} | Qtd: {e[5]} | Data: {e[6]}")
            pausar()
        elif opcao == "0":
            print("\nSistema encerrado. Até logo!")
            conexao.close()
            break
        else:
            print("\nOpção inválida!")
            pausar()

if __name__ == "__main__":
    menu_principal()