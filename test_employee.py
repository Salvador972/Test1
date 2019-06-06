import unittest
from employee import Employee



class TestEmployee(unittest.TestCase):


    def test_email(self):

        emp_1 = Employee('Jesus','Garcia',50000)
        emp_2 = Employee('Salvador','Escamilla',60000)

        self.assertEqual(emp_1.email,'Jesus.Garcia@email.com')
        self.assertEqual(emp_2.email,'Salvador.Escamilla@email.com')

        emp_1.first = 'Juan'
        emp_2.first = 'Juana'

        self.assertEqual(emp_1.email, 'Juan.Garcia@email.com')
        self.assertEqual(emp_2.email, 'Juana.Escamilla@email.com')

    def test_fullname(self):

        emp_1 = Employee('Jesus','Garcia',50000)
        emp_2 = Employee('Salvador','Escamilla',60000)

        self.assertEqual(emp_1.fullname,'Jesus Garcia')
        self.assertEqual(emp_2.fullname,'Salvador Escamilla')

        emp_1.first ='Juan'
        emp_2.first ='Juana'

        self.assertEqual(emp_1.fullname,'Juan Garcia')
        self.assertEqual(emp_2.fullname,'Juana Escamilla')

    def test_apply_raise(self):
        emp_1 = Employee('Jesus','Garcia', 50000)
        emp_2 = Employee('Salvador','Escamilla',60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
