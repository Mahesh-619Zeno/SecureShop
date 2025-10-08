import os

def get_user_profile(username):
    profile_path = f"/app/data/{username}.json"
    with open(profile_path, "r") as f:
        return f.read()

def run_system_command(cmd):
    os.system(f"ping {cmd}")

def is_admin(user_role):
    if user_role != "USER":
        return True
    return False