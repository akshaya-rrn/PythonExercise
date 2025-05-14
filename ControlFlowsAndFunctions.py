print("""###############################################
                      String Compare                                    
      ##################################################""")


x = "HELLO"
y="HELLO"
if(x == y): 
    print("strings are same")
elif (X != Y):
    print("strings are not same")
else:
    print("else part")



number = 5

while number>0:
    print("Now, the number is {0}". format(number))
    number -= 1

for i in range(0,10):
    number+=1
    print("Now, the number incremented in for loop is {0}" . format(number))


while True:
    s =input(" Enter somthing: " )
    print (" User entered ", s)
    if s == 'quit': 
        break



def Function_without_params() :
    print ("im printing inside a functions")

Function_without_params()

Function_without_params()

def print_sum(a,b):
    print("printin_sum inside a function : ", a+b)
    return a+b

print_sum(5,6)
print_sum('a', 'b')



def say(message, times=2):
    print(message * times)

say('Hello ')

say('World ', 5)


