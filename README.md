```markdown
# Book Manager API

## Description

This project is a simple API for managing books in a library. It is developed using Python and FastAPI.

## Installation

1. Clone the repository to your computer:

```bash
git clone https://github.com/korobov-alex/API.git
```

2. Navigate to the project directory:

```bash
cd your-repo
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
uvicorn main:app --reload
```

## Usage

The API has the following endpoints:

- `GET /` - Get a list of all books.
- `POST /books/` - Add a new book.
- `GET /{id}` - Get information about a book by its identifier.
- `PUT /{id}` - Update information about a book.
- `DELETE /{id}` - Delete a book.
- `GET /history/{id}` - Get a history of changes of one book.

## Testing

The API is tested using the Behave library. Run the tests using the following command:

```bash
behave
```
## Database

The API is using MongoDB

## Additional Resources

Additional resources such as API documentation and sample requests can be found in the `docs` folder.

```
