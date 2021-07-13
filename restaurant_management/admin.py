from django.contrib import admin
from django import forms
import codecs
from django.shortcuts import redirect, render

import datetime
import os

from .models import *
from django.urls import path


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "phone")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("pk", "customer_id", "date", "amount")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "price")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "order_id", "product_id", "quantity")
