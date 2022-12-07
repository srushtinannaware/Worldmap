import pandas
import turtle
import random

COLOR = ["red", "black", "green", "brown", "gray", "pink", "blue", "purple",
         "dark green", "orange", "dark blue"]
STYLE = ('Courier', 10, 'bold')

screen = turtle.Screen()
screen.title("My World Map")
image = "world_map.gif"
screen.addshape(image)
turtle.shape(image)

# def get_cor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_cor)
# turtle.mainloop()


data = pandas.read_csv("demo.csv")

all_countries = data.country.to_list()

guessed_countries = []

while len(guessed_countries) < 196:
    answer = screen.textinput(f"{len(guessed_countries)}/196 Correct", prompt="Whats the next country").title()

    if answer == "Exit":
        missing = []
        for country in all_countries:
            if country not in guessed_countries:
                missing.append(country)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("missing_countries.csv")
        break
    if answer in all_countries:
        guessed_countries.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinates = data[data.country == answer]
        t.goto(int(coordinates.x), int(coordinates.y))
        t.color(random.choice(COLOR))
        t.write(answer, font=STYLE, align="center")
