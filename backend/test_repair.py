from pipeline.intent_extractor import extract_intent
from pipeline.planner import generate_plan
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_config
from pipeline.repair_engine import repair_config

prompt = """
Build a CRM with login and contacts
"""

intent = extract_intent(prompt)

plan = generate_plan(intent)

schema = generate_schema(plan)

# Intentionally break schema

schema["endpoints"][0]["table"] = "missing_table"

validation = validate_config(schema)

print("VALIDATION:")
print(validation)

print("\nREPAIRING...\n")

fixed_schema = repair_config(
    schema,
    validation["errors"]
)

print(fixed_schema)