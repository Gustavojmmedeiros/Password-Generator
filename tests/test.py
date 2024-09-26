from unittest.mock import patch
from src.main import *


def test_length_input_lower_than_minimum():
    # Simula entrada: 5 (inválida), depois 6 (válida)
    with patch('builtins.input', side_effect=['5', '6']):
        result = length_input()
        assert result == 6