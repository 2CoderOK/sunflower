import random

weather = {"Sunny": 1, "Rainy": 2, "Cloudy": 0, "Windy": -1, "Burning sun": -2}
height = 1
max_height = 1
day = 1
good_days = 3

print("Good morning little flower!!!\n")

while height > 0:
    print(f"Day {day}")

    w = random.choice(list(weather.keys()))
    print(f"The weather is {w}")

    if good_days > 0:
        height += 1
        good_days -= 1
    else:
        height += weather[w]
    print(f'Sunflower`s height is {height}"\n\n')

    if height > max_height:
        max_height = height

    day += 1

print("Your sunflower is gone ...\n")
print(f"Sunflower survived {day} days")
print(f'Sunflower`s max height was {max_height}"\n\n')

print("Good luck with your next sunflower")
