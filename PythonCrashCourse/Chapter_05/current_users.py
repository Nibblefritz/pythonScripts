current_users = ['hector', 'joe', 'kyle', 'admin', 'fabio']
new_users = ['Bob', 'joe', 'bill', 'Euberta', 'hector']

for user in new_users:
    if user.lower() in current_users:
        print(f"User {user.lower()} is already a current user")
    else:
        print(f"The username {user.lower()} is available")