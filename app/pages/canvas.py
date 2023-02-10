import pynecone as pc
from app.overlay.Drawer import DrawerState


def right():
    return pc.vstack(
        on_click=DrawerState.right,
        )


def canvas():
    return pc.grid(
        pc.grid_item(row_span=1, col_span=1, bg="black"),
        h="60em",
        width="100%",
        padding="1em",
    )


