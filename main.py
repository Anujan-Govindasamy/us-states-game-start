import turtle
import pandas
FONT = ("Courier", 8, "normal")

writer=turtle.Turtle()
screen = turtle.Screen()
screen.title("us state quiz game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()
correct_found_count=0
correct_answers=[]
list_unanswered_states = []
game_on=True

while game_on:
    answer_state=turtle.textinput(title=f"{correct_found_count}/50 states found",prompt="guess the name of the state")

    answer_value=answer_state.title()
    # print(answer_value)

    if answer_state == "exit":
        list_unanswered_states = [each_state for each_state in list_of_states if each_state not in correct_answers]
        break

    for each_state in list_of_states:

        if answer_value == each_state and answer_value not in correct_answers:
            correct_found_count += 1
            correct_answers.append(each_state)
            state_coordinates=data[data.state == each_state]
            state_x = int(state_coordinates.x.iloc[0])
            state_y = int(state_coordinates.y.iloc[0])
            writer.penup()
            writer.color("black")
            writer.hideturtle()
            writer.goto(x=state_x,y=state_y)
            writer.write(arg=f"{each_state}",align="center",font=FONT)

    if correct_found_count == 50:
        game_on = False


# creating a csv file of unanswered states


unanswered_data_dict ={
    "unanswered states":list_unanswered_states
}

unanswered_data = pandas.DataFrame(unanswered_data_dict)

unanswered_data.to_csv("unanswered_states.csv")











