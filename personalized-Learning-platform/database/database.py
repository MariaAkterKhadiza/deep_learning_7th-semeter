import sqlite3


def create_database():

    conn = sqlite3.connect(
        "database/learning_platform.db"
    )

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            email TEXT UNIQUE,

            password TEXT

        )
        """
    )


    conn.commit()

    conn.close()



create_database()
print("Database created successfully!")