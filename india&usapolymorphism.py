class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developed country.")

class USA():
    def capital(self):
        print("Washington D.C. is the capital of the USA. ")

    def language(self):
        print("English is the most widely spoken language of the USA.")

    def type(self):
        print("USA is a developing country.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()