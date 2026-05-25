from schemas.app_schema import AppConfig


def validate_config(config):

    errors = []

    # Pydantic validation

    try:
        AppConfig(**config)

    except Exception as e:
        errors.append(str(e))

    # Cross-layer validation

    table_names = []

    for table in config["tables"]:
        table_names.append(table["name"])

    for endpoint in config["endpoints"]:

        if endpoint["table"] not in table_names:

            errors.append(
                f"Endpoint references missing table: {endpoint['table']}"
            )

    # UI validation

    page_names = []

    for page in config["pages"]:
        page_names.append(page["name"])

    if len(page_names) == 0:
        errors.append("No UI pages generated")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }