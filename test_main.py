import main

def test_calcul():
    """Test the calcul function"""
    assert main.calcul(3, 4) == 14

def test_message():
    """Test the message output"""
    assert main.print_message() == "Hello CI/CD!"