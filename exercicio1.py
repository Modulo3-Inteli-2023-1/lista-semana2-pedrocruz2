def conta_palavras_unicas(x: str) -> int: # Pedro Henrique de Azeredo Coutinho Cruz
    palavras = x.split()  
    palavras_unicas = set(palavras)
    return len(palavras_unicas)
