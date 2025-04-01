# print_sql_old_school

This Python function, `print_sql_old_school`, executes an SQL query and prints the result set as a formatted, "old-school" text table, reminiscent of the output style from SQL*Plus. It dynamically adjusts column widths based on the data, with an optional maximum width limit.

## Features

* **SQL*Plus Style Output:** Produces plain text tables similar to the classic SQL*Plus output.
* **Dynamic Column Widths:** Automatically calculates column widths based on the data, ensuring readability.
* **Maximum Column Width Limit:** Allows you to specify a maximum width for each column, preventing excessively long lines.
* **Data Truncation:** Truncates data values that exceed the maximum column width.
* **Error Handling:** Includes error handling for SQLite database operations.
* **Data Return:** Returns the query results as a list of dictionaries for further processing.

## Usage

1.  **Import the function:**

    ```python
    from your_module import print_sql_old_school
    ```

2.  **Call the function:**

    ```python
    import sqlite3

    db_file = "library.db"  # Path to your SQLite database
    sql_query = "SELECT * FROM books"  # Your SQL query
    max_column_width = 15  # Optional: Maximum column width

    results = print_sql_old_school(db_file, sql_query, max_column_width)

    if results:
        # Process the results (list of dictionaries)
        for row in results:
            print(row)
    ```

## Function Signature

```python
def print_sql_old_school(db_path, sql_query, max_column_width=None):
    """
    Executes an SQL query and prints the result set as a formatted, "old-school" text table.

    Args:
        db_path (str): The path to the SQLite database file.
        sql_query (str): The SQL query to execute.
        max_column_width (int, optional): The maximum width allowed for each column.
                                           Defaults to None, meaning no width limit.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row from the result set.
              The keys of the dictionaries are the column names. Returns None on error.

    Notes:
        The output format of this function is intentionally designed to resemble the classic,
        text-based table output produced by SQL*Plus, a command-line SQL client.
        It prioritizes data presentation in a simple, readable, and functional manner,
        similar to the "old-school" terminal-based database interaction.
    """
    # ... function code ...
```

```python

Example Output
Given a books table:

id	title	            author	        year
1	The Hitchhikers...	Douglas Adams	1979
2	Pride & Prejudice	Jane Austen	    1813
3	1984	            George Orwell	1950

PS C:\python\projects\2025-03-30> py .\print_sql_old_school.py
id    year
----------
1     1979
2     1813
3     1950

id    title           author          year
------------------------------------------
1     The Hitchhiker  Douglas Adams    1979
2     Pride & Preju   Jane Austen     1813
3     1984            George Orwell   1950
```