import pynecone as pc
from app.overlay.Drawer import DrawerState


def canvas():
    return pc.grid(
        pc.vstack(DrawerState),
        pc.grid_item(row_span=1, col_span=1, bg="black"),
        h="60em",
        width="100%",
        padding="1em",
    )

