from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from pipeline.intent_extractor import extract_intent
from pipeline.planner import generate_plan
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_config
from pipeline.repair_engine import repair_config
from runtime.sqlite_runtime import execute_schema

app = FastAPI()

# CORS FIX

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():

    return {
        "message": "AI App Compiler Running"
    }


@app.post("/generate")
def generate_app(request: PromptRequest):

    user_prompt = request.prompt

    # STEP 1 — INTENT EXTRACTION

    intent = extract_intent(user_prompt)

    # STEP 2 — SYSTEM PLANNING

    plan = generate_plan(intent)

    # STEP 3 — SCHEMA GENERATION

    schema = generate_schema(plan)

    # STEP 4 — VALIDATION

    validation = validate_config(schema)

    repaired = False

    # STEP 5 — REPAIR IF NEEDED

    if not validation["valid"]:

        schema = repair_config(
            schema,
            validation["errors"]
        )

        repaired = True

        validation = validate_config(schema)

    # STEP 6 — RUNTIME EXECUTION

    runtime = execute_schema(schema)

    return {
        "intent": intent,
        "plan": plan,
        "schema": schema,
        "validation": validation,
        "repair_applied": repaired,
        "runtime": runtime
    }