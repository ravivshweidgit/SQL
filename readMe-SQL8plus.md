# SQL8plus - A Simple SQLite Client

SQL8plus is a basic command-line SQLite client written in Python, designed to provide an interactive environment for executing SQL queries and managing SQLite databases. It mimics some of the functionality of SQL*Plus, offering a straightforward interface for database interaction.

## Features

* **Database Creation:** Creates a new SQLite database if the specified database file does not exist.
* **Basic CLI Commands:**
    * `.tables`: Lists all tables in the database.
    * `.schema [table_name]`: Displays the schema for a specified table or all tables.
    * `commit`: Saves changes to the database.
    * `rollback`: Undoes changes made since the last commit.
    * `exit` / `q` / `quit`: Exits the client.
    * `SET COLUMN n`: Sets the maximum column width for displayed query results.
* **SQL Query Execution:** Executes arbitrary SQL queries and displays the results in a formatted table.
* **DML Statement Feedback:** Prints the number of affected rows for `INSERT`, `UPDATE`, and `DELETE` statements.
* **Error Handling:** Provides basic error messages for SQLite errors and other exceptions.
* **Clear Screen:** Clears the console screen upon connection.

## Prerequisites

* Python 3.x
* SQLite3 library (usually included with Python)

## Usage

1.  **Run the client:**

    ```bash
    python sql8client.py <database_name>
    ```

    Replace `<database_name>` with the name of your SQLite database file (e.g., `mydatabase.db`). If the database does not exist, the client will prompt you to create it.

2.  **Interact with the database:**

    Once connected, you can enter SQL queries and CLI commands at the `SQL8plus>` prompt.

    * To execute an SQL query, simply type the query and press Enter.
    * To use a CLI command, type the command and press Enter.

3.  **Example:**

    ```bash
    python SQL8plus.py mylibrary.db
    ```

    ```
    Connected to SQLite database: mylibrary.db
    Available CLI commands:
        .tables - List all tables
        .schema [table_name] - Show schema for a table, or all tables
        commit - Save changes
        rollback - Undo changes
        exit / q / quit - Exit the client
        SET COLUMN n - Set the maximum column width to n
        [SQL statements] - Execute any SQL statement
    SQL8plus> .tables
    books
    SQL8plus> SELECT * FROM books;
    id    title                           author          year
    ----------------------------------------------------------
    1     The Hitchhiker's Guide to the G Douglas Adams   1979
    2     Pride and Prejudice             Jane Austen     1813
    3     1984                            George Orwell   1950
    SQL8plus> INSERT INTO books (title, author, year) VALUES ('Brave New World', 'Aldous Huxley', 1932);
    1 row(s) affected.
    SQL8plus> commit
    Changes committed.

    SQL8plus> PRAGMA table_info(books) 
    cid  name    type     notnull  dflt_value  pk  
    -----------------------------------------------
    0    id      INTEGER  0                    1   
    1    title   TEXT     1                    0   
    2    author  TEXT     1                    0   
    3    year    INTEGER  0                    0   
    SQL8plus>

    SQL8plus> exit
    Connection closed.
    ```

## Improvements

This is a basic client, and several improvements can be made:

* **Command History:** Implement command history using the `readline` library.
* **Tab Completion:** Add tab completion for table and column names.
* **Multiline Input:** Allow users to enter multiline SQL statements.
* **Paging:** Implement paging for large result sets.
* **Improved Error Handling:** Provide more specific and informative error messages.
* **Column Formatting:** implement SQL*Plus like column formatting.
* **Add PRAGMA command:** Add a command that allows the user to run any pragma command.
* **Fetch many:** use fetch many for large result sets.
* **More configuration:** Allow users to configure the client.

## Contributing

Contributions are welcome! If you have any suggestions or bug reports, please open an issue or submit a pull request.