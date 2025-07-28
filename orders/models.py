from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MinValueValidator
from decimal import Decimal

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='France')
    phone = models.CharField(max_length=20, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Payment fields (placeholder for future payment integration)
    payment_method = models.CharField(max_length=50, default='card')
    payment_status = models.CharField(max_length=20, default='pending')
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_subtotal(self):
        return sum((item.price * item.weight* item.quantity) for item in self.items.all())

    def get_total_discount(self):
        return float(self.get_subtotal()) - float(self.get_total_cost())

    def get_total_weight(self):
        return sum(item.weight for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    weight = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(10)]) 

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return  self.calculate_discounted_price_per_weight

    @property
    def calculate_discounted_price_per_weight(self):
        discount = 0

        if self.weight >= 1000:
            discount = 0.30  # 30% discount
        elif self.weight >= 500:
            discount = 0.20  # 20% discount
        elif self.weight >= 100:
            discount = 0.10  # 10% discount
        elif self.weight >= 50:
            discount = 0.05

        unit_price = float(self.price) * float(1 - discount) * float(self.weight) * float(self.quantity)
        return round(unit_price, 2)
    
    @property
    def discount_price(self):
        return float(self.price) - (float(self.price) * (self.discount_percentage / 100))

    @property
    def discount_percentage(self):
        discount = 0

        if self.weight >= 1000:
            discount = 0.30  # 30% discount
        elif self.weight >= 500:
            discount = 0.20  # 20% discount
        elif self.weight >= 100:
            discount = 0.10  # 10% discount
        elif self.weight >= 50:
            discount = 0.05
        return 100 * discount
    


