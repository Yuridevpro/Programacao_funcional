# tests/test_core.py
"""
Este arquivo é o nosso foi criado para testar a qualidade.

O objetivo aqui é testar cada função do `core.py` de forma isolada
para garantir que a lógica de negócio esteja funcionando perfeitamente,
independentemente da interface com o usuário.

Cada função de teste simula um cenário específico e verifica se o resultado
produzido pela função do "core.py" é exatamente o que esperamos.
"""
# script para utilizar no terminal para realizar o teste "python -m unittest discover tests"
# certifique-se que voce esteja dentro do diretorio raiz do projeto "programacao funcional", nao precisa entrar na pasta "tests" para executar o script

import unittest
# Esse módulo já vem junto com o Python e é usado para automatizar testes.
# Com ele a gente consegue:
# 1. Agrupar os testes em classes para deixar tudo organizado.
# 2. Criar métodos que preparam o ambiente antes dos testes e limpam depois (como o setUp).
# 3. Conferir se os resultados estão certos usando verificações prontas.

import sys
sys.path.insert(0, './src')

# Importamos todas as funções que vamos testar.
from core import (
    filtrar_pontos_por_bairro,
    filtrar_pontos_por_criticidade,
    atualizar_status_pontos,
    gerar_relatorio_por_bairro,
    criar_filtro_por_status
)


# Ao herdar de "unittest.TestCase", nossa classe "TestWasteManagement"
# ganha todos as ferramentas de teste, como "setUp" e "assertEqual" que serão utilizado em diante
class TestWasteManagement(unittest.TestCase):

    # O método "setUp" é muito essencial e interessante: ele roda antes de CADA teste.
    # Usamos ele para criar um conjunto de dados limpo e consistente,
    # garantindo que um teste não interfira no outro.
    def setUp(self):
        """Prepara um ambiente de teste fresco para cada função de teste."""
        self.pontos_teste = [
            {'id': 1, 'bairro': 'Pirambu', 'criticidade': 8, 'status': 'pendente'},
            {'id': 2, 'bairro': 'Centro', 'criticidade': 5, 'status': 'resolvido'},
            {'id': 3, 'bairro': 'Pirambu', 'criticidade': 2, 'status': 'pendente'},
            {'id': 4, 'bairro': 'Centro', 'criticidade': 7, 'status': 'em_atendimento'},
        ]

 
    def test_filtrar_pontos_por_bairro(self):
        """Verifica se a filtragem por bairro está funcionando corretamente."""
        # Cenário 1: Procurar por 'Pirambu'. Esperamos encontrar 2 pontos.
        resultado_pirambu = filtrar_pontos_por_bairro(self.pontos_teste, 'Pirambu')
        self.assertEqual(len(resultado_pirambu), 2)

        # Cenário 2: Procurar por 'Centro'. Também esperamos encontrar 2 pontos.
        resultado_centro = filtrar_pontos_por_bairro(self.pontos_teste, 'Centro')
        self.assertEqual(len(resultado_centro), 2)

    def test_filtrar_pontos_por_criticidade(self):
        """Garante que o filtro por faixa de criticidade está correto."""
        # Cenário: Nível 'alto' (8 a 10). Esperamos encontrar 1 ponto, o de ID 1.
        resultado_alto = filtrar_pontos_por_criticidade(self.pontos_teste, 8, 10)
        self.assertEqual(len(resultado_alto), 1)
        self.assertEqual(resultado_alto[0]['id'], 1)

        # Cenário: Nível 'medio' (4 a 7). Esperamos encontrar 2 pontos, de IDs 2 e 4.
        resultado_medio = filtrar_pontos_por_criticidade(self.pontos_teste, 4, 7)
        self.assertEqual(len(resultado_medio), 2)
        # Usamos um set para verificar os IDs sem nos preocupar com a ordem.
        ids_medio = {p['id'] for p in resultado_medio}
        self.assertEqual(ids_medio, {2, 4})

        # Cenário: Nível 'baixo' (1 a 3). Esperamos encontrar 1 ponto, o de ID 3.
        resultado_baixo = filtrar_pontos_por_criticidade(self.pontos_teste, 1, 3)
        self.assertEqual(len(resultado_baixo), 1)
        self.assertEqual(resultado_baixo[0]['id'], 3)
    
    def test_atualizar_status_pontos(self):
        """
        Testa a Função de Alta Ordem, passando uma lambda para atualizar o status.
        """
        # A instrução é: "mude o status de todos para 'verificado'".
        pontos_atualizados = atualizar_status_pontos(
            self.pontos_teste,
            lambda p: {**p, 'status': 'verificado'}
        )
        # Verificamos se a mudança foi aplicada corretamente nos primeiros itens.
        self.assertEqual(pontos_atualizados[0]['status'], 'verificado')
        self.assertEqual(pontos_atualizados[1]['status'], 'verificado')

    def test_gerar_relatorio_por_bairro(self):
        """Verifica se a contagem de pontos por bairro está correta."""
        relatorio = gerar_relatorio_por_bairro(self.pontos_teste)
        # O resultado esperado é um dicionário com a contagem exata.
        relatorio_esperado = {'Pirambu': 2, 'Centro': 2}
        self.assertEqual(relatorio, relatorio_esperado)

    def test_closure_filtro_por_status(self):
        """
        Testa a Closure, nossa "fábrica de filtros".
        """
        # Passo 1: Usamos a variavel de filtro para criar um filtro especialista em 'pendente'.
        filtrar_pendentes = criar_filtro_por_status('pendente')
        
        # Passo 2: Usamos o filtro que acabamos de criar.
        resultado = filtrar_pendentes(self.pontos_teste)

        # Passo 3: Verificamos se o filtro fez seu trabalho corretamente.
        # Nos nossos dados de teste, esperamos encontrar 2 pontos pendentes.
        self.assertEqual(len(resultado), 2)