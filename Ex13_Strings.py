my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
list_of = [n for n in my_string]
joined = "&".join(list_of)
print(joined)

print("&".join(my_string))