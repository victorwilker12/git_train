class Animal:
    def __init__(self, name, specie, classification):
        self.name = name
        self.specie = specie
        self.classification = classification 
    def make_noise(self):
        return f"The {self.name} makes {self.sound}!"

