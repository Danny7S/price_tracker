from django.db import models
from catalog.models import Product
from stores.models import Store

class StorePrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, max_length=200)

    def __str__(self):
        return f"{self.product.name} -> {self.store.name} - {self.price}lv." # Да си припомним една легенда