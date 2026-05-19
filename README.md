# 🍕 Sistema de Pizzaria - Full Stack (Flask + PostgreSQL)

Projeto desenvolvido com o objetivo de praticar o desenvolvimento full stack utilizando Flask (Python), PostgreSQL, HTML e CSS, enquanto ainda estou em processo de aprendizado das tecnologias.

---

## 🧠 Conceitos aplicados

* Criação de tabelas com `CREATE TABLE`
* Uso de `PRIMARY KEY` e `FOREIGN KEY`
* Regras de integridade com `ON DELETE` (RESTRICT, CASCADE)
* Validações com `CHECK`
* Uso de `UNIQUE` para evitar duplicidade de dados
* Tipos de dados adequados (VARCHAR, CHAR, NUMERIC, TIMESTAMP)

---

## 🗂️ Estrutura do Banco

O sistema foi modelado com as seguintes entidades:

* **usuarios** → Armazena dados dos clientes
* **pedidos** → Representa os pedidos realizados
* **produtos** → Lista de produtos disponíveis
* **itens_pedido** → Relaciona pedidos e produtos (itens do pedido)

---

## 🔗 Relacionamentos

* Um usuário pode ter vários pedidos
* Um pedido pertence a um único usuário
* Um pedido pode conter vários produtos
* Produtos não podem ser removidos se já estiverem vinculados a pedidos
* Ao excluir um pedido, seus itens são removidos automaticamente

---

## ⚙️ Regras de negócio implementadas

* Não é possível excluir usuários que possuem pedidos (`ON DELETE RESTRICT`)
* Ao excluir um pedido, seus itens são excluídos automaticamente (`ON DELETE CASCADE`)
* Produtos não podem ser excluídos se estiverem em pedidos (`ON DELETE RESTRICT`)
* Não é permitido repetir o mesmo produto dentro de um pedido (`UNIQUE (pedido_id, produto_id)`)
* Quantidade de itens deve ser maior que zero
* Preço dos produtos não pode ser negativo

---

## 🛠️ Tecnologias utilizadas

* PostgreSQL
* SQL
* HTML
* CSS

---

## 🌐 Interface do sistema (Frontend)

O projeto também conta com páginas iniciais desenvolvidas em HTML e CSS:

* Criado **Index.html** como página inicial com mensagem de boas-vindas e promoções do dia
* Criado **Cadastro.html** para registro de usuários com campos de nome, email, senha, telefone, endereço e CPF
* Criado **Login.html** para autenticação de usuários com campos de nome e senha
* Criado **Cardapio.html** para exibição do cardápio com links de navegação
* Criado **Pedido.html** para realização de pedidos com links de navegação
* Adicionada **PizzariaLogo.png** como logotipo do projeto
* Incluídos arquivos CSS para estilização das páginas

---

## 📌 Observações

Este projeto tem fins educacionais e foi desenvolvido como parte do meu processo de aprendizado em Análise e Desenvolvimento de Sistemas.

---

## 👨‍💻 Autor

Sidne
