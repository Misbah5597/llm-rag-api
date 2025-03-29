# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import execute_function, list_available_functions

app = FastAPI()

class FunctionRequest(BaseModel):
    function_name: str
    arguments: dict = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM + RAG-Based Function Execution API"}

@app.get("/functions")
def get_functions():
    """Returns a list of available functions and their descriptions."""
    return list_available_functions()

@app.post("/execute")
def execute(request: FunctionRequest):
    """
    Executes the requested function with provided arguments.
    Example Request:
    {
        "function_name": "get_cpu_usage",
        "arguments": {}
    }
    """
    try:
        result = execute_function(request.function_name, **request.arguments)
        return {"function": request.function_name, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
