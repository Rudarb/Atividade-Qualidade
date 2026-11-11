import pytest

from regras_localeats import qnt_itens_valida

def test_qnt_valida_entre_1_e_10():
    resultado = qnt_itens_valida(3)
    assert resultado is True

def test_qnt_acima_de_10_retorna_false():
    resultado = qnt_itens_valida(11)
    assert resultado is False


def test_qnt_negativa_gera_value_error():
    with pytest.raises(ValueError):
        qnt_itens_valida(-1)



@pytest.mark.parametrize(
    "quantidade, esperado",
    [
        (0, False),   
        (1, True),  
        (10, True),   
        (11, False), 
    ],
)
def test_limites_da_quantidade_de_itens(quantidade, esperado):
    assert qnt_itens_valida(quantidade) is esperado
