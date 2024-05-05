from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from utils.error_util import GlobalHandlerMiddleware
from routes.index_route import router as api_router

# Routes

app = FastAPI()
# Global Handler Middleware Handles any exceptions globally , so that one doesn't have to have try exception blocks
app.add_middleware(GlobalHandlerMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defining API Route
app.include_router(api_router, prefix="/task-manager",
                   tags=["Task Manager"])


@app.get("/")
async def read_root():
    return {"Message : ": "Success"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
