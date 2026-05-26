def criar_fazenda(conexao, nome, estoque, cnpj):
    cursor = conexao.cursor()
    sql = """
    INSERT INTO tbl_fazenda (nome_fazenda, estoque_fazenda, cnpj_fazenda)
    VALUES (%s, %s, %s);
    """
    cursor.execute(sql, (nome, estoque, cnpj))
    conexao.commit()
    cursor.close()
    print(f" Fazenda '{nome}' cadastrada com sucesso!")

def listar_fazendas(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_fazenda;")
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def atualizar_estoque(conexao, id_fazenda, novo_estoque):
    cursor = conexao.cursor()
    sql = "UPDATE tbl_fazenda SET estoque_fazenda = %s WHERE id_fazenda = %s;"
    cursor.execute(sql, (novo_estoque, id_fazenda))
    conexao.commit()
    cursor.close()
    print(f" Estoque da fazenda ID {id_fazenda} atualizado para {novo_estoque}!")

def deletar_fazenda(conexao, id_fazenda):
    cursor = conexao.cursor()
    sql = "DELETE FROM tbl_fazenda WHERE id_fazenda = %s;"
    cursor.execute(sql, (id_fazenda,))
    conexao.commit()
    cursor.close()
    print(f" Fazenda ID {id_fazenda} removida do sistema!")

def criar_transportadora(conexao, nome, cnh, telefone):
    cursor = conexao.cursor()
    sql = """
    INSERT INTO tbl_motorista (nome_motorista, cnh_motorista, telefone_motorista) 
    VALUES (%s, %s, %s);
    """
    cursor.execute(sql, (nome, cnh, telefone))
    conexao.commit()
    cursor.close()
    print(f"Motorista {nome} cadastrado com sucesso!")

def listar_transportadora(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbl_motorista;')
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def atualizar_motorista(conexao, id_motorista, novo_nome):
    cursor = conexao.cursor()
    sql = 'UPDATE tbl_motorista SET nome_motorista = %s WHERE id_motorista = %s;'
    cursor.execute(sql, (novo_nome, id_motorista))
    conexao.commit()
    cursor.close()
    print(f'Dados do motorista ID {id_motorista} atualizados para: {novo_nome}')

def deletar_motorista(conexao, id_motorista):
    cursor = conexao.cursor()
    sql = 'DELETE FROM tbl_motorista WHERE id_motorista = %s;'
    cursor.execute(sql, (id_motorista,))
    conexao.commit()
    cursor.close()
    print(f'Motorista ID {id_motorista} removido do sistema')

def criar_hortifruti(conexao, nome, cnpj, telefone):
    cursor = conexao.cursor()
    sql = """
    INSERT INTO tbl_hortifruti (nome_hortifruti, cnpj_hortifruti, telefone_hortifruti)
    VALUES (%s, %s, %s);
    """
    cursor.execute(sql, (nome, cnpj, telefone))
    conexao.commit()
    cursor.close()
    print(f"Hortifrúti {nome} cadastrado com sucesso!")

def listar_hortifruti(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbl_hortifruti;')
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def atualizar_hortifruti(conexao, id_hortifruti, novo_nome):  
    cursor = conexao.cursor()
    sql = 'UPDATE tbl_hortifruti SET nome_hortifruti = %s WHERE id_hortifruti = %s;'
    cursor.execute(sql, (novo_nome, id_hortifruti))
    conexao.commit()
    cursor.close()
    print(f"Hortifrúti ID {id_hortifruti} atualizado para {novo_nome}")

def deletar_hortifruti(conexao, id_hortifruti):    
    cursor = conexao.cursor()
    sql = 'DELETE FROM tbl_hortifruti WHERE id_hortifruti = %s;'
    cursor.execute(sql, (id_hortifruti,))
    conexao.commit()
    cursor.close()
    print(f'Hortifrúti ID {id_hortifruti} removido do sistema')

def criar_planta(conexao, nome, especie, id_fazenda):
    cursor = conexao.cursor()
    sql = """
    INSERT INTO tbl_planta (nome_planta, especie_planta, id_fazenda)
    VALUES (%s, %s, %s);
    """
    cursor.execute(sql, (nome, especie, id_fazenda))
    conexao.commit()
    cursor.close()
    print(f"Planta {nome} cadastrada com sucesso!")

def listar_planta(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbl_planta;')
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def atualizar_planta(conexao, id_planta, nome_planta):
    cursor = conexao.cursor()
    sql = 'UPDATE tbl_planta SET nome_planta = %s WHERE id_planta = %s;'
    cursor.execute(sql, (nome_planta, id_planta))
    conexao.commit()
    cursor.close()
    print(f'Planta ID {id_planta} atualizada para {nome_planta}')

def deletar_planta(conexao, id_planta):
    cursor = conexao.cursor()
    sql = 'DELETE FROM tbl_planta WHERE id_planta = %s;'
    cursor.execute(sql, (id_planta,))
    conexao.commit()
    cursor.close()
    print(f'Planta ID {id_planta} removida do sistema')


def criar_safra(conexao, nome_safra, ano, semestre):    
    cursor = conexao.cursor()
    sql = """
    INSERT INTO tbl_safra(nome_safra, ano, semestre)
    VALUES (%s, %s, %s);
    """
    cursor.execute(sql, (nome_safra, ano, semestre))
    conexao.commit()
    cursor.close()
    print(f'Safra {nome_safra} cadastrada com sucesso')

def listar_safra(conexao):    
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbl_safra;')
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def atualizar_safra(conexao, id_safra, nome_safra):    
    cursor = conexao.cursor()
    sql = 'UPDATE tbl_safra SET nome_safra = %s WHERE id_safra = %s;'
    cursor.execute(sql, (nome_safra, id_safra))
    conexao.commit()   
    cursor.close()
    print(f'Safra ID {id_safra} atualizada para {nome_safra}')

def deletar_safra(conexao, id_safra):    
    cursor = conexao.cursor()
    sql = 'DELETE FROM tbl_safra WHERE id_safra = %s;'
    cursor.execute(sql, (id_safra,))
    conexao.commit()
    cursor.close()
    print(f'Safra ID {id_safra} removida do sistema')

def registrar_envio(conexao, id_f, id_h, id_m, id_p, id_s, qtd):
    cursor = conexao.cursor()
    sql = """
    INSERT INTO tbl_envio (id_fazenda, id_hortifruti, id_motorista, id_planta, id_safra, quantidade_enviada)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    cursor.execute(sql, (id_f, id_h, id_m, id_p, id_s, qtd))
    conexao.commit()
    cursor.close()
    print(" Envio registrado com sucesso!")

def relatorio_envios(conexao):
    cursor = conexao.cursor()
    sql = """
    SELECT 
        e.id_envio, f.nome_fazenda, h.nome_hortifruti, m.nome_motorista, 
        p.nome_planta, e.quantidade_enviada, e.data_envio
    FROM tbl_envio e
    JOIN tbl_fazenda f ON e.id_fazenda = f.id_fazenda
    JOIN tbl_hortifruti h ON e.id_hortifruti = h.id_hortifruti
    JOIN tbl_motorista m ON e.id_motorista = m.id_motorista
    JOIN tbl_planta p ON e.id_planta = p.id_planta;
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados
