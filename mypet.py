from pet import Pet

class Mypet(Pet):
    def __init__(self, name, age, tipology, owner):
        Pet.__init__(self, name, age, tipology)
        self.owner = owner
    
    def say_hello(self):
        if self.tipology == 'cat':
            print('meow')
        elif self.tipology == 'dog':
            print('bau')
        elif self.tipology == 'horse':
            print('hihihi')