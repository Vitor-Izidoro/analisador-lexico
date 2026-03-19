# Codigo principal da maquina de estado

from lexer_context import LexerContext
from states import estadoInicial
from tokens import TokenType

def parseExpressao(linha: str) -> list:
    ctx = LexerContext(linha)
    
    estado_atual = estadoInicial
    
    while estado_atual is not None:
        estado_atual = estado_atual(ctx)
        
        if ctx.tokens and ctx.tokens[-1].tipo == TokenType.ERRO:
            print(f"Erro Léxico encontrado na palavra: {ctx.tokens[-1].valor}")
            break
            
    return ctx.tokens

if __name__ == "__main__":
    testes = [
        "(3.14 2.0 +)",
        "(5 RES)",
        "(10.5 CONTADOR MEM)",
        "(3.14.5 2.0 +)",
        "(4.0 2.0 //)"
    ]

    for linha in testes:
        print(f"\nAnalisando: {linha}")
        tokens = parseExpressao(linha)
        for t in tokens:
            print(f"  -> {t}")