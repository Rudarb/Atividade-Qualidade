QNT_MIN = 1
QNT_MAX = 10


def qnt_itens_valida(quantidade):
    """Informa se a quantidade de itens de um pedido é válida.

    - 1 a 10 itens: True
    - 0 ou acima de 10: False
    - negativa: ValueError
    """
    if quantidade < 0:
        raise ValueError("A quantidade de itens não pode ser negativa.")
    return QNT_MIN <= quantidade <= QNT_MAX
