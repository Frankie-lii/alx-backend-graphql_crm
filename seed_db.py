#!/usr/bin/env python3
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_backend_graphql_crm.settings")
django.setup()

from crm.models import Customer, Product

def run():
        # Seed Customers
            Customer.objects.get_or_create(name="Alice", email="alice@example.com", phone="+1234567890")
                Customer.objects.get_or_create(name="Bob", email="bob@example.com")

                    # Seed Products
                        Product.objects.get_or_create(name="Laptop", price=999.99, stock=10)
                            Product.objects.get_or_create(name="Phone", price=499.99, stock=20)

                                print("Database seeded successfully!")

                                if __name__ == "__main__":
                                        run()
                                        

