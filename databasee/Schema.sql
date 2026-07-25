-- =========================
-- 📦 Estrutura do Banco
-- =========================

-- Usuários
CREATE TABLE usuarios(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE CHECK (email LIKE '%@%'),
    senha VARCHAR(255) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    endereco VARCHAR(255) NOT NULL, -- simplificado, poderia ser normalizado em cidade/estado/rua
    telefone VARCHAR(20)            -- adicionado posteriormente
);

-- Pedidos
CREATE TABLE pedidos(
    id SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL REFERENCES usuarios(id) ON DELETE RESTRICT,
    tipo_entrega VARCHAR(50) NOT NULL CHECK (tipo_entrega IN ('delivery', 'local')),
    tipo_pagamento VARCHAR(50) NOT NULL CHECK (tipo_pagamento IN ('cartao', 'pix', 'dinheiro')),
    data_pedido TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Produtos
CREATE TABLE produtos(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10,2) NOT NULL CHECK (preco >= 0),
    imagem VARCHAR(100),                 -- adicionada
    disponivel BOOLEAN DEFAULT TRUE,     -- adicionada
    CONSTRAINT unique_nome UNIQUE (nome) -- restrição de nome único
);

-- Itens do Pedido
CREATE TABLE itens_pedido(
    id SERIAL PRIMARY KEY,
    pedido_id INT NOT NULL REFERENCES pedidos(id) ON DELETE CASCADE,
    produto_id INT NOT NULL REFERENCES produtos(id) ON DELETE RESTRICT,
    quantidade INT NOT NULL CHECK (quantidade > 0),
    UNIQUE (pedido_id, produto_id)
);