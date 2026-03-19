# Codigo principal da maquina de estado

from lexer_context import LexerContext
from states import estadoInicial
from tokens import TokenType
import json

def parseExpressao(linha: str) -> list:
    ctx = LexerContext(linha)
    
    estado_atual = estadoInicial
    
    while estado_atual is not None:
        estado_atual = estado_atual(ctx)
        
        if ctx.tokens and ctx.tokens[-1].tipo == TokenType.ERRO:
            print(f"Erro Léxico encontrado na palavra: {ctx.tokens[-1].valor}")
            break
            
    return ctx.tokens

def salvar_tokens_json(dados_agrupados: list, nome_arquivo: str = "tokens_ultima_execucao.txt"):
    
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_agrupados, arquivo, indent=4, ensure_ascii=False)
    print(f"\n[+] Tokens salvos com sucesso no arquivo '{nome_arquivo}'")

if __name__ == "__main__":
    testes = [
        "(3.14 2.0 +)",
        "(5 RES)",
        "(10.5 CONTADOR MEM)",
        "(3.14.5 2.0 +)",
        "(4.0 2.0 //)"
    ]

    historico_para_salvar = []

    for linha in testes:
        print(f"\nAnalisando: {linha}")
        
        tokens = parseExpressao(linha)
        
        for t in tokens:
            print(f"  -> {t}")
            
        tokens_formatados = [{"tipo": t.tipo.name, "valor": t.valor} for t in tokens]
        
        bloco = {
            "expressao": linha,
            "tokens": tokens_formatados
        }
        
        historico_para_salvar.append(bloco)

    if historico_para_salvar:
        salvar_tokens_json(historico_para_salvar)