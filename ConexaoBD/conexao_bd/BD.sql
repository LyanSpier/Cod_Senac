use bancoteste;

create table Projetos(
	id INT PRIMARY KEY,
    nome varchar(100),
    descricao TEXT,
    usuario_id INT,
    data_criacao DATE,
    FOREIGN KEY (usuario_id) references Usuarios(Id)
); 
CREATE TABLE Tarefas(
	id INT PRIMARY KEY,
    projeto_id INT,
    nome VARCHAR(100),
    descricao TEXT,
    data_criacao DATE,
    data_conclusao DATE,
    status VARCHAR(20),
    FOREIGN KEY (projeto_id) REFERENCES Projetos(id)
);
