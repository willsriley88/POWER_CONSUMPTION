from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Voltage(BaseModel):
    DEVICE: str
    VALUE: float


class VoltageGet(BaseModel):
    DEVICE: str
    VALUE: float
    TIME_STAMP: datetime
    ID: int
