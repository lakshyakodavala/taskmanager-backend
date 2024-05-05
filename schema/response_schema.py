from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

generic_type = TypeVar("generic_type")


class ApiResponse(BaseModel, Generic[generic_type]):
    status_code: int = 500
    message: str = "Something went wrong"
    data: Optional[generic_type] = None
    stack_trace: generic_type = None
