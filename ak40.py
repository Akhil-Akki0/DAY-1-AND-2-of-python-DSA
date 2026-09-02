foods = {
    ("hot","fresh") : "soda",
    ("cold" , "kick") : "sprite",
    ("cool" , "relax") : "water",
}

food1 = ("hot","fresh")
print(f"food:{foods[food1]} tasty")
food_pais = list(foods.keys())
for pair in food_pais:
    foodx , foody = pair
    print(f"{foodx} and {foody}:{foods[pair]} tasty")