from rest_framework import serializers
from .models import Order, OrderItem
from apps.inventory.serializers import ItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    item_detail = ItemSerializer(source="item", read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "item", "item_detail", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "user", "created_at", "total_amount", "is_paid", "items"]
        read_only_fields = ["total_amount"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        total = 0
        for item_data in items_data:
            item = item_data["item"]
            qty = item_data["quantity"]
            total += item.price * qty
            OrderItem.objects.create(order=order, **item_data)

        order.total_amount = total
        order.save()
        return order
