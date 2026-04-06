from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))  # ✅ THIS FIXES YOUR ERROR

    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(Date)
    notes = Column(String)

    # Relationship
    user = relationship("User", back_populates="records")  # ✅ REQUIRED