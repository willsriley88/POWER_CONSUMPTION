from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Voltage(BaseModel):
    DEVICE: str
    VALUE: float
    STACK: int


class VoltageGet(BaseModel):
    DEVICE: str
    VALUE: float
    STACK: int
    TIME_STAMP: datetime
    ID: int
