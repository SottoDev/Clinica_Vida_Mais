# 🏥 Sistema Clínica Vida+

> Sistema de gerenciamento de pacientes desenvolvido em Python com banco de dados SQLite

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/database-SQLite-green)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)
[![Status](https://img.shields.io/badge/status-ativo-success)](https://github.com)

---

## 📋 Sobre o Projeto

O **Sistema Clínica Vida+** é uma aplicação de linha de comando desenvolvida para gerenciar informações de pacientes em clínicas e consultórios médicos. O sistema permite cadastrar, buscar, listar e deletar pacientes, além de fornecer estatísticas úteis sobre os dados cadastrados.

### ✨ Principais Funcionalidades

- ✅ **Cadastro de Pacientes** - Registre nome, idade e telefone
- 📊 **Estatísticas Avançadas** - Visualize total, idade média, paciente mais novo e mais velho
- 🔍 **Busca Inteligente** - Encontre pacientes pelo nome (busca parcial)
- 📝 **Listagem Completa** - Veja todos os pacientes cadastrados de forma organizada
- 🗑️ **Exclusão de Registros** - Remova pacientes do banco de dados
- 💾 **Armazenamento Persistente** - Dados salvos permanentemente em banco SQLite

---

## 🚀 Começando

### Pré-requisitos

- Python 3.7 ou superior
- SQLite3 (já incluído no Python)

### 📦 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/clinica-vida-plus.git
   cd clinica-vida-plus
   ```

2. **Verifique a instalação do Python**
   ```bash
   python --version
   ```
   ou
   ```bash
   python3 --version
   ```

3. **Execute o programa**
   ```bash
   python main.py
   ```
   ou
   ```bash
   python3 main.py
   ```

**Não é necessário instalar dependências externas!** O projeto usa apenas bibliotecas nativas do Python.

---

## 📁 Estrutura do Projeto

```
clinica-vida-plus/
│
├── main.py              # Arquivo principal - executa o programa
├── database.py          # Gerenciamento do banco de dados SQLite
├── paciente.py          # Operações CRUD de pacientes
├── menu.py              # Interface de usuário e menus
├── clinica.db           # Banco de dados (criado automaticamente)
├── README.md            # Este arquivo
└── LICENSE              # Licença do projeto
```

### 📄 Descrição dos Arquivos

| Arquivo | Responsabilidade |
|---------|------------------|
| `main.py` | Ponto de entrada do programa, coordena todas as funcionalidades |
| `database.py` | Criação, conexão e gerenciamento do banco de dados |
| `paciente.py` | Funções de cadastro, busca, listagem, estatísticas e exclusão |
| `menu.py` | Exibição de menus e mensagens para o usuário |
| `clinica.db` | Banco de dados SQLite (gerado automaticamente na primeira execução) |

---

## 🎮 Como Usar

### Menu Principal

Ao executar o programa, você verá o seguinte menu:

```
========================================
=== SISTEMA CLÍNICA VIDA+ ===
========================================
1. Cadastrar paciente
2. Ver estatísticas
3. Buscar paciente
4. Listar todos os pacientes
5. Deletar paciente
6. Sair
========================================
Escolha uma opção:
```

### 1️⃣ Cadastrar Paciente

```
=== CADASTRAR PACIENTE ===
Nome do paciente: João Silva
Idade: 45
Telefone: (11) 99999-9999
✅ Paciente cadastrado com sucesso!
```

**Validações:**
- Nome não pode estar vazio
- Idade deve ser um número entre 0 e 150
- Telefone não pode estar vazio

### 2️⃣ Ver Estatísticas

```
=== ESTATÍSTICAS ===
Total de pacientes: 3
Idade média: 45.0 anos
Paciente mais novo: Maria Santos (32 anos)
Paciente mais velho: Pedro Costa (58 anos)
```

### 3️⃣ Buscar Paciente

```
=== BUSCAR PACIENTE ===
Digite o nome do paciente: maria

✅ 1 paciente(s) encontrado(s):

ID: 2
Nome: Maria Santos
Idade: 32 anos
Telefone: (11) 88888-8888
```

**Obs:** A busca não diferencia maiúsculas de minúsculas e encontra nomes parciais.

### 4️⃣ Listar Todos os Pacientes

```
=== LISTA DE PACIENTES ===

1. João Silva
   ID: 1
   Idade: 45 anos
   Telefone: (11) 99999-9999

2. Maria Santos
   ID: 2
   Idade: 32 anos
   Telefone: (11) 88888-8888

3. Pedro Costa
   ID: 3
   Idade: 58 anos
   Telefone: (11) 77777-7777
```

### 5️⃣ Deletar Paciente

```
=== DELETAR PACIENTE ===

Pacientes cadastrados:
ID 1: João Silva
ID 2: Maria Santos
ID 3: Pedro Costa

Digite o ID do paciente a deletar (0 para cancelar): 2
✅ Paciente deletado com sucesso!
```

---

## 🗄️ Banco de Dados

### Estrutura da Tabela `pacientes`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | INTEGER | Chave primária, auto-incremento |
| `nome` | TEXT | Nome completo do paciente (obrigatório) |
| `idade` | INTEGER | Idade do paciente (obrigatório) |
| `telefone` | TEXT | Telefone de contato (obrigatório) |

### Exemplo de SQL

```sql
CREATE TABLE pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    telefone TEXT NOT NULL
);
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+** - Linguagem de programação
- **SQLite3** - Banco de dados relacional
- **Metodologia Ágil Scrum** - Gestão do projeto

---

## 📚 Conceitos Aplicados

### Programação

- ✅ Funções e modularização
- ✅ Tratamento de exceções (`try/except`)
- ✅ Validação de dados de entrada
- ✅ Manipulação de strings
- ✅ Estruturas de controle (if/elif/else, while, for)
- ✅ Importação de módulos

### Banco de Dados

- ✅ Operações CRUD (Create, Read, Update, Delete)
- ✅ Consultas SQL (SELECT, INSERT, DELETE)
- ✅ Funções de agregação (COUNT, AVG, MIN, MAX)
- ✅ Prepared Statements (proteção contra SQL Injection)
- ✅ Gerenciamento de conexões

### Boas Práticas

- ✅ Separação de responsabilidades
- ✅ Código limpo e comentado
- ✅ Nomenclatura descritiva
- ✅ Tratamento de erros robusto
- ✅ Estrutura de projeto organizada

---

## 🎯 Funcionalidades Futuras

- [ ] Atualizar dados de pacientes existentes
- [ ] Exportar relatórios em PDF
- [ ] Sistema de agendamento de consultas
- [ ] Histórico médico dos pacientes
- [ ] Interface gráfica (GUI) com Tkinter ou PyQt
- [ ] Sistema de backup automático
- [ ] Múltiplos níveis de usuário (admin, recepcionista, médico)
- [ ] Integração com API de envio de SMS

---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Siga os passos abaixo:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### Diretrizes de Contribuição

- Mantenha o código limpo e bem comentado
- Adicione testes para novas funcionalidades
- Siga o estilo de código existente
- Atualize a documentação quando necessário

---

## 🐛 Reportar Bugs

Encontrou um bug? Por favor, abra uma [issue](https://github.com/seu-usuario/clinica-vida-plus/issues) descrevendo:

- O que você esperava que acontecesse
- O que realmente aconteceu
- Passos para reproduzir o erro
- Versão do Python que está usando

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por **[Seu Nome]**

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [Seu Nome](https://linkedin.com/in/seu-perfil)
- Email: seu.email@exemplo.com

---

## 📞 Suporte

Se precisar de ajuda, você pode:

- 📧 Enviar um email para: suporte@clinicavidaplus.com
- 💬 Abrir uma [discussão](https://github.com/seu-usuario/clinica-vida-plus/discussions)
- 🐛 Reportar um [bug](https://github.com/seu-usuario/clinica-vida-plus/issues)

---

## 🙏 Agradecimentos

- Agradecimento especial à metodologia Scrum por organizar o desenvolvimento
- Comunidade Python pela documentação excelente
- Todos os contribuidores que ajudaram a melhorar este projeto

---

## 📊 Status do Projeto

```
✅ Versão 1.0 - Lançamento inicial
📅 Data: Outubro de 2025
👥 Equipe: 1 desenvolvedor
⏱️ Tempo de desenvolvimento: 2 semanas (Sprint 1)
```

---

## 🔧 Solução de Problemas

### Erro: "No module named 'sqlite3'"

**Solução:** O SQLite3 vem incluído no Python. Verifique sua instalação do Python.

### Erro: "Permission denied" ao criar clinica.db

**Solução:** Execute o programa em uma pasta onde você tenha permissão de escrita.

### Banco de dados corrompido

**Solução:** Delete o arquivo `clinica.db` e execute o programa novamente para criar um novo banco.

---

## 📖 Documentação Adicional

Para mais informações sobre as tecnologias utilizadas:

- [Documentação Python](https://docs.python.org/3/)
- [Documentação SQLite](https://www.sqlite.org/docs.html)
- [Tutorial SQL](https://www.w3schools.com/sql/)

---

<div align="center">

**🏥 Sistema Clínica Vida+ - Gerenciando saúde com tecnologia 🏥**

Feito com ❤️ e Python

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!

</div>