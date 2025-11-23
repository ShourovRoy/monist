from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Necklace', 'Necklace'),
        ('Ring', 'Ring'),
        ('Earring', 'Earring'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
