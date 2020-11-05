import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):


    def test_email(self):
        emp_1 = Employee('James', 'Hudnall', 50000)
        emp_2 = Employee('Sam', 'Hudnall', 45000)

        self.assertEqual(emp_1.email, 'James.Hudnall@email.com')
        self.assertEqual(emp_2.email, 'Sam.Hudnall@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'
    
        self.assertEqual(emp_1.email, 'John.Hudnall@email.com')
        self.assertEqual(emp_2.email, 'Jane.Hudnall@email.com')

    def test_fullname(self):
        emp_1 = Employee('James', 'Hudnall', 50000)
        emp_2 = Employee('Sam', 'Hudnall', 45000)

        self.assertEqual(emp_1.fullname, 'James Hudnall')
        self.assertEqual(emp_2.fullname, 'Sam Hudnall')

        emp_1.first = 'John'
        emp_2.first = 'Jane'
        
        self.assertEqual(emp_1.fullname, 'John Hudnall')
        self.assertEqual(emp_2.fullname, 'Jane Hudnall')

    def test_apply_raise(self):
        emp_1 = Employee('James', 'Hudnall', 50000)
        emp_2 = Employee('Sam', 'Hudnall', 45000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 47250)


if __name__ == '__main__':
    unittest.main()