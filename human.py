from mypet import Mypet

class Human():
    def __init__(self, firstname, lastname, my_pet_name, my_pet_age, my_pet_tipology, my_pet_owner):
        self.firstname = firstname
        self.lastname = lastname
        self.my_pet = Mypet(my_pet_name, my_pet_age, my_pet_tipology, my_pet_owner)

    def say_hello(self):
        print(self.firstname + ' ' + self.lastname + ' ' + self.my_pet.name)
        return self.my_pet.say_hello()


a = Human('Gabriele', 'Valastro', 'Silvestro', 10, 'cat', 'Gabriele' )
a.say_hello()

b = Human('Marco', 'Nisi', 'Pluto', 15, 'dog', 'Marco' )
b.say_hello()

c = Human('Nancy', 'Nisi', 'Furia', 9, 'horse', 'Nancy' )
c.say_hello()