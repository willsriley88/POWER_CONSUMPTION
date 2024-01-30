from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from database import Base


class VOLTAGE(Base):
    __tablename__ = "VOLTAGE"
    DEVICE = Column(String, nullable=False)
    VALUE = Column(Float, nullable=False)
    STACK = Column(Integer, nullable=False)
    TIME_STAMP = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    ID = Column(Integer, autoincrement=True, primary_key=True, nullable=False, default=None)

