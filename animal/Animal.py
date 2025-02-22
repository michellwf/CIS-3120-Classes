class Animal:
    def __init__(self, name, species, energy=100): 
        self.__name = name
        self.__species = species
        self.__energy = energy
        print("Hello, I am", self.__name, "and I am a", self.__species)
        print("Energy level:", self.__energy)

    def sound(self, sound):
        self.__energy -= 10
        self.__sound = sound
        print(f"{self.__sound} {self.__sound}!")
        print("Energy level:", self.__energy)

    def love(self, thing1, thing2):
        self.__thing1= thing1
        self.__thing2=thing2
        self.__energy -= 10
        print(f"{self.__name} loves {self.__thing1} and {self.__thing2}")
        print("Energy level:", self.__energy)

    def play(self):
        self.__energy -= 45
        print(f"{self.__name} plays happily")
        print("Energy level:", self.__energy)

    def food(self):
        self.__energy += 50
        print(f"{self.__name} eats lots of tasty food")
        print("Energy level:", self.__energy)

    def sleep(self):
        self.__energy = 100
        print(f"It's the end of the day and {self.__name} goes to sleep")
        print("Energy level:", self.__energy)
        print(f"Bye {self.__sound} Bye {self.__sound}!")

    def energyup(self):
        self.__energy = 100


