from guizero import App, PushButton, Slider

def print_pos(x, y):
    print("{}, {}".format(x, y))

def print_bottom():
    print("bottom button")

def hide():
    b00.hide()
    b01.hide()
    b10.hide()
    b11.hide()
    b_bottom.hide()

def show():
    b00.show()
    b01.show()
    b10.show()
    b11.show()
    b_bottom.show()

app = App(layout="grid")

b00 = PushButton(app, print_pos, text="1", args=[0,0], grid=[0,0])
b01 = PushButton(app, print_pos, text="4", args=[0,1], grid=[0,1])
b10 = PushButton(app, print_pos, text="2", args=[1,0], grid=[1,0])
b11 = PushButton(app, print_pos, text="5", args=[1,1], grid=[1,1])
b20 = PushButton(app, print_pos, text="3", args=[2,0], grid=[2,0])
b21 = PushButton(app, print_pos, text="6", args=[2,1], grid=[2,1])
b30 = PushButton(app, print_pos, text="7", args=[0,3], grid=[3,3])
b31 = PushButton(app, print_pos, text="8", args=[3,1], grid=[3,1])
b40 = PushButton(app, print_pos, text="9", args=[3,2], grid=[4,0])

app.display()