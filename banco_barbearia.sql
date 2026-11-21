CREATE DATABASE IF NOT EXISTS barbearia_lfj
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE barbearia_lfj;

CREATE TABLE IF NOT EXISTS agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    servico VARCHAR(80) NOT NULL,
    barbeiro VARCHAR(60) NOT NULL,
    data_horario VARCHAR(25) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'Agendado'
);