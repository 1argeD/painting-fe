import pynecone as pc

from app.overlay.Drawer import right
from app.pages import canvas


class State(pc.State):
    pass


app = pc.App(state=State)
app.add_page(canvas.canvas)
app.add_page(right)
app.compile()