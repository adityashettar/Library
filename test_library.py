from library import add_book, issue_book, library_data

def setup_function():
    library_data.clear()

def test_issue_success():
    add_book("Python", 5)
    result = issue_book("Python", 2)
    assert result == "ISSUED"

def test_insufficient_copies():
    add_book("Java", 2)
    result = issue_book("Java", 5)
    assert result == "INSUFFICIENT_COPIES"

def test_book_not_available():
    result = issue_book("C++", 1)
    assert result == "BOOK_NOT_AVAILABLE"
