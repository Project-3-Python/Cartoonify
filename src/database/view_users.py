import sqlite3

def view_users():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()

    if users:
        print("Registered Users:")
        for user in users:
            print(f"Email: {user[0]}, Password: {user[1]}")
    else:
        print("No registered users found.")

view_users()
