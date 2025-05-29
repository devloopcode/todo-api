from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):

    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    
    # def __init__(self, id: int, title, description, priority, complete):
    #     self.id = id
    #     self.title = title
    #     self.description = description
    #     self.priority = priority
    #     self.complete = complete
    
    
    