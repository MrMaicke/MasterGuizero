from guizero import App, PushButton, Text, Box

app = App()

top_box = Box(app)
PushButton(top_box, text="1", align="left", height="2", width="4")
PushButton(top_box, text="2", align="left")
PushButton(top_box, text="3", align="left")

top_box = Box(app, align="top" , width="500", height="2")
PushButton(top_box, text="5", align="left")
PushButton(top_box, text="6", align="left")
PushButton(top_box, text="7", align="left")

top_box = Box(app, align="center" , width="500", height="2")
PushButton(top_box, text="8", align="left")
PushButton(top_box, text="9", align="left")
PushButton(top_box, text="⌫", align="left")


app.display()
