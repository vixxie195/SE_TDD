import unittest
from user_management import UserManagement

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.user_management = UserManagement()
        self.user1 = {'name': 'Vixxie', 'age': 18}
        self.user2 = {'name': 'Mark', 'age': 21}

    def test_add_get_user_info(self):
        self.user_management.add_user(1, self.user1)
        self.assertEqual(self.user_management.get_user_info(1), self.user1)

    def test_add_update_user_info(self):
        self.user_management.add_user(1, self.user1)
        new_info = {'name': 'James Vixen', 'age': 35}
        self.user_management.update_user_info(1, new_info)
        self.assertEqual(self.user_management.get_user_info(1), new_info)

    def test_add_multiple_users_get_user_info(self):
        self.user_management.add_user(1, self.user1)
        self.user_management.add_user(2, self.user2)
        self.assertEqual(self.user_management.get_user_info(1), self.user1)
        self.assertEqual(self.user_management.get_user_info(2), self.user2)

if __name__ == '__main__':
    unittest.main()
