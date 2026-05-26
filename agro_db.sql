CREATE DATABASE IF NOT EXISTS agro_db;
USE agro_db;

CREATE TABLE tbl_fazenda (
    id_fazenda INT PRIMARY KEY AUTO_INCREMENT,
    nome_fazenda VARCHAR(100) NOT NULL,
    estoque_fazenda DECIMAL(10,2) DEFAULT 0.00,
    cnpj_fazenda VARCHAR(18)
);

CREATE TABLE tbl_planta (
    id_planta INT PRIMARY KEY AUTO_INCREMENT,
    nome_planta VARCHAR(100) NOT NULL,
    especie_planta VARCHAR(100),
    id_fazenda INT,
    FOREIGN KEY (id_fazenda) REFERENCES tbl_fazenda(id_fazenda) ON DELETE SET NULL
);

CREATE TABLE tbl_hortifruti (
    id_hortifruti INT PRIMARY KEY AUTO_INCREMENT,
    nome_hortifruti VARCHAR(100) NOT NULL,
    cnpj_hortifruti VARCHAR(18),
    telefone_hortifruti VARCHAR(20)
);

CREATE TABLE tbl_motorista (
    id_motorista INT PRIMARY KEY AUTO_INCREMENT,
    nome_motorista VARCHAR(100) NOT NULL,
    cnh_motorista VARCHAR(20),
    telefone_motorista VARCHAR(20)
);


CREATE TABLE tbl_safra (
    id_safra INT PRIMARY KEY AUTO_INCREMENT,
    nome_safra VARCHAR(50) NOT NULL, 
    ano INT NOT NULL,                
    semestre INT NOT NULL CHECK (semestre IN (1, 2)) 
);


CREATE TABLE tbl_envio (
    id_envio INT PRIMARY KEY AUTO_INCREMENT,
    id_fazenda INT,
    id_hortifruti INT,
    id_motorista INT,
    id_planta INT,
    id_safra INT, 
    quantidade_enviada DECIMAL(10,2) NOT NULL,
    data_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_fazenda) REFERENCES tbl_fazenda(id_fazenda),
    FOREIGN KEY (id_hortifruti) REFERENCES tbl_hortifruti(id_hortifruti),
    FOREIGN KEY (id_motorista) REFERENCES tbl_motorista(id_motorista),
    FOREIGN KEY (id_planta) REFERENCES tbl_planta(id_planta),
    FOREIGN KEY (id_safra) REFERENCES tbl_safra(id_safra) 
);



INSERT INTO tbl_hortifruti (nome_hortifruti, cnpj_hortifruti, telefone_hortifruti) VALUES 
('Hortifrúti Central', '11.222.333/0001-44', '(11) 99999-1234'),
('Sacolão do Bairro', '55.666.777/0001-88', '(11) 98888-4321');

INSERT INTO tbl_motorista (nome_motorista, cnh_motorista, telefone_motorista) VALUES 
('Carlos Souza', '12345678900', '(11) 97777-5555'),
('Marcos Lima', '98765432100', '(11) 96666-4444');

INSERT INTO tbl_fazenda (nome_fazenda, estoque_fazenda, cnpj_fazenda) VALUES 
('Fazenda Sol Nascente', 5000.00, '12.345.678/0001-99'),
('Sítio Vale Verde', 3500.50, '98.765.432/0001-11');

INSERT INTO tbl_planta (nome_planta, especie_planta, id_fazenda) VALUES 
('Alface Crespa', 'Verdura', 1),
('Tomate Cereja', 'Fruto', 1),
('Morango Orgânico', 'Fruta', 2);


INSERT INTO tbl_safra (nome_safra, ano, semestre) VALUES 
('Safra de Verão', 2026, 1),
('Safra de Primavera', 2026, 2);


INSERT INTO tbl_envio (id_fazenda, id_hortifruti, id_motorista, id_planta, id_safra, quantidade_enviada) VALUES
(1, 1, 1, 1, 1, 150.00);