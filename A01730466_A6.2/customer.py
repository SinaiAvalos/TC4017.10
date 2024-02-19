"""Customer module.
"""
import re


class Customer:
    """
    Represents a customer with attributes such as name and email.
    """

    # Class variable to store all customers' data
    customers_data = {}

    def __init__(self, customer_id, name, email):
        """
        Initializes a new Customer object.

        Args:
            customer_id (str): The unique identifier of the customer.
            name (str): The name of the customer.
            email (str): The email address of the customer.
        """
        self.customer_id = customer_id
        if customer_id in self.customers_data:
            raise ValueError("customer_id must be unique")
        if not name.strip():
            raise ValueError("The name cannot be empty.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        self.name = name
        self.email = email
        # Add customer data to the class variable
        self.customers_data[customer_id] = {
            "name": name,
            "email": email
        }

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """
        Creates a new Customer object.
        """
        customer = cls(customer_id, name, email)
        return customer

    def display_info(self):
        """
        Display information about the customer.
        """
        customer_info = (f"Customer ID: {self.customer_id}, "
                         f"Name: {self.name}, Email: {self.email}")
        print(f"\n{customer_info} \n")  # Print customer information
        return customer_info.strip()  # Return customer information as a string

    def modify_info(self, new_name, new_email):
        """
        Modify the information of the customer.
        """
        # Check if the customer exists
        if self.customer_id not in self.customers_data:
            raise KeyError(f"Customer ID '{self.customer_id}' does not exist.")

        # Validate the new name
        if not new_name.strip():
            raise ValueError("The name cannot be empty.")

        # Validate the new email using a basic pattern
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            raise ValueError("Invalid email format.")

        # If validations pass, proceed to update the customer's information
        self.name = new_name
        self.customers_data[self.customer_id]["name"] = new_name
        self.email = new_email
        self.customers_data[self.customer_id]["email"] = new_email

    def delete_customer(self):
        """
        If the customer exists, it removes it from the data.
        """
        if self.customer_id in Customer.customers_data:
            del Customer.customers_data[self.customer_id]
            print(f"Customer '{self.name}' deleted successfully.")
        else:
            raise KeyError("Customer ID does not exist.")
