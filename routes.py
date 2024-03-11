import bson
from fastapi import APIRouter, HTTPException
from models import Books  # Importing the Books model
from database import connection, update_data_in_second_database, \
    history_connection  # Importing database connection and update functions
from serializer import short_books_serializer, full_serializer, partial_updater, \
    history_serializer  # Importing serializers
from bson import ObjectId

# Creating an APIRouter instance
router = APIRouter()


# Endpoint to get all books
@router.get("/")
def get_books():
    # Fetching all books from the database and serializing them
    all_books = short_books_serializer(connection.find({}))
    return all_books


# Endpoint to get a specific book by ID
@router.get("/{id}")
def get_book_data(id: str):
    if bson.objectid.ObjectId.is_valid(id):
        book = connection.find_one({"_id": ObjectId(id)})
        if book:
            return full_serializer(book)  # Serializing full details of the book
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    else:
        raise HTTPException(status_code=400, detail="Invalid ID")


# Endpoint to create a new book
@router.post("/")
async def create_book(book: Books):
    result = connection.insert_one(dict(book))  # Inserting book data into the database
    book_id = str(result.inserted_id)
    await update_data_in_second_database(book_id, dict(book))  # Updating history database with the new book data
    return "Book added"


# Endpoint to update an existing book by ID
@router.put("/{id}")
async def update_book(id: str, book: Books):
    if bson.objectid.ObjectId.is_valid(id):
        request_data = book.dict()
        curr_book = connection.find_one({"_id": ObjectId(id)})
        if curr_book:
            changed_book = partial_updater(full_serializer(curr_book), request_data)  # Updating book data
            if changed_book["amount"] < 1:
                changed_book["status"] = False
            connection.update_one(curr_book, {"$set": changed_book})  # Updating book in the database
            await update_data_in_second_database(id, changed_book)  # Updating history database
            data = full_serializer(connection.find_one({"_id": ObjectId(id)}))  # Fetching updated book data
            return data
        else:
            return {"status": "Book with this ID was not found."}
    else:
        raise HTTPException(status_code=400, detail="Invalid ID")


# Endpoint to delete a book by ID
@router.delete("/{id}")
def delete_book(id: str):
    if bson.objectid.ObjectId.is_valid(id):
        book = connection.find_one({"_id": ObjectId(id)})
        if book:
            connection.delete_one({"_id": ObjectId(id)})  # Deleting book from the database
            return "Book was deleted"
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    else:
        raise HTTPException(status_code=400, detail="Invalid ID")


# Endpoint to get history of changes for a book by ID
@router.get("/history/{id}")
async def get_history(id: str):
    if bson.objectid.ObjectId.is_valid(id):
        history_obj = history_connection.find_one({"_id": ObjectId(id)})  # Fetching history from history database
        if history_obj:
            history = history_serializer(history_obj)  # Serializing history data
            return history
        else:
            raise HTTPException(status_code=404, detail="History not found for this ID")
    else:
        raise HTTPException(status_code=400, detail="Invalid ID")
