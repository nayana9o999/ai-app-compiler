from pipeline.intent_extractor import extract_intent

prompt = """
Build a CRM with login, dashboard,
contacts, payments, and admin analytics
"""

result = extract_intent(prompt)

print(result)