import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# Create a new variable "image"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Use a loop to allow the user to keep guessing
while len(guessed_states) < 50:
    # Keep track of the score
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()
    if answer_state == "Exit":
        # Record the missing states in a list and create a "States to learn.csv"
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the guess is among the 50 states
    if answer_state in all_states:
        # If they got right:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # Write correct guesses onto the map
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





# screen.exitonclick()
