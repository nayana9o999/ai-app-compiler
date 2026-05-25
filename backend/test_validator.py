from pipeline.intent_extractor import extract_intent
from pipeline.planner import generate_plan
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_config

prompt = """
Build a CRM with login, dashboard,
contacts, payments, and admin analytics
"""

intent = extract_intent(prompt)

plan = generate_plan(intent)

schema = generate_schema(plan)

validation = validate_config(schema)

print(validation)