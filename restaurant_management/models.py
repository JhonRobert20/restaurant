from django.contrib.gis.db import models
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, unique=False, blank=True)
    phone = models.CharField(max_length=20, null=True, unique=False, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return f"Anonymous: {self.pk}"


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, to_field='id', on_delete=models.CASCADE, null=False,
                                    blank=True, unique=False)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, unique=False)
    amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, unique=False)

    def __str__(self):
        return f"Mr o Miss : {self.customer_id.__str__()}, date : {self.date}"


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False, unique=False)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, to_field='id', on_delete=models.CASCADE, null=False, unique=False, blank=False)
    product_id = models.ForeignKey(Product, to_field='id', on_delete=models.CASCADE,
                                   null=False, unique=False, blank=False)
    quantity = models.IntegerField(null=False, unique=False, blank=False)


@receiver(pre_save, sender=OrderItem)
def pre_save(sender, instance, **kwargs):
    order = Order.objects.get(pk=instance.order_id.pk)
    product = Product.objects.get(pk=instance.product_id.pk)

    total_price_per_product = product.price * instance.quantity
    if order.amount:
        order.amount = order.amount + total_price_per_product
    else:
        order.amount = total_price_per_product
    order.save()
    print(order.amount)


@receiver(pre_delete, sender=OrderItem)
def pre_delete(sender, instance, **kwargs):
    order = Order.objects.get(pk=instance.order_id.pk)
    product = Product.objects.get(pk=instance.product_id.pk)

    total_price_per_product = product.price * instance.quantity
    if order.amount:
        order.amount = order.amount - total_price_per_product if order.amount >= total_price_per_product else 0
    else:
        order.amount = 0

    order.save()





