import unittest

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

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.user_management = UserManagement()
        self.user1 = {'name': 'Vixxie', 'age': 18}
        self.user2 = {'name': 'Mark', 'age': 21}

    def test_add_user(self):
        self.user_management.add_user(1, self.user1)
        self.assertEqual(self.user_management.users[1], self.user1)

    def test_get_user_info(self):
        self.user_management.add_user(1, self.user1)
        self.assertEqual(self.user_management.get_user_info(1), self.user1)

    def test_update_user_info(self):
        self.user_management.add_user(1, self.user1)
        new_info = {'name': 'James Vixen', 'age': 35}
        self.user_management.update_user_info(1, new_info)
        self.assertEqual(self.user_management.get_user_info(1), new_info)

    def test_update_user_info_non_existing_user(self):
        with self.assertRaises(ValueError):
            self.user_management.update_user_info(2, {'name': 'Jane', 'age': 33})

if __name__ == '__main__':
    unittest.main()
