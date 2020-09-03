from item import Item

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def __str__(self):
        return f'{super().__str__()}This treasure is worth {self.value} gold!'