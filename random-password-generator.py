# 4. Generate Random Password
def generate_password(length=12):
    import random
    import string
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")

length = int(input("Enter password length: "))
generate_password(length)


