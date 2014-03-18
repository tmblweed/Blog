from sqlalchemy import Column, Integer, String
from database import Base


class Entry(Base): #table details
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    text = Column(String(500) )

    def __init__(self, title=None, text=None):  #Here is where we are initializing
        self.title= title
        self.text = text

