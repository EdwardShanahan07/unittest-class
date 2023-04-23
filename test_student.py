import unittest
from student import Student
from datetime import timedelta

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

    def test_apply_extensions(self):
        old_end_date = self.student.end_date
        self.student.apply_extensions(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))



if __name__ == "__main__":
    unittest.main()
