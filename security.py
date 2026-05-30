class Security:
    def __init__(self):
        self.roles = {
            "admin": ["read", "write", "delete"],
            "student": ["read", "write"],
            "guest": ["read"]
        }

    def check(self, role, action):
        if action in self.roles.get(role, []):
            return True
        else:
            print(f"SECURITY ALERT: {role} denied {action}")
            return False