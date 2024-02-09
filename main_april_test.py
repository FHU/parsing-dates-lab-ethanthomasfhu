import main

def test_main():
    date = "April 2, 1995"
    assert main.parse_date(date) == '04/02/1995'