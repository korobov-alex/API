from models import HistoryItem, HistoryModel  # Importing necessary models


# Function to serialize a book with only essential details
def short_serializer(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "price": book["price"],
        "status": book["status"]
    }


# Function to serialize a book with all details
def full_serializer(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "genre": book["genre"],
        "year": book["year"],
        "cover": book["cover"],
        "price": book["price"],
        "amount": book["amount"],
        "status": book["status"]
    }


# Function to serialize a list of books with all details
def full_books_serializer(books):
    return [full_serializer(book) for book in books]


# Function to serialize a list of books with only essential details
def short_books_serializer(books):
    return [short_serializer(book) for book in books]


# Function to update a book with partial data
def partial_updater(book, update_data):
    serialized_data = book.copy()
    for key, value in update_data.items():
        if update_data[key] is not None:
            serialized_data[key] = update_data[key]
    return serialized_data


# Function to serialize history of changes
def history_serializer(history_of_changes):
    history = []
    # Looping through each change in the history
    for change in history_of_changes.get("history", []):
        # Creating HistoryItem instances and adding them to the list
        history.append(HistoryItem(timestamp=change["timestamp"], data=change["data"]))
    # Returning the HistoryModel instance
    return HistoryModel(_id=str(history_of_changes["_id"]), history=history)
