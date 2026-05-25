def extract_intent(user_prompt):

    return {
        "app_type": "CRM",
        "features": [
            "login",
            "dashboard",
            "contacts",
            "payments",
            "analytics"
        ],
        "roles": [
            "admin",
            "user"
        ]
    }