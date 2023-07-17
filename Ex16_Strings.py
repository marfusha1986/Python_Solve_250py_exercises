my_string = "In %s, someone paid %s %s for two pizzas."

print("In %(year)s, someone paid %(cost)s %(money)s for two pizzas."%{'year':'2010','cost':'10k','money':'Bitcoin'})
print(my_string %('2010','10k','Bitcoin'))