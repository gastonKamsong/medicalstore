from decimal import Decimal
from django.conf import settings
from products.models import Product
from django.core.validators import MinValueValidator


class Cart:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, weight=10, override_quantity=False, override_weight=False):
        """
        Add a product to the cart or update its quantity and weight.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'weight': weight,
                'price': str(product.price)  # Store as string to avoid Decimal serialization issues
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        if override_weight:
            self.cart[product_id]['weight'] = weight
            
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        # Process items for display - convert strings back to Decimal for calculations
        for item in cart.values():
            if 'product' in item:  # Only process items that have products
                price = Decimal(item['price'])
                quantity = item['quantity']
                weight = item.get('weight', 10)  # Default weight if not set
                total_price = self._calculate_discounted_price(price, quantity, weight)
                
                # Add calculated fields (but don't store them in session)
                item['price_decimal'] = price
                item['weight'] = weight
                item['total_price'] = total_price
                item['discounted_price_per_unit'] = self._get_discounted_unit_price(price, weight)
                yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculate the total cost of the items in the cart with weight discounts applied.
        """
        total = Decimal('0')
        for item in self.cart.values():
            price = Decimal(item['price'])
            quantity = item['quantity']
            weight = item.get('weight', 10)
            total += self._calculate_discounted_price(price, quantity, weight)
        return total

    def _calculate_discounted_price(self, price, quantity, weight):
        """
        Calculate the discounted price based on weight.
        """
        discount = self._get_discount_percentage(weight)
        discounted_price = price * (1 - discount) * weight * quantity
        return round(discounted_price, 2)

    def _get_discount_percentage(self, weight):
        """
        Get discount percentage based on weight.
        """
        if weight >= 1000:
            return Decimal('0.30')  # 30% discount
        elif weight >= 500:
            return Decimal('0.20')  # 20% discount
        elif weight >= 100:
            return Decimal('0.10')  # 10% discount
        elif weight >= 50:
            return Decimal('0.05')  # 5% discount
        return Decimal('0')  # No discount

    def _get_discounted_unit_price(self, price, weight):
        """
        Get discounted price per unit weight.
        """
        discount = self._get_discount_percentage(weight)
        return round(price * (1 - discount), 2)

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
        
    def get_products_detail(self):
        """Return a list of product details for all items in the cart"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        product_details = []
        for product in products:
            item = self.cart[str(product.id)]
            weight = item.get('weight', 10)
            price = Decimal(item['price'])
            total_price = self._calculate_discounted_price(price, item['quantity'], weight)
            
            product_details.append({
                'product': product,
                'quantity': item['quantity'],
                'weight': weight,
                'price': float(price),
                'discounted_unit_price': float(self._get_discounted_unit_price(price, weight)),
                'total_price': float(total_price)
            })
        return product_details