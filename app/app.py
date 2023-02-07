import pynecone as pc

from app.pages import canvas


class State(pc.State):
    pass


app = pc.App(state=State)
app.add_page(canvas.canvas)
app.compile()