# Pesquisa Binária
def pesquisa_binaria(lista, item):
    # baixo e alto acompanham a parte da lista que você esta procurando
    baixo = 0
    alto = len(lista) - 1
  
    while baixo <= alto: # enquanto ainda não conseguiu chegar a um único elemento...        
        meio = (baixo + alto) // 2 # verifica o elemento
        chute = lista[meio]
        if chute == item: # Acha item
            return meio  
        if chute > item: # O chute foi muito alto
            alto = meio - 1
        else: # O chute foi muito baixo
            baixo = meio + 1
    return None # O item não existe


minha_lista = [1, 3, 5, 7, 9] # Vamos testá-lo!

print(f"Achou: {pesquisa_binaria(minha_lista, 3)}")
print(f"Não existe: {pesquisa_binaria(minha_lista, - 1)}")

