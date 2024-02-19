"""Unit Test for customer.py
"""


import unittest
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Customer Test Cases."""
    def setUp(self):
        # Setup runs before each test method
        Customer.customers_data.clear()  # Ensure a fresh start for each test

    def test_create_customer(self):
        """Test the creation of a customer."""
        customer = Customer.create_customer(
            "C01", "Peter T", "peter@email.com")
        self.assertIsInstance(customer, Customer)
        self.assertIn("C01", Customer.customers_data)

    def test_display_info(self):
        """Test displaying customer information."""
        customer = Customer("C02", "Ana P", "ana@email.com")
        expected_info = ("Customer ID: C02, "
                         "Name: Ana P, Email: ana@email.com")
        self.assertEqual(
            customer.display_info().strip(), expected_info.strip())

    def test_modify_info(self):
        """Test modyfing information."""
        customer = Customer("C03", "Lucas L", "lucas@email.com")
        customer.modify_info("Tomas S", "tomas@email.com")
        self.assertEqual(customer.name, "Tomas S")
        self.assertEqual(customer.email, "tomas@email.com")
        self.assertEqual(Customer.customers_data["C03"]["name"], "Tomas S")
        self.assertEqual(
            Customer.customers_data["C03"]["email"], "tomas@email.com")

    def test_delete_customer(self):
        """Test deleting a customer."""
        customer = Customer("C04", "Omar D", "Omar@email.com")
        customer.delete_customer()
        self.assertNotIn("C04", Customer.customers_data)

    # Negative test cases
    def test_modify_nonexistent_customer(self):
        """Modyfing a non existent customer."""
        customer = Customer("C07", "Cris C", "cris@email.com")
        Customer.customers_data.clear()  # Clear all existing customers
        with self.assertRaises(KeyError):
            customer.modify_info("New Name", "newemail@email.com")

    def test_create_customer_with_existing_id(self):
        """Adding a customer with a duplicate ID."""
        Customer("C08", "Lylla L", "lylla@email.com")
        with self.assertRaises(ValueError):
            Customer.create_customer("C08", "Duplicate", "duplicate@email.com")

    def test_invalid_email_format(self):
        """Modifying customer email with invalid format."""
        with self.assertRaises(ValueError):
            Customer("C09", "Invalid Email", "asdfghjkl")

    def test_empty_customer_name(self):
        """Modifying customer name with invalid format."""
        with self.assertRaises(ValueError):
            Customer("C10", "", "empty@email.com")


if __name__ == '__main__':
    unittest.main()
