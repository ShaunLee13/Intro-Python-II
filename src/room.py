# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, ground):
        self.name = name
        self.description = description
        self.ground = ground

    # def __str__(self):
    #     ret = f"{self.name}\n"
    #     for g in self.ground.items():
    #         ret += g.name + "\n"
        
    #     return ret