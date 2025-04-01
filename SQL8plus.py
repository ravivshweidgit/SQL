import sqlite3
import sys
import os
import print_sql_old_school as printsql
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def SQL8plus(db_name):
    """
    A simple SQLite client (sql8client) that takes a database name as an argument, can create the database if it doesn't exist, and supports 'commit' and 'rollback'.
    Prints the number of affected rows for DML statements when the result set is empty.
    Prints all cli commands after connecting to the database.
    """
    clear_screen()
    
    if not os.path.exists(db_name):
        create = input(f"Database '{db_name}' not found. Create it? (y/n): ")
        if create.lower() != 'y':
            print("Exiting.")
            return

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        print("**************************************************************")
        print("* SQL8plus - A Simple SQLite Client")
        print("*")
        print(f"* Connected to SQLite database: {db_name}")
        print("* Available CLI commands:")
        print("* .tables - List all tables")
        print("* .schema [table_name] - Show schema for a table, or all tables")
        print("* commit - Save changes")
        print("* rollback - Undo changes")
        print("* exit / q / quit - Exit the client")
        print("* SET COLUMN n - Set the maximum column width to n")
        print("* [SQL statements] - Execute any SQL statement (end with ';')")
        print("*")
        print("**************************************************************")

        max_column_len = None  # Initialize max_column_len
        buffer = ""  # Buffer to store multiline SQL statements

        while True:
            try:
                if buffer:
                    query = input("... ")  # Indicate continuation
                else:
                    query = input("SQL8plus> ")

                buffer += query + "\n"  # Add input to buffer, using \n for newlines

                if ";" in query or query.lower() in ("exit", "q", "quit"):
                    # End of SQL statement
                    buffer = buffer.strip()  # Remove leading/trailing whitespace
                    buffer = buffer.rstrip(';') # remove the ;
                    if buffer.lower() in ("exit", "q", "quit"):
                        break
                    elif buffer.lower() == "commit":
                        conn.commit()
                        print("Changes committed.")
                    elif buffer.lower() == "rollback":
                        conn.rollback()
                        print("Changes rolled back.")
                    elif buffer.lower().startswith("set column"):
                        try:
                            max_column_len = int(buffer.split(" ")[2])
                            print(f"Maximum column width set to {max_column_len}.")
                        except (ValueError, IndexError):
                            print("Invalid 'SET COLUMN' command. Usage: SET COLUMN <integer>")
                    elif buffer.lower().startswith(".schema"):
                        table_name = buffer.split(" ")[1] if len(buffer.split(" ")) > 1 else None
                        if table_name:
                            cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
                            result = cursor.fetchone()
                            if result:
                                print(result[0])
                            else:
                                print(f"Table '{table_name}' not found.")
                        else:
                            cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
                            results = cursor.fetchall()
                            if results:
                                for table_name, sql in results:
                                    print(f"Table: {table_name}")
                                    print(sql)
                                    print("-" * 20)
                            else:
                                print("No tables found.")
                    elif buffer.lower().startswith(".tables"):
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                        results = cursor.fetchall()
                        if results:
                            tables = [row[0] for row in results]
                            print(" ".join(tables))
                        else:
                            print("No tables found.")
                    else:
                        cursor.execute(buffer)
                        if buffer.lower().startswith(('insert', 'update', 'delete')):
                            print(f"{cursor.rowcount} row(s) affected.")
                        elif buffer.lower().startswith(('drop', 'create', 'alter')):
                            print("Query executed successfully.")  # Or a similar message
                        else:
                            printsql.print_cursor_old_school(cursor, max_column_len)

                    buffer = ""  # Reset buffer
                else:
                    # Continue reading multiline statement
                    continue

            except sqlite3.Error as e:
                print(f"SQLite error: {e}")
                buffer = "" #clear buffer.
            except Exception as e:
                print(f"Error: {e}")
                buffer = "" #clear buffer.

    except sqlite3.Error as e:
        print(f"Could not connect to database: {e}")

    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sql8client.py <database_name>")
    else:
        db_name = sys.argv[1]
        SQL8plus(db_name)