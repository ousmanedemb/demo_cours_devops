import pytest
from Program import saisir_matrix
from unittest.mock import patch

def test_saisir_matrix():
    # Entrées simulées pour les tests
    inputs = ["2", "3", "1", "2", "3", "4", "5", "6"]

    # Patching de la fonction input() pour simuler les entrées utilisateur
    with patch("builtins.input", side_effect=inputs):
        matrices = saisir_matrix("Test")

    # Vérifier si la matrice retournée est correcte
    assert matrices is not None
