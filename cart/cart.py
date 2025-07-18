from decimal import Decimal
from django.conf import settings
from products.models import Product


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

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)  # Store as string to avoid Decimal serialization issues
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
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
                total_price = price * quantity
                
                # Add calculated fields (but don't store them in session)
                item['price_decimal'] = price
                item['total_price'] = total_price
                yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculate the total cost of the items in the cart.
        """
        total = Decimal('0')
        for item in self.cart.values():
            total += Decimal(item['price']) * item['quantity']
        return total

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
            product_details.append({
                'product': product,
                'quantity': item['quantity'],
                'price': float(item['price']),
                'total_price': float(item['price']) * item['quantity']
            })
        return product_details