import random
a = {"water": 55, "potato": 35, "bread": 25, "barbecue": 40, "coal": 45, "beer": 20, "whiskey": 30}
maximum_load = 100
counter = 0
List_artibute = []
while counter < maximum_load:
    key, value = random.choice(list(a.items()))
    if key in List_artibute:
        continue
    if counter + value > maximum_load:
        break
    counter += value
    List_artibute += (str(key), str(value))
print(List_artibute, "=", counter)