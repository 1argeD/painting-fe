import pynecone as pc

from app.overlay import Drawer


def canvas():
    return pc.center(
        pc.grid(
            pc.grid_item(row_span=1, col_span=1, bg="black"),
            h="60em",
            width="100%",
            padding="1em",
        )
    )


