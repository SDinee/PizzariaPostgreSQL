SELECT * FROM usuarios;

ALTER TABLE usuarios ADD COLUMN telefone VARCHAR(20);

ALTER TABLE produtos ADD COLUMN imagem VARCHAR(100);

ALTER TABLE produtos ADD COLUMN disponivel BOOLEAN DEFAULT TRUE;

DELETE FROM produtos
WHERE id = 2;

ALTER TABLE produtos ADD CONSTRAINT unique_nome UNIQUE (nome);

UPDATE produtos
SET imagem = 'pizzamaracananapolitana.jpeg'
WHERE nome = 'Maracanã Napolitana';

UPDATE produtos
SET preco = 79.99
WHERE nome = 'Quatro Queijos';

UPDATE produtos
SET imagem = 'cocacola.jpeg'
WHERE nome = 'Coca Cola 2L';


