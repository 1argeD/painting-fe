import pynecone as pc
from tkinter import *

from app.pages import painting


class State(pc.State):
    pass


app = pc.App(state=State)
app.add_page(painting.about)
app.add_page(painting.paint, path="/paint")
app.compile()