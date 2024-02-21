class UserManagement:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_info):
        self.users[user_id] = user_info

    def get_user_info(self, user_id):
        return self.users.get(user_id)

    def update_user_info(self, user_id, new_info):
        if user_id in self.users:
            self.users[user_id].update(new_info)
        else:
            raise ValueError("User not found")
