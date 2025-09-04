# main.py
# script para utilizar no terminal para realizar o teste "python main.py"
# certifique-se que voce esteja dentro do diretorio raiz do projeto "programacao funcional" para executar o script

import sys

# Essa linha adiciona a pasta 'src' aos caminhos que o Python procura por módulos.
sys.path.insert(0, './src')

# Agora podemos importar nossas ferramentas lógicas do arquivo 'core.py' que será preciso para criar o menu interativo.
from core import (
    filtrar_pontos_por_bairro,
    filtrar_pontos_por_criticidade, 
    gerar_relatorio_por_bairro,
    atualizar_status_pontos,
    criar_filtro_por_status
)

# Para simular um banco de dados real, começamos com alguns dados de exemplo.
# Em um sistema de verdade, isso viria de um arquivo ou de uma API ou de um DB.
PONTOS_DE_DESCARTE = [
    {'id': 1, 'bairro': 'Pirambu', 'criticidade': 8, 'status': 'pendente'},
    {'id': 2, 'bairro': 'Barra do Ceará', 'criticidade': 9, 'status': 'pendente'},
    {'id': 3, 'bairro': 'Vicente Pinzón', 'criticidade': 5, 'status': 'pendente'},
    {'id': 4, 'bairro': 'Pirambu', 'criticidade': 6, 'status': 'em_atendimento'},
    {'id': 5, 'bairro': 'Centro', 'criticidade': 7, 'status': 'resolvido'},
    {'id': 6, 'bairro': 'Vicente Pinzón', 'criticidade': 2, 'status': 'resolvido'},
]

# Detalhes visuais apenas para deixar a interface mais amigável
STATUS_EMOJI = {
    'pendente': '🔴',
    'em_atendimento': '🟡',
    'resolvido': '🟢'
}

def format_status(status_text):
    """Uma pequena função para deixar os status mais amigaveis."""
    emoji = STATUS_EMOJI.get(status_text, '❓')
    texto_formatado = status_text.replace('_', ' ').capitalize()
    return f"{emoji} {texto_formatado}"
# Fim dos detalhes visuais

# Configurações centrais da nossa aplicação
# Aqui definimos as "regras de negócio" da nossa interface.
NIVEIS_CRITICIDADE = {
    'baixo': (1, 3),
    'medio': (4, 7),
    'alto': (8, 10)
}
DESCRICOES_NIVEIS = {
    'baixo': "Nível Baixo (1-3): Pequeno acúmulo, baixo risco.",
    'medio': "Nível Médio (4-7): Acúmulo considerável, requer atenção da gestão.",
    'alto': "Nível Alto (8-10): Ponto crítico, risco à saúde pública, ação urgente."
}
STATUS_VALIDOS = ['pendente', 'em_atendimento', 'resolvido']


def mostrar_menu():
    """Simplesmente mostra o menu de opções para o usuário a cada rodada do loop."""
    print("\n--- 🗑️  MENU - Monitoramento de Descarte de Lixo ---")
    print("1. 🏙️  Listar pontos de um bairro específico")
    print("2. ⚠️  Listar pontos por nível de criticidade")
    print("3. 📊 Ver relatório de ocorrências por bairro")
    print("4. 🔄 Atualizar status de um ponto de descarte")
    print("5. ➕ Cadastrar novo ponto de descarte")
    print("6. 🔎 Filtros rápidos por status")
    # A OPÇÃO 7 FOI REMOVIDA
    print("0. 🚪 Sair")

# A função "main" é o ponto de partida do nosso programa interativo.
def main():
    """Controla o loop principal da aplicação, mostrando o menu e respondendo as escolhas."""
    # "global" nos permite modificar a lista PONTOS_DE_DESCARTE de dentro da função.
    global PONTOS_DE_DESCARTE

    # O "while True" cria um loop infinito que só é quebrado quando o usuário digita '0'.
    while True:
        mostrar_menu()
        escolha = input("➡️  Digite sua opção: ")

        # Opção 1: O usuário quer ver os pontos de um bairro.
        if escolha == '1':
            prompt = "  - Digite o nome do bairro (ou 'ver' para listar os bairros disponíveis): "
            bairro_input = input(prompt).strip()
            
            if bairro_input.lower() == 'ver':
                bairros_unicos = sorted(list({p['bairro'] for p in PONTOS_DE_DESCARTE}))
                print("\n  -> Bairros com pontos de descarte registrados:")
                for bairro in bairros_unicos:
                    print(f"     - {bairro}")
                continue
            
            bairro_selecionado = bairro_input
            pontos_encontrados = filtrar_pontos_por_bairro(PONTOS_DE_DESCARTE, bairro_selecionado)
            
            if not pontos_encontrados:
                print(f"  ❌ Nenhum ponto encontrado para '{bairro_selecionado}'.")
            else:
                print(f"  -> Pontos em '{bairro_selecionado}':")
                for ponto in pontos_encontrados:
                    print(f"     - ID: {ponto['id']}, Criticidade: {ponto['criticidade']}, Status: {format_status(ponto['status'])}")
        
        # Opção 2: O usuário quer filtrar por criticidade.
        elif escolha == '2':
            prompt = "  - Digite o nível de criticidade (baixo, medio, alto) ou 'ajuda' para ver as definições: "
            nivel_texto = input(prompt).lower().strip()

            if nivel_texto == 'ajuda':
                print("  -> Definições dos Níveis de Criticidade:")
                for nivel, desc in DESCRICOES_NIVEIS.items():
                    print(f"     - {nivel.capitalize()}: {desc}")

            elif nivel_texto in NIVEIS_CRITICIDADE:
                faixa = NIVEIS_CRITICIDADE[nivel_texto]
                nivel_min, nivel_max = faixa
                pontos_filtrados = filtrar_pontos_por_criticidade(PONTOS_DE_DESCARTE, nivel_min, nivel_max)
                
                if not pontos_filtrados:
                    print(f"  ❌ Nenhum ponto encontrado com criticidade no nível '{nivel_texto}'.")
                else:
                    print(f"  -> Pontos com criticidade no nível '{nivel_texto}' ({nivel_min}-{nivel_max}):")
                    for ponto in pontos_filtrados:
                        print(f"     - ID: {ponto['id']}, Bairro: {ponto['bairro']}, Criticidade: {ponto['criticidade']}")
            else:
                print("  ❌ Erro: Nível inválido. Por favor, tente 'baixo', 'medio', 'alto' ou 'ajuda'.")

        # Opção 3: O usuário quer um resumo geral.
        elif escolha == '3':
            relatorio = gerar_relatorio_por_bairro(PONTOS_DE_DESCARTE)
            print("  -> Relatório de Ocorrências por Bairro:")
            for bairro, contagem in relatorio.items():
                print(f"     - {bairro}: {contagem} ponto(s) de descarte")
        
        # Opção 4: O usuário quer atualizar o status de um ponto.
        elif escolha == '4':
            while True:
                prompt = "  - Digite o ID do ponto a atualizar (ou 'ver' para listar todos os pontos): "
                id_input = input(prompt).lower().strip()

                if id_input == 'ver':
                    print("\n--- 📋 Lista de Todos os Pontos Registrados ---")
                    if not PONTOS_DE_DESCARTE:
                        print("  -> Nenhum ponto de descarte cadastrado.")
                    else:
                        for ponto in PONTOS_DE_DESCARTE:
                            print(
                                f"  - ID: {ponto['id']:<3} | "
                                f"Bairro: {ponto['bairro']:<15} | "
                                f"Criticidade: {ponto['criticidade']:<2} | "
                                f"Status: {format_status(ponto['status'])}"
                            )
                    print("-" * 60) # Linha separadora para clareza
                    continue # Volta para o prompt, permitindo que o usuário digite o ID
                
                try:
                    id_ponto = int(id_input)
                    if not any(p['id'] == id_ponto for p in PONTOS_DE_DESCARTE):
                        print(f"  ❌ Erro: Ponto com ID {id_ponto} não foi encontrado.")
                        break # Sai do loop interno e volta para o menu principal
                    
                    print(f"  - Status disponíveis: {', '.join(STATUS_VALIDOS)}")
                    novo_status = input(f"  - Digite o novo status para o ponto ID {id_ponto}: ").lower().strip()
                    
                    if novo_status not in STATUS_VALIDOS:
                        print("  ❌ Erro: Status inválido.")
                        break
                    
                    # TESTE PRÁTICO: Função de Alta Ordem + Lambda
                    PONTOS_DE_DESCARTE = atualizar_status_pontos(PONTOS_DE_DESCARTE,lambda ponto: {**ponto, 'status': novo_status} if ponto['id'] == id_ponto else ponto)
                    print(f"\n  ✅ Status do ponto ID {id_ponto} atualizado para '{novo_status}' com sucesso!")
                    break # Sai do loop interno com sucesso

                except ValueError:
                    print("  ❌ Erro: Entrada inválida. Por favor, digite um número de ID ou a palavra 'ver'.")
                    break # Sai do loop interno em caso de erro

        # Opção 5: O usuário quer cadastrar um novo ponto.
        elif escolha == '5':
            print("\n--- ➕ Cadastro de Novo Ponto de Descarte ---")
            novo_bairro = input("  - Digite o nome do bairro: ").strip()
            if not novo_bairro:
                print("  ❌ Erro: O nome do bairro não pode ser vazio.")
                continue
            
            try:
                criticidade_input = input("  - Digite o nível de criticidade (1 a 10): ")
                nova_criticidade = int(criticidade_input)
                if not 1 <= nova_criticidade <= 10:
                    print("  ❌ Erro: A criticidade deve ser um número entre 1 e 10.")
                    continue
            except ValueError:
                print("  ❌ Erro: A criticidade deve ser um número.")
                continue
            
            max_id = max(p['id'] for p in PONTOS_DE_DESCARTE) if PONTOS_DE_DESCARTE else 0
            novo_id = max_id + 1
            
            novo_ponto = {'id': novo_id,'bairro': novo_bairro,'criticidade': nova_criticidade,'status': 'pendente'}
            PONTOS_DE_DESCARTE.append(novo_ponto)
            
            print("\n  ✅ Ponto cadastrado com sucesso!")
            print(f"     ID Gerado: {novo_ponto['id']}")
            print(f"     Bairro: {novo_ponto['bairro']}")
            print(f"     Criticidade: {novo_ponto['criticidade']}")
            print(f"     Status: {format_status(novo_ponto['status'])}")

        # Opção 6: O usuário quer usar os filtros rápidos.
        elif escolha == '6':
            print("\n--- 🔎 Filtros Rápidos por Status ---")
            print(f"  - Status disponíveis: {', '.join(STATUS_VALIDOS)}")
            status_escolhido = input("  - Digite o status pelo qual deseja filtrar: ").lower().strip()

            if status_escolhido not in STATUS_VALIDOS:
                print("  ❌ Erro: Status inválido.")
                continue
            
            # TESTE PRÁTICO: Closure
            filtro_por_status = criar_filtro_por_status(status_escolhido)
            
            pontos_filtrados = filtro_por_status(PONTOS_DE_DESCARTE)

            if not pontos_filtrados:
                print(f"  -> Nenhum ponto encontrado com o status '{status_escolhido}'.")
            else:
                print(f"\n  -> Pontos com status '{status_escolhido}':")
                for ponto in pontos_filtrados:
                    print(f"     - ID: {ponto['id']}, Bairro: {ponto['bairro']}, Criticidade: {ponto['criticidade']}")
        
        # Opção 0: O usuário quer sair do programa.
        elif escolha == '0':
            print("\nSaindo do sistema. Obrigado por usar! 👋")
            break
        
        # Se o usuário digitar qualquer outra coisa.
        else:
            print("  ❌ Opção inválida, por favor tente novamente.")

# Esta linha garante que a função "main()"" só será chamada quando
# executarmos o arquivo diretamente (com "python main.py").
if __name__ == "__main__":
    main()