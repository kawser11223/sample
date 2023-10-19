# class Brid:
#     name=''
#     size=''
#     colar=''
#     demo='hi'

#     def another_funce(self):
#         return 2+2

#     def funce_name(self):
#         print("hello",self.another_funce())

#     def show_name(self,username):
#         print("msg from out side the class:",username)    



# crow=Brid()
# crow.colar='black'


# sparrow=Brid()
# sparrow.name

# print(crow.colar,sparrow.name)

# print(sparrow.funce_name())

# crow.show_name("kawser")

class Room:
    length=0.0
    height=0.0
    width=0.0

    def __init__(self,a,b,c):
        self.height=a
        self.length=b
        self.width=c

        

    def Calculator(self):
        print("area of the given number is :",str(self.height*self.length*self.width))


# room1=Room()
# room1.height=7
# room1.length=9
# room1.width=5
# room1.Calculator()    

# room2=Room()
# room2.height=6
# room2.length=9
# room2.width=5
# room2.Calculator()

room3=Room(2,38,54)
room3.Calculator()

