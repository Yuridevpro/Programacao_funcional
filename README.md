# Mapeamento e Monitoramento de Pontos de Descarte Irregular de Lixo

![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)![Python](https://img.shields.io/badge/Python-3.x-blue)

---

### **Índice**

1.  [Visão Geral do Projeto](#-visão-geral-do-projeto)
2.  [Arquitetura](#-arquitetura)
3.  [Funcionalidades](#-funcionalidades)
4.  [Conceitos de Programação Funcional Aplicados](#-conceitos-de-programação-funcional-aplicados)
5.  [Como Executar](#-como-executar)
    *   [Executando a Aplicação](#executando-a-aplicação)
    *   [Executando os Testes](#executando-os-testes)
6.  [Equipe e Papéis](#-equipe-e-papéis)

---

### **🎯 Visão Geral do Projeto**

Este projeto oferece uma solução de linha de comando para o mapeamento e monitoramento de pontos de descarte irregular de lixo em uma cidade. A aplicação permite que os usuários listem, filtrem, cadastrem e atualizem pontos de descarte, utilizando uma abordagem baseada em programação funcional para garantir um código limpo, modular e testável.

O objetivo principal é fornecer uma ferramenta eficiente para a gestão de resíduos, permitindo a identificação rápida de áreas críticas e o acompanhamento das ações de limpeza.

---

### **🏛️ Arquitetura**

O sistema foi projetado com uma clara **Separação de Responsabilidades**, dividindo o código em componentes lógicos para facilitar a manutenção e a testabilidade.

*   **`src/core.py`**: O coração da aplicação, contendo toda a lógica de negócio pura. As funções neste arquivo são independentes da interface com o usuário, o que permite que sejam testadas de forma isolada.
*   **`tests/test_core.py`**: Contém os testes unitários para cada função do `core.py`, garantindo a qualidade e a corretude da lógica de negócio.
*   **`main.py`**: A camada de apresentação (interface de linha de comando) que interage com o usuário e utiliza as funções do `core.py` para executar as operações.
*   **`docs/`**: Armazena a documentação detalhada do projeto.

---

### **✨ Funcionalidades**

A aplicação implementa os seguintes requisitos funcionais:

*   **RF01: Filtrar por Bairro:** Permite ao usuário listar todos os pontos de descarte de um bairro específico.
*   **RF02: Filtrar por Criticidade:** Filtra e exibe pontos com base em níveis de criticidade: 'baixo' (1-3), 'médio' (4-7) e 'alto' (8-10).
*   **RF03: Atualizar Status:** Permite a atualização do status de um ponto de descarte (ex: de 'pendente' para 'resolvido').
*   **RF04: Gerar Relatório por Bairro:** Gera um resumo com a contagem total de pontos de descarte em cada bairro.
*   **RF05: Cadastrar Novo Ponto:** Permite ao usuário adicionar um novo ponto de descarte, com ID e status gerados automaticamente.
*   **RF06: Filtros Rápidos por Status:** Oferece uma maneira rápida de visualizar todos os pontos que correspondem a um status específico.

---

### **🧠 Conceitos de Programação Funcional Aplicados**

Este projeto foi desenvolvido com foco na aplicação de conceitos de programação funcional para criar um código mais declarativo e com menos efeitos colaterais.

*   **Função de Alta Ordem:**
    *   **Implementação:** `atualizar_status_pontos()`
    *   **Descrição:** Esta função recebe outra função como argumento (`funcao_atualizacao`), o que a torna extremamente flexível. Ela aplica a lógica de atualização recebida a cada item da lista, sem precisar conhecer os detalhes da operação.

*   **Função Lambda:**
    *   **Utilização:** Em `main.py`, funções anônimas (lambda) são passadas para `atualizar_status_pontos` para definir dinamicamente a lógica de atualização de status, tornando o código mais conciso.

*   **List Comprehension:**
    *   **Implementação:** `filtrar_pontos_por_bairro()`, `filtrar_pontos_por_criticidade()`, `gerar_relatorio_por_bairro()`
    *   **Descrição:** Utilizada para criar novas listas de forma declarativa e eficiente, aplicando condições de filtragem de maneira clara e idiomática em Python.

*   **Closure:**
    *   **Implementação:** `criar_filtro_por_status()`
    *   **Descrição:** Esta função atua como uma "fábrica de funções". Ela cria e retorna uma nova função de filtro que "lembra" o status pelo qual deve filtrar. Isso permite a criação de filtros especializados e reutilizáveis sob demanda.

---

### **🚀 Como Executar**

**Pré-requisitos:**
*   Python 3.x

#### **Executando a Aplicação**

1.  Clone este repositório para a sua máquina local.
2.  Abra um terminal e navegue até a pasta raiz do projeto.
3.  Execute o seguinte comando para iniciar a aplicação interativa:
    ```bash
    python main.py
    ```

#### **Executando os Testes**

Para verificar a integridade e o correto funcionamento da lógica de negócio, você pode executar os testes automatizados.

1.  No terminal, na pasta raiz do projeto, execute o comando:
    ```bash
    python -m unittest discover tests
    ```

---

### **🤝 Equipe e Papéis**

| Papel | Integrante |
| :--- | :--- |
| Gerentes de Projeto e Documentação | José Alves Ferreira Neto, Alan Magalhães Barros |
| Desenvolvedores Principais | Yuri da Silva Ferreira, Alisson Rafael Silva de Almeida, Kairo César Ferreira Cunha |
| Engenheiro(a) de Qualidade e Testes | Gabriel Nogueira Ibiapina |
