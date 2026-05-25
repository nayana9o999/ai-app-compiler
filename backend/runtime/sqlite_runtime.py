import sqlite3


def execute_schema(config):

    conn = sqlite3.connect("generated_app.db")

    cursor = conn.cursor()

    for table in config["tables"]:

        table_name = table["name"]

        columns = []

        for col in table["columns"]:

            col_name = col["name"]

            col_type = "TEXT"

            if col["type"] == "integer":
                col_type = "INTEGER"

            columns.append(
                f"{col_name} {col_type}"
            )

        query = f"""
        CREATE TABLE IF NOT EXISTS
        {table_name}
        ({",".join(columns)})
        """

        cursor.execute(query)

    conn.commit()

    conn.close()

    return {
        "runtime_status": "success",
        "database": "generated_app.db"
    }