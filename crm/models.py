from django.db import models
from django.utils import timezone

class Customer(models.Model):
        name = models.CharField(max_length=100)
            email = models.EmailField(unique=True)
                phone = models.CharField(max_length=20, blank=True, null=True)

                    def __str__(self):
                                return self.name


                            class Product(models.Model):
                                    name = models.CharField(max_length=100)
                                        price = models.DecimalField(max_digits=10, decimal_places=2)
                                            stock = models.PositiveIntegerField(default=0)

                                                def __str__(self):
                                                            return f"{self.name} (${self.price})"


                                                        class Order(models.Model):
                                                                customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
                                                                    products = models.ManyToManyField(Product, related_name="orders")
                                                                        total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
                                                                            order_date = models.DateTimeField(default=timezone.now)

                                                                                def save(self, *args, **kwargs):
                                                                                            # Calculate total amount from products
                                                                                                    if not self.pk:  # Only calculate on creation
                                                                                                                    total = sum([p.price for p in self.products.all()])
                                                                                                                                self.total_amount = total
                                                                                                                                        super().save(*args, **kwargs)

                                                                                                                                            def __str__(self):
                                                                                                                                                        return f"Order {self.id} by {self.customer.name}"
                                                                                                                                    
