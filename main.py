class Animal:
    def __init__(self, name, specie, sound):
        self.name = name
        self.specie = specie
        self.sound = sound 
    def make_noise(self):
        return f"The {self.name} makes {self.sound}!"

