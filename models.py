from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional, List


# Defining a Pydantic model for representing books
class Books(BaseModel):
    title: str  # Title of the book
    author: str  # Author of the book
    genre: Optional[str] = None  # Genre of the book (optional)
    year: Optional[int] = Field(None, ge=1)  # Year of publication (optional, must be greater than or equal to 1)
    cover: Optional[str] = None  # Cover image URL (optional)
    price: Optional[float] = Field(None, ge=0)  # Price of the book (optional, must be greater than or equal to 0)
    amount: int = Field(None, ge=0)  # Amount of available copies (optional, must be greater than or equal to 0)
    status: Optional[bool] = True  # Status of availability (optional, default is True)


# Defining a Pydantic model for representing history items
class HistoryItem(BaseModel):
    timestamp: datetime  # Timestamp of the change
    data: dict  # Data representing the change (e.g., updated fields)


# Defining a Pydantic model for representing history of changes
class HistoryModel(BaseModel):
    _id: str  # ID of the item in the history
    history: List[HistoryItem]  # List of history items representing changes over time
