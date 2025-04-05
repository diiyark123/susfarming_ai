from fastapi import FastAPI
from backend.langgraph_flow import run_ai_agents  # ✅ updated import

app = FastAPI()

@app.post("/run-agents")
def run_agents(input_data: dict):
    return run_ai_agents(input_data)
