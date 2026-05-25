def repair_config(config, errors):

    repaired = config.copy()

    for error in errors:

        # Missing table repair

        if "missing table" in error:

            missing_table = error.split(":")[-1].strip()

            repaired["tables"].append({
                "name": missing_table,
                "columns": [
                    {
                        "name": "id",
                        "type": "integer"
                    }
                ]
            })

        # Missing pages repair

        if "No UI pages generated" in error:

            repaired["pages"].append({
                "name": "Home",
                "components": [
                    "Navbar",
                    "MainContent"
                ]
            })

    return repaired