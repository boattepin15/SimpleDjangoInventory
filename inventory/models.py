from django.db import models


class Product(models.Model):
    name = models.CharField("ชื่อสินค้า", max_length=100)
    qty = models.IntegerField("จำนวนสินค้า")
    category = models.CharField("หมวดหมู่สินค้า", max_length=100)
    price = models.DecimalField("ราคา", max_digits=10, decimal_places=2, default=0.00)
    update_at = models.DateField("แก้ไขเมื่อ", auto_now=True)
    def __str__(self):
        return f"{self.name} ({self.qty} ชิ้น) - ราคา {self.price} บาท"




