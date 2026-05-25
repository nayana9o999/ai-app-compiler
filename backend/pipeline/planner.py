def generate_plan(intent):

    features = intent["features"]

    entities = []
    pages = []
    flows = []

    if "login" in features:
        entities.append("User")
        pages.append("Login")
        flows.append("Authentication Flow")

    if "contacts" in features:
        entities.append("Contact")
        pages.append("Contacts")

    if "payments" in features:
        entities.append("Subscription")
        pages.append("Billing")
        flows.append("Payment Flow")

    if "dashboard" in features:
        pages.append("Dashboard")

    if "analytics" in features:
        pages.append("Analytics")

    return {
        "entities": entities,
        "pages": pages,
        "flows": flows,
        "roles": intent["roles"]
    }