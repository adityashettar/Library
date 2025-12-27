import os

# Store books and issued counts
library_data = {}

def add_book(book_name, total_copies):
    library_data[book_name] = total_copies

def issue_book(book_name, requested_copies):
    available = library_data.get(book_name, 0)

    if available == 0:
        return "BOOK_NOT_AVAILABLE"
    elif requested_copies <= available:
        library_data[book_name] -= requested_copies
        return "ISSUED"
    else:
        return "INSUFFICIENT_COPIES"


if __name__ == "__main__":
    book = os.getenv("BOOK_NAME")
    total = os.getenv("TOTAL_COPIES")
    request = os.getenv("REQUESTED_COPIES")

    if not book or not total or not request:
        print("ERROR: Missing parameters")
        exit(1)

    total = int(total)
    request = int(request)

    add_book(book, total)
    decision = issue_book(book, request)

    print("Book:", book)
    print("Total Copies:", total)
    print("Requested Copies:", request)
    print("Decision:", decision)
