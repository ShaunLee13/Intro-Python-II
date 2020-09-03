# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

class Player:
    def __init__(self,name, location):
        self.name = name
        self.location = location
        self.inventory = []
        self.score = 0
    
    def __str__(self):
        return f'You are currently at {self.location.name}\n\n{textwrap.fill(self.location.description)}\n'

    def get(self, item):
        self.inventory.append(item)
        print(f'You pick up the {item.name}')
        if hasattr(item, 'value'):
            self.score += item.value
            print(f"You're score's changed! {self.score}")

    def drop(self, item):
        self.inventory.remove(item)
        print(f'You drop the {item.name}')
        if hasattr(item, 'value'):
            self.score -= item.value
            print(f"You're score's changed! {self.score}")

    def __repr__(self):
        return f'{self.name},{self.location}'