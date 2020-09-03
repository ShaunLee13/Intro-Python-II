import textwrap

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {textwrap.fill(self.description, width=40)}\n'