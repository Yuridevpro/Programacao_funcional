
---

# Mapeamento e Monitoramento de Pontos de Descarte Irregular de Lixo

![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)![Linguagem](https://img.shields.io/badge/Linguagem-Python_3.x-blue)![Paradigma](https://img.shields.io/badge/Paradigma-Programa%C3%A7%C3%A3o_Funcional-purple)

---

### **Índice**

1.  [Contexto Acadêmico](#-contexto-acadêmico)
2.  [Alinhamento com os ODS da ONU](#-alinhamento-com-os-ods-da-onu)
3.  [Proposta da Solução](#-proposta-da-solução)
4.  [Arquitetura](#-arquitetura)
5.  [Funcionalidades Implementadas (RF)](#-funcionalidades-implementadas-rf)
6.  [Conceitos de Programação Funcional Aplicados](#-conceitos-de-programação-funcional-aplicados)
7.  [Como Executar](#-como-executar)
8.  [Equipe e Papéis](#-equipe-e-papéis)

---

### **📝 Contexto Acadêmico**

Este repositório documenta um projeto desenvolvido para a disciplina de **Programação Funcional**. Seu objetivo principal não é ser uma aplicação de produção, mas sim **aplicar e demonstrar o entendimento de conceitos-chave do paradigma funcional** em um cenário prático e relevante.

O arquivo `main.py` funciona como uma interface simbólica (prova de conceito) para interagir e validar a lógica de negócio, que foi implementada de forma pura e isolada no núcleo do sistema (`src/core.py`), conforme as boas práticas do paradigma.

### **🌍 Alinhamento com os ODS da ONU**

O tema do projeto foi escolhido em alinhamento com os **Objetivos de Desenvolvimento Sustentável (ODS)** da ONU. A solução proposta aborda diretamente metas do **ODS 11: Cidades e Comunidades Sustentáveis**, que busca tornar os assentamentos humanos mais inclusivos, seguros, resilientes e sustentáveis.

Ao focar no gerenciamento do descarte irregular de lixo, o projeto explora como a tecnologia e os paradigmas de programação podem contribuir para resolver desafios urbanos críticos, promovendo ambientes mais limpos e organizados.

### **🎯 Proposta da Solução**

A proposta consiste em um núcleo de lógica de negócio (`core.py`) que utiliza princípios da programação funcional para manipular dados sobre pontos de descarte irregular de lixo. Este núcleo oferece funções puras para operações como filtragem, atualização e geração de relatórios, garantindo um código testável, modular e com menos efeitos colaterais.

A interface de linha de comando (`main.py`) serve como uma camada de demonstração para interagir com essa lógica de forma controlada.

### **🏛️ Arquitetura**

O sistema foi projetado com uma clara **Separação de Responsabilidades** para facilitar a manutenção e a testabilidade:

*   **`src/core.py`**: O cérebro da aplicação, contendo toda a lógica de negócio pura e as funções funcionais. É totalmente independente da interface.
*   **`tests/test_core.py`**: Contém os testes unitários que validam o comportamento de cada função do `core.py`, garantindo a qualidade e a corretude da lógica.
*   **`main.py`**: A camada de apresentação simbólica (interface de linha de comando) que invoca as funções do `core.py` para executar as operações solicitadas pelo usuário.

---

### **✨ Funcionalidades Implementadas (RF)**

*   **RF01: Filtrar por Bairro:** Lista todos os pontos de descarte de um bairro específico.
*   **RF02: Filtrar por Criticidade:** Exibe pontos com base em níveis de criticidade: 'baixo' (1-3), 'médio' (4-7) ou 'alto' (8-10).
*   **RF03: Atualizar Status:** Permite a atualização do status de um ponto (ex: de 'pendente' para 'resolvido').
*   **RF04: Gerar Relatório por Bairro:** Gera um resumo com a contagem de pontos por bairro.
*   **RF05: Cadastrar Novo Ponto:** Adiciona um novo ponto de descarte ao sistema.
*   **RF06: Filtros Rápidos por Status:** Permite visualizar rapidamente os pontos com um status específico.

---

### **🧠 Conceitos de Programação Funcional Aplicados**

Este projeto foi desenvolvido para aplicar diretamente os conceitos exigidos pela atividade acadêmica:

*   **Função de Alta Ordem (Higher-Order Function):**
    *   **Implementação:** `atualizar_status_pontos()` em `core.py`.
    *   **Descrição:** A função recebe outra função como argumento (`funcao_atualizacao`), o que a torna genérica e reutilizável. Ela aplica a lógica recebida a cada item da lista, sem conhecer os detalhes da operação.

*   **Função Lambda:**
    *   **Utilização:** Em `main.py`, funções anônimas (lambda) são criadas e passadas para `atualizar_status_pontos` para definir a lógica de atualização de status dinamicamente, tornando o código mais conciso.

*   **List Comprehension:**
    *   **Implementação:** `filtrar_pontos_por_bairro()`, `filtrar_pontos_por_criticidade()` e `gerar_relatorio_por_bairro()`.
    *   **Descrição:** Utilizada para criar novas listas de forma declarativa e eficiente, aplicando condições de filtragem de maneira idiomática em Python.

*   **Closure:**
    *   **Implementação:** `criar_filtro_por_status()` em `core.py`.
    *   **Descrição:** Atua como uma "fábrica de funções". Ela cria e retorna uma nova função de filtro que "lembra" o `status` pelo qual deve filtrar. Isso permite a criação de filtros especializados e reutilizáveis sob demanda.

---

### **🚀 Como Executar**

**Pré-requisitos:**
*   Python 3.x

#### **Executando a Aplicação (Demonstração)**

1.  Clone este repositório para a sua máquina local.
2.  Abra um terminal e navegue até a pasta raiz do projeto.
3.  Execute o seguinte comando para iniciar a interface interativa:
    ```bash
    python main.py
    ```

#### **Executando os Testes Automatizados**

Para verificar a integridade da lógica de negócio no `core.py`:

1.  No terminal, na pasta raiz do projeto, execute o comando:
    ```bash
    python -m unittest discover tests
    ```

---

### **🤝 Equipe e Papéis**

| Papel | Integrante(s) |
| :--- | :--- |
| Gerentes de Projeto e Documentação | José Alves Ferreira Neto, Alan Magalhães Barros |
| Desenvolvedores Principais | Yuri da Silva Ferreira, Alisson Rafael Silva de Almeida, Kairo César Ferreira Cunha |
| Engenheiro de Qualidade e Testes | Gabriel Nogueira Ibiapina |