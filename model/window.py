class Window(object):
    def __init__(self, width: int = 960, height: int = 540, icon_name: str = "icon.ico", is_customize: bool = False):
        self.width = width
        self.height = height
        self.icon_name = icon_name
        self.is_customize = is_customize
