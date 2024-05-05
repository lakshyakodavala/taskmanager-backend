import bcrypt
from sqlalchemy import text

"""
    User Service
        1. Create
        2. Read 
        3. Update 
        4. Delete
"""


class UserService:
    @classmethod
    def register_user(cls, conn, email: str, password: str):

        # Check if user exists
        select_query = text("SELECT * FROM users WHERE email = :email")
        result = conn.execute(select_query, {'email': email}).fetchone()
        if result:
            return {"status_code": 200, "message": "User Already Exists", 'data': {}}

        # User does not exist, proceed with registration
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        insert_query = text("INSERT INTO users (email, password) VALUES (:email, :password)")
        conn.execute(insert_query, {'email': email, 'password': hashed_password})
        conn.commit()

        return {"status_code": 201, "message": "User Created", "data": {}}

    @classmethod
    def login_user(cls, conn, email: str, password: str):
        # Fetch user's email and password in one query
        fetch_user_query = text("SELECT email, password FROM users WHERE email = :email")
        user_result = conn.execute(fetch_user_query, {'email': email}).fetchone()

        if user_result:
            # Directly access the email and password fields
            email = user_result[0]
            password_hash = user_result[1]

            # Now you can check the password
            if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
                return {'status_code': 200, "message": "Login Successful",
                        'data': {"email": email, "authenticated": True}}
            else:
                # Incorrect password
                return {'status_code': 200, "message": "LOGIN_FAILED",
                        'data': "Incorrect password"}
        else:
            # User does not exist
            return {'status_code': 200, "message": "USER_DOES_NOT_EXIST",
                    'data': {}}
