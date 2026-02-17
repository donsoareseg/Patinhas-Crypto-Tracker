def calcular_lucro(dinheiro_investido, quantidade_btc, preco_atual):
    """Calcula o lucro ou prejuízo com bitcoin, sendo que:
    1-A variável "dinheiro_investido" representa o valor total que foi investido em bitcoin;
    2- A variável "Quantidade_btc" representa a quantidade de bitcoins do usuário;
    3- A variável "preco_atual" representa quanto o bitcoin está valendo no mercado;
    4- A variável "valor_atual" representa o valor atual do investimento do usuário em bitcoin."""
    preco_medio = dinheiro_investido / quantidade_btc
    valor_atual = quantidade_btc * preco_atual
    lucro = valor_atual - dinheiro_investido
    return preco_medio, valor_atual, lucro