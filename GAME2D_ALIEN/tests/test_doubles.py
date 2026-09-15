from tests.doubles import StubSemDesconto
from src.desconto import Pedido


def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100


def test_pedido_com_mock_desconto(mocker):
    mock_desconto = mocker.Mock()  # Criar mock do desconto
    mock_desconto.calcular.return_value = 10  # Definir comportamento do mock

    pedido = Pedido(mock_desconto)  # Injetar mock no Pedido
    resultado = pedido.total(100)  # Executar método

    assert resultado == 90  # Verificar resultado final

    mock_desconto.calcular.assert_called()  # verifica se o método calcular foi chamado
    mock_desconto.calcular.assert_called_once_with(100)  # verifica se o método calcular foi chamado uma única vez com o valor 100
    assert mock_desconto.calcular.call_count == 1  # verifica se o método calcular foi chamado exatamente uma vez
