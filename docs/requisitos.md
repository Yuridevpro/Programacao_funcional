# PROJETO: Mapeamento e Monitoramento de Pontos de Descarte Irregular de Lixo

---


### **1. Arquitetura do Projeto**

O projeto foi estruturado seguindo o princípio da **Separação de Responsabilidades**, dividindo a aplicação em componentes lógicos e independentes.

- **`docs/`:** Contém a documentação do projeto.
- **`src/core.py`:** É o cérebro da aplicação, contendo a lógica de negócio pura e testável.
- **`tests/test_core.py`:** Contém os testes automatizados que validam o comportamento do `core.py`.
- **`main.py`:** É a camada de apresentação e o ponto de entrada interativo da aplicação.

---

### **2. Requisitos Funcionais (RF)**

*   **RF01:** O sistema deve ser capaz de filtrar e retornar todos os pontos de descarte de um bairro específico.
    *   **Implementado em:** `src/core.py`, função `filtrar_pontos_por_bairro()`.

*   **RF02:** O sistema deve identificar e retornar uma lista de pontos de descarte com base em faixas de criticidade (níveis 'baixo', 'medio' e 'alto').
    *   **Implementado em:** `src/core.py`, função `filtrar_pontos_por_criticidade()`.

*   **RF03:** O sistema deve permitir a atualização do status de um ponto de descarte específico, fornecendo uma forma integrada de visualizar os IDs dos pontos.
    *   **Implementado em:** `src/core.py`, função `atualizar_status_pontos()`. A interface de ajuda está em `main.py`.

*   **RF04:** O sistema deve gerar um relatório resumido com a contagem de pontos por bairro.
    *   **Implementado em:** `src/core.py`, função `gerar_relatorio_por_bairro()`.

*   **RF05:** O sistema deve permitir o cadastro de um novo ponto de descarte com ID e status gerados automaticamente.
    *   **Implementado em:** Lógica de interface em `main.py`.

*   **RF06:** O sistema deve fornecer filtros rápidos para visualizar todos os pontos por um status específico.
    *   **Implementado em:** `src/core.py`, através da closure `criar_filtro_por_status()`, que é acionada pela interface em `main.py`.

---

### **3. Requisitos Não Funcionais (RNF)**

#### RNF01 - Interface de Usuário
- **Descrição:** O sistema deverá fornecer uma interface de linha de comando intuitiva e amigável.
- **Implementação no Código:**
  - **Função:** `mostrar_menu()`
  - **Localização:** Arquivo `main.py`
  - **Características:** Menu numerado com emojis para melhor UX.
  - **Formatação:** Função `format_status()` para exibição visual dos status.

#### RNF02 - Tratamento de Erros
- **Descrição:** O sistema deverá tratar adequadamente erros de entrada do usuário.
- **Implementação no Código:**
  - **Validação de IDs:** Bloco `try-except` para conversão de string para inteiro.
  - **Validação de Status:** Verificação contra a lista `STATUS_VALIDOS`.
  - **Validação de Criticidade:** Verificação de faixa de valores (1-10).
  - **Mensagens de Erro:** Padronização com emoji ❌ para feedback visual.

#### RNF03 - Configurabilidade
- **Descrição:** O sistema deverá permitir a configuração centralizada de níveis de criticidade e status válidos.
- **Implementação no Código:**
  - **Constantes:** `NIVEIS_CRITICidade`, `STATUS_VALIDOS`, `DESCRICOES_NIVEIS`.
  - **Localização:** Arquivo `main.py`
  - **Mapeamento Visual:** Dicionário `STATUS_EMOJI` para representação gráfica.

#### RNF04 - Extensibilidade
- **Descrição:** O sistema deverá ser projetado de forma a ser facilmente extensível para novas funcionalidades.
- **Implementação no Código:**
  - **Modularização:** Separação clara entre lógica de negócio (`core.py`) e interface (`main.py`).
  - **Funções de Alta Ordem:** `atualizar_status_pontos` permite novas lógicas de atualização sem modificar o código existente.
  - **Estrutura de Dados:** Uso de dicionários para representar os pontos, facilitando a adição de novos campos no futuro.

#### RNF05 - Performance
- **Descrição:** O sistema deverá processar operações de filtragem e contagem de forma eficiente.
- **Implementação no Código:**
  - **List Comprehensions:** Operações otimizadas e idiomáticas em Python para filtragem de dados.
  - **`collections.Counter`:** Uso de um algoritmo altamente eficiente para a contagem de itens em `gerar_relatorio_por_bairro`.
  - **Estruturas em Memória:** Acesso direto aos dados na lista `PONTOS_DE_DESCARTE`, sem a latência de um banco de dados externo.

#### RNF06 - Usabilidade
- **Descrição:** O sistema deverá fornecer ajuda contextual e feedback claro ao usuário para facilitar o uso.
- **Implementação no Código:**
  - **Sistema de Ajuda:** Comando 'ver' integrado nas opções de listagem e atualização.
  - **Feedback Visual:** Uso de emojis (🔴, 🟡, 🟢) para representar o status dos pontos.
  - **Mensagens Informativas:** Descrições detalhadas dos níveis de criticidade para guiar o usuário.
  - **Confirmações:** Mensagens de sucesso padronizadas com ✅ após operações de cadastro e atualização.

---

### **4. Mapeamento dos Conceitos de Programação Funcional**

*   **Função de Alta Ordem:** Aplicado na função `atualizar_status_pontos`.
*   **Função Lambda:** Usada para fornecer a lógica de atualização para `atualizar_status_pontos`.
*   **List Comprehension:** Utilizada nas funções `filtrar_pontos_por_criticidade`, `filtrar_pontos_por_bairro` e `gerar_relatorio_por_bairro`.
*   **Closure:** Implementada na função `criar_filtro_por_status(status)`. **Esta função é acionada diretamente pela "Opção 6" do menu interativo**, onde uma função de filtro especializada é criada e utilizada sob demanda.

---

### **5. Guia de Uso e Execução**

**Pré-requisitos:**
*   Python 3.

#### **Executando a Aplicação Interativa**

1.  Abra um terminal na pasta raiz do projeto.
2.  Execute o comando: `python main.py`

#### **Executando os Testes Automatizados**

1.  Abra um terminal na pasta raiz do projeto.
2.  Execute o comando: `python -m unittest discover tests`

#### **Funcionalidades no Menu**

*   **Opção 1 (Listar por Bairro):** Permite ver os pontos de um bairro por nome. Use o comando 'ver' para listar os bairros disponíveis.
*   **Opção 2 (Listar por Criticidade):** Filtra os pontos com base nos níveis 'baixo' (1-3), 'medio' (4-7) ou 'alto' (8-10).
*   **Opção 3 (Ver Relatório):** Mostra um resumo quantitativo de pontos por bairro.
*   **Opção 4 (Atualizar Status):** Permite alterar o status de um ponto. Use o comando 'ver' dentro desta opção para listar todos os pontos e encontrar o ID correto.
*   **Opção 5 (Cadastrar Ponto):** Permite adicionar um novo registro.
*   **Opção 6 (Filtros por Status):** Permite visualizar todos os pontos que correspondem a um status específico.

---
