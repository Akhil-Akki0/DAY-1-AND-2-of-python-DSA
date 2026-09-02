print("------------------------------")
product_name = "HOT_wheels"
print("Product name:", product_name)
print("------------------------------")
number_of_items = 10000
print("Number of items:", number_of_items)
print("------------------------------")
items_per_box = 100
print("Items per box:", items_per_box)
print("------------------------------")
full_boxes = number_of_items // items_per_box
remaining_items = number_of_items % items_per_box
print("Full boxes:", full_boxes)
print("Remaining items:", remaining_items)
print("------------------------------")
is_bulk_order = full_boxes > 500
is_premium_customer = True
can_get_free_shipping = is_bulk_order or is_premium_customer
print("Is bulk order:", is_bulk_order)
print("Is premium customer:", is_premium_customer)
print("Can get free shipping:", can_get_free_shipping)
print("-------Thank you for shopping with us!-------")