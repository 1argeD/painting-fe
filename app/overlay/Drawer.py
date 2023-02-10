import pynecone as pc


class DrawerState(pc.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)


pc.box(
    pc.button(
        "Show Right Drawer", on_click=DrawerState.right
    ),
    pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.drawer_header("Confirm"),
                pc.drawer_body(
                    "Do you want to confirm example?"
                ),
                pc.drawer_footer(
                    pc.button(
                        "Close", on_click=DrawerState.right
                    )
                ),
            )
        ),
        is_open=DrawerState.show_right,
    ),
)

pc.badge(DrawerState.show_right)

