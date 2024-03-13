import pytest
from ..Program import saisir_matrix

def test_saisir_matrix():
    # Simuler la saisie de l'utilisateur
    with pytest.raises(SystemExit):
        with pytest.stdin("2\n3\n1\n2\n3\n4\n5\n6\n"):
            matrices = saisir_matrix("Test")

    # Vérifier si la matrice retournée est correcte
    assert matrices == [[1, 2, 3], [4, 5, 6]]
