def generate_schema(plan):

    tables = []
    endpoints = []
    pages = []
    roles = []

    # DATABASE TABLES

    for entity in plan["entities"]:

        if entity == "User":
            tables.append({
                "name": "users",
                "columns": [
                    {"name": "id", "type": "integer"},
                    {"name": "email", "type": "string"},
                    {"name": "password", "type": "string"}
                ]
            })

        if entity == "Contact":
            tables.append({
                "name": "contacts",
                "columns": [
                    {"name": "id", "type": "integer"},
                    {"name": "name", "type": "string"},
                    {"name": "phone", "type": "string"}
                ]
            })

        if entity == "Subscription":
            tables.append({
                "name": "subscriptions",
                "columns": [
                    {"name": "id", "type": "integer"},
                    {"name": "plan", "type": "string"},
                    {"name": "status", "type": "string"}
                ]
            })

    # API ENDPOINTS

    for table in tables:

        endpoints.append({
            "path": f"/api/{table['name']}",
            "method": "GET",
            "table": table["name"]
        })

    # UI PAGES

    for page in plan["pages"]:

        pages.append({
            "name": page,
            "components": [
                "Navbar",
                "Sidebar",
                "MainContent"
            ]
        })

    # AUTH ROLES

    for role in plan["roles"]:

        if role == "admin":
            permissions = ["read", "write", "delete"]

        else:
            permissions = ["read"]

        roles.append({
            "name": role,
            "permissions": permissions
        })

    return {
        "app_name": "Generated App",
        "tables": tables,
        "endpoints": endpoints,
        "pages": pages,
        "roles": roles
    }