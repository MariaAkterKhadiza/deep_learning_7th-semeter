import sqlite3
import bcrypt


DATABASE_NAME = "database/learning_platform.db"



# ----------------------------
# Register User
# ----------------------------

def register_user(name, email, password):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    # Convert password into hash

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )


    try:

        cursor.execute(
            """
            INSERT INTO students
            (name, email, password)

            VALUES (?, ?, ?)

            """,
            (
                name,
                email,
                hashed_password
            )
        )


        conn.commit()

        return True


    except sqlite3.IntegrityError:

        return False


    finally:

        conn.close()



# ----------------------------
# Login User
# ----------------------------

def login_user(email, password):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT password
        FROM students
        WHERE email=?
        """,
        (email,)
    )


    result = cursor.fetchone()


    conn.close()


    if result:


        stored_password = result[0]


        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        ):

            return True


    return False