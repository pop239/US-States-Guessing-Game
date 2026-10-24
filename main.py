import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S STATS GAME")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

#this is how to get x&y position at any point in screen
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


guessed_state = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


while len(guessed_state) < 50:

    user_answer = turtle.textinput(title=f"{len(guessed_state)}/50 states correct" , prompt="What's another state's name?").title()#state

    if user_answer == "Exit":
        # instead of this:
        
        #     missing_state = []
        #
        #     for st in all_states:
        #         if st not in guessed_state:
        #             missing_state.append(st)


        # we can do this:
        missing_state = [st for st in all_states if st not in guessed_state]

        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_states.csv")
        break




    if user_answer == "Giveup":

        for m,i in data.iterrows():
            if i["state"] not in guessed_state:
                x=i["x"]
                y=i["y"]
                new = turtle.Turtle()
                new.hideturtle()
                new.penup()
                new.goto(x,y)
                new.write(i["state"])


    if user_answer in all_states:
        if user_answer in guessed_state:
            continue
        guessed_state.append(user_answer)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        state = data[data.state == user_answer]
        posX = int(state.x.item())
        posY = int(state.y.item())
        timmy.penup()
        timmy.goto(posX, posY)
        timmy.write(arg=f"{user_answer}", align="center", font=("Arial", 8, "normal"))










