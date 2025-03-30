import sqlite3

def print_sql_old_school(db_path, sql_query, max_column_len=None):
    """
    Executes an SQL query and prints the result set as a formatted, "old-school" text table,
    reminiscent of the output style from SQL*Plus.
    
    Dynamically adjusts column widths based on data, with an optional maximum width limit.

    Args:
        db_params (dict): Database connection parameters (e.g., {'db_type': 'sqlite', 'db_path': 'library.db'}).
        sql_query (str): The SQL query to execute.
        max_column_width (int, optional): The maximum width allowed for each column.
                                           Defaults to None, meaning no width limit.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row from the result set.
              The keys of the dictionaries are the column names. Returns None on error.
    """

    results = []

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]

        if not rows:
            print("No results found.")
            return []

        # Calculate max column widths
        col_widths = {}
        for i, col in enumerate(columns):
            col_widths[col] = len(col)  # Start with column name length
            for row in rows:
                value = row[i]
                if value is not None:
                    value_len = len(str(value))
                    col_widths[col] = max(col_widths[col], value_len)
            #limit the column width.
            if max_column_len is not None:
                col_widths[col] = min(col_widths[col], max_column_len)

        # Print header
        header_format = "".join([f"{{:<{col_widths[col] + 2}}}" for col in columns])  # +2 for padding
        print(header_format.format(*columns))
        print("-" * sum(col_widths.values()) + "-" * (2 * len(columns)))  # Separator

        # Print rows
        row_format = "".join([f"{{:<{col_widths[col] + 2}}}" for col in columns])
        for row in rows:
            row_values = []
            for i in range(len(columns)):
                value = row[i]
                if value is None:
                    row_values.append("")
                else:
                    value_str = str(value)
                    if max_column_len is not None:
                        value_str = value_str[:max_column_len]
                    row_values.append(value_str)
            print(row_format.format(*row_values))
            results.append(dict(zip(columns, row)))

        return results

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        if conn:
            conn.close()

# Example usage (assuming you have a library.db database):
if __name__ == "__main__":
    db_file = "library.db"
    max_column_width = 15
    result_list = print_sql_old_school(db_file, "SELECT id, year FROM books", max_column_width)
    result_list = print_sql_old_school(db_file, "SELECT * FROM books", max_column_width)