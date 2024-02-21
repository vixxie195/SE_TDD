# user_management_tests.py
import unittest
from user_management import UserManagement

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
