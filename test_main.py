import main

def test_calcul():
    """Verifică funcția matematică din main.py"""
    assert main.calcul(3, 4) == 14

def test_mesaj():
    """Validează un mesaj specific"""
    expected = "Hello CI/CD!"
    assert main.print_message() == expected