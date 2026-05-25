from pipeline.intent_extractor import extract_intent
from pipeline.planner import generate_plan
from pipeline.schema_generator import generate_schema
from runtime.sqlite_runtime import execute_schema

prompt = """
Build a CRM with login, contacts,
payments and dashboard
"""

intent = extract_intent(prompt)

plan = generate_plan(intent)

schema = generate_schema(plan)

result = execute_schema(schema)

print(result)