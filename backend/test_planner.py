from pipeline.intent_extractor import extract_intent
from pipeline.planner import generate_plan

prompt = """
Build a CRM with login, dashboard,
contacts, payments, and admin analytics
"""

intent = extract_intent(prompt)

plan = generate_plan(intent)

print(plan)