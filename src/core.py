# src/core.py
"""
Este é o coração da nossa aplicação. Aqui fica toda a lógica "pura"
para manipular os dados dos pontos de descarte.
"""
from functools import reduce
# Essa função "reduce" vai nos ajudar a aplicar uma operação passo a passo
# em uma lista de valores até chegar em um único resultado.

from collections import Counter
# Essa funcao "Counter", serve como ferramenta prática para contar quantas vezes
# cada item aparece em uma lista.



# Essa função cuida de encontrar todos os pontos de um bairro específico.
# Ela atende ao Requisito Funcional RF01(O sistema deve ser capaz de filtrar e retornar todos os pontos de descarte de um bairro específico.)
def filtrar_pontos_por_bairro(pontos: list[dict], bairro: str) -> list[dict]:
    """
    Filtra uma lista de pontos, retornando apenas os de um bairro.

    Para ser mais amigável, a busca não diferencia maiúsculas de minúsculas,
    então se o usuario procurar por 'Pirambu' ou 'pirambu' dá o mesmo resultado.

    CONCEITO APLICADO: List Comprehension.
    Usamos uma list comprehension aqui porque é uma forma muito limpa e favoravel de usar no python para criar uma nova lista baseada em uma condição.
    """
    return [ponto for ponto in pontos if ponto['bairro'].lower() == bairro.lower()]


# Aqui, filtramos os pontos pela sua faixa de criticidade.
# Atende ao Requisito Funcional RF02(O sistema deve identificar e retornar uma lista de pontos de descarte com base em faixas de criticidade (níveis 'baixo', 'medio' e 'alto').
def filtrar_pontos_por_criticidade(pontos: list[dict], nivel_min: int, nivel_max: int) -> list[dict]:
    """
    Retorna uma lista de pontos que estão dentro de uma faixa de criticidade.

    exemplo, para o nível 'baixo', nivel de criticidade 1 e 3 pontos
    no 'médio' (4-7)  e  'alto' (8-10).

    CONCEITO APLICADO: List Comprehension.
    Novamente, usemos aqui a list comprehension pois é ideal para utilizar nessa filtragem baseada em uma condição.
    """
    return [ponto for ponto in pontos if nivel_min <= ponto['criticidade'] <= nivel_max]


# Essa função é a nossa ferramenta para modificar os dados.
# Atende ao Requisito Funcional RF03(O sistema deve permitir a atualização do status de um ponto de descarte específico).
def atualizar_status_pontos(pontos: list[dict], funcao_atualizacao) -> list[dict]:
    """
    Aplica uma operação de atualização em cada ponto da lista.

    CONCEITO APLICADO: Função de Alta Ordem.
    O legal dessa função é que ela não sabe como atualizar. Em vez disso,
    ela recebe uma outra função como uma "instrução" e a aplica a todos
    os itens. Isso torna ela super flexível. No nosso `main.py`, passamos
    uma função Lambda para ela.
    """
    return list(map(funcao_atualizacao, pontos))


# Para o relatório, precisamos contar quantos pontos cada bairro tem.
# Atende ao Requisito Funcional RF04(O sistema deve gerar um relatório resumido com a contagem de pontos por bairro).
def gerar_relatorio_por_bairro(pontos: list[dict]) -> dict:
    """
    Cria um resumo com a contagem de pontos por bairro.

    CONCEITO APLICADO: List Comprehension.
    Primeiro, usamos uma list comprehension para pegar apenas a lista de nomes
    de bairros. Depois disso, a ferramenta `Counter` faz o trabalho pesado de contar
    as ocorrências de cada um eficientemente.
    """
    bairros = [ponto['bairro'] for ponto in pontos]
    return dict(Counter(bairros))


# Aqui é logica do filtros.
# Atende ao Requisito Funcional RF06(O sistema deve fornecer filtros rápidos para visualizar todos os pontos por um status específico).
def criar_filtro_por_status(status: str):
    """
    Cria e retorna uma nova função que foi criada para filtrar por um status.

    CONCEITO APLICADO: Closure.
    O fato interesante ocorre aqui, a função `filtrar` criada anteriormente "lembra" de qual
    `status` ela deve procurar, mesmo depois que a função `criar_filtro_por_status`
    terminou de rodar. Isso permite criar filtros personalizados e
    reutilizáveis de forma muito pratica.
    """
    def filtrar(pontos: list[dict]) -> list[dict]:
        return [ponto for ponto in pontos if ponto['status'] == status]
    return filtrar