import random


directions = ["NORTH", "WEST", "SOUTH", "EAST"]
commands = ["LEFT", "RIGHT", "MOVE"]


def toy(instructions):
    instructions = instructions.replace(" ", ",")
    instructions = instructions.split(",")

    if (instructions[0] == "PLACE"):
        try:
            x = int(instructions[1])
            y = int(instructions[2])
            if (x < 5 and y < 5 and x >= 0 and y >= 0):
                if (instructions[3] in directions):
                    direction = directions.index(instructions[3])
                    rest = instructions[4:]
                    return play(rest, x, y, direction)
                else:
                    print("WRONG ORIENTATION")
                    return False
            else:
                print("WRONG PLACING (x,y)")
                return False
        except:
            print("WRONG PLACING parse(x,y)")
            return False
    else:
        print("WRONG PLACING (PLACE)")
        return False


def play(rest, x, y, direction):
    for i in rest:
        if (i == "REPORT"):
            print(x, y, directions[direction])
        elif (i == "MOVE"):
            x, y = move(x, y, direction)
        elif (i == "LEFT"):
            direction += 1
            if (direction > 3): direction = 0
        elif (i == "RIGHT"):
            direction -= 1
            if (direction < 0): direction = 3
    return True


def move(x, y, direction):
    if (direction == 0 and y < 4):
        y += 1
    elif (direction == 1 and x > 0):
        x -= 1
    elif (direction == 2 and y > 0):
        y -= 1
    elif (direction == 3 and x < 4):
        x += 1
    return x, y


# def test(valid):
#     if (valid):
#         num = 4
#     else:
#         num = 20
#     s = "PLACE "
#     s += str(random.randint(0, num)) + "," + str(random.randint(0, num)) + "," + random.choice(directions) + " "
#     for i in range(random.randint(1, 10)):
#         comm = random.choice(commands)
#         if (comm != "MOVE"):
#             s += (comm + " ")
#         else:
#             s += (comm + " ") * random.randint(1, 5)
#     s += "REPORT"
#     return s
#
#
# for i in range(100):
#     s = test(True)  # True or False
#     print(s, end=" --> ")
#     toy(s)
#     print()


s = "PLACE 0,0,NORTH MOVE REPORT"
toy(s)
print()

s = "PLACE 0,0,NORTH LEFT REPORT"
toy(s)
print()

s =  "PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT"
toy(s)
print()
