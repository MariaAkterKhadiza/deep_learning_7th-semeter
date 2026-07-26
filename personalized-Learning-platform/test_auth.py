from modules.auth import register_user, login_user



# Test Registration

result = register_user(
    "Maria",
    "maria@gmail.com",
    "123456"
)


print("Registration:", result)



# Test Login

login = login_user(
    "maria@gmail.com",
    "123456"
)


print("Login:", login)