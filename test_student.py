import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        print("Setup")
        self.student = Student("John", "Doe")

    
    def tearDown(self):
        print("Tear Down")


    def test_full_name(self): 
        print("Test full name")
        self.assertEqual(self.student.full_name, "John Doe")


    def test_email_address(self):
        print("Test email address")
        self.assertEqual(self.student.email_address, "john.doe@email.com")


    def test_alert_santa(self):
        print("Test alert santq")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


if __name__ == "__main__":
    unittest.main()
