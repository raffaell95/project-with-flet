import flet as ft


class MainContent(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self):
        return ft.Container()