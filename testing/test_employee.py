import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('James', 'Hudnall', 50000)
        self.emp_2 = Employee('Sam', 'Hudnall', 45000)

    def tearDown(self):
        """Useful for deleting temporary testing files, directories, databases, etc """
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'James.Hudnall@email.com')
        self.assertEqual(self.emp_2.email, 'Sam.Hudnall@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
    
        self.assertEqual(self.emp_1.email, 'John.Hudnall@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Hudnall@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'James Hudnall')
        self.assertEqual(self.emp_2.fullname, 'Sam Hudnall')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.fullname, 'John Hudnall')
        self.assertEqual(self.emp_2.fullname, 'Jane Hudnall')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 47250)


if __name__ == '__main__':
    unittest.main()