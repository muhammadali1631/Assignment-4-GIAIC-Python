import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    hashed = hash_password(password_to_check)
    if email in stored_logins:
        return stored_logins[email] == hashed
    return False

def main():
    stored_logins = {
        "ali@example.com": hash_password("mysecurepassword"),
        "john@example.com": hash_password("123456"),
    }

    print(login("ali@example.com", "mysecurepassword", stored_logins))
    print(login("ali@example.com", "wrongpassword", stored_logins))
    print(login("unknown@example.com", "any", stored_logins))

main()
