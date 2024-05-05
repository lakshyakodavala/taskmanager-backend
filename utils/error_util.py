import logging
import sys
import traceback
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from schema.response_schema import ApiResponse



logger = logging.getLogger(__name__)


class GlobalHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            import logging
            logging.error(e, exc_info=True)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            filename, line_number, function_name, _ = traceback.extract_tb(
                exc_traceback)[-1]
            error_response = ApiResponse(
                status_code=500,
                message="Something Went Wrong",
                stack_trace=f"Error in file '{filename}', line {line_number}, in {function_name}: {e}",
            )
            return JSONResponse(
                status_code=error_response.status_code,
                content={"message": error_response.message, "stack_trace": error_response.stack_trace}
            )

