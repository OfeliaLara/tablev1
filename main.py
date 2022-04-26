'''
from tabulate import tabulate
print(tabulate([["1. Fettuccine Alfredo", "  $16.99", "4. Zuppa Toscana", "  $7.99", "7. Fountain Drinks", "$2.11"], ["2. Chicken Alfredo", "$20.99", "5. Chicken Gnocchi", "  $8.99", "8. Sweet Ice Tea", "$3.55"], ["3. Shrimp Scampi", "$21.99", "6. Pasta e Fagioli", "$9.99", "9. Regular Lemonade", "$3.99"]],   ["Pasta" , "  $", "Soups" , "  $", "Drinks", "  $" ], "fancy_grid"))
'''
'''
Friend_Q1= input('What is your name? ')
Friend_Q2= input('What is your favorite show? ')
Friend_Q3 = input('Who is your favorite artist? ')

if ("I don't know" in Friend_Q1 or "I don't know" in Friend_Q2 or "I don't know" in Friend_Q3): 
  print("You don't seem like a nice person...")
else: 
  print ("You seem like an awesome person, " + Friend_Q1 +"!")
'''
'''
total = 11

#Mrs.Bridges is giving out instruments to new students. This subtracts instruments. 

def subtractInstruments():
  global total
  total -= 1

#continue subtracting until the all 10 instruments are left.
for i in range(11):
  subtractInstruments()
  if(i == 9):
    print(str(total)+ " instrument is left.")
  else:
    print(str(total)+ " instruments are left.")

print("There's no more instruments to give out!")          
'''
'''
def SanrioCharacterSurvey():

  print('1) Hello Kitty')
  print('2) Kuromi')
  print('3) My Melody')
  print('4) Keroppi')
  print('5) Cinnamoroll')

  while True: 
    try: 
      question = int(input('Out of these options, (1,2,3,4,5), which is your favorite Sanrio Character? '))
      break
    except:
      print("That's not a valid option!")
  if question == 1:
    print('She is cool! ')
  elif question ==2:
    print("We stan an iconic queen!")
  elif question ==3:
    print('She is so adorable!')
  elif question ==4:
    print('He is awesome!')
  elif question ==5:
    print("He's so chubby and cute!")
  else:
    print("That's not an option, you silly goose!")

SanrioCharacterSurvey()

'''

'''
from tabulate import tabulate
print(tabulate([["1. Fettuccine Alfredo", "  $16.99", "4. Zuppa Toscana", "  $7.99", "7. Fountain Drinks", "$2.11", "10. Chocolate", "$1.55", ], ["2. Chicken Alfredo", "$17.35", "5. Chicken Gnocchi", "  $8.99", "8. Sweet Ice Tea", "$3.55", "11. Strawberry", "$1.55"], ["3. Shrimp Scampi", "$18.59", "6. Pasta e Fagioli", "$9.99", "9. Regular Lemonade", "$3.99", "12. Vanilla", "$1.55"]],   ["Pasta" , "  $", "Soups" , "  $", "Drinks", "  $", "Ice Cream", "$ per scoop" ], "fancy_grid")) 
from tabulate import tabulate
IceCream = "Chocolate"
scoopsPrice = 1.55
total = 0.0
scoopsCount = 0 

scoopsCount = input ("How many scoops of IceCream would you like? Please put a numerical value. For example: 1\n")
scoopsCount = float (scoopsCount)

totalForIceCream = scoopsCount*scoopsPrice
total += totalForIceCream
print ("${:0.2f}". format (total))

print("Here's your receipt!")
table = [[int (scoopsCount), "Ice Cream","${:0.2f}".format (scoopsPrice)+ " per scoop"],["","TOTAL", "${:0.2f}".format(total) ]]
headers= ["Number", "Item", "Price"]
print("\n")
print (tabulate(table, headers))

'''





from tabulate import tabulate
print(tabulate([["1. Fettuccine Alfredo", "  $16.99", "4. Zuppa Toscana", "  $7.99", "7. Fountain Drinks", "$2.11", "10. Chocolate", "$1.55", ], ["2. Chicken Alfredo", "$17.35", "5. Chicken Gnocchi", "  $8.99", "8. Sweet Ice Tea", "$3.55", "11. Strawberry", "$1.55"], ["3. Shrimp Scampi", "$18.59", "6. Pasta e Fagioli", "$9.99", "9. Regular Lemonade", "$3.99", "12. Vanilla", "$1.55"]],   ["Pasta" , "  $", "Soups" , "  $", "Drinks", "  $", "Ice Cream", "$ per scoop" ], "fancy_grid")) 

total=0 
order=[]

#waiter is telling the customer to pick a type of pasta.
pasta = input("Pick a type of pasta: Fettuccine Alfredo, Chicken Alfredo or Shrimp Scampi? ")

print(pasta )
if pasta.lower()== "fettucine alfredo":
    order.append("fettucine alfredo")
    total = 16.99

elif pasta.lower()== "chicken alfredo":
    order.append("chicken alfredo")
    total = 17.35
elif pasta.lower()== "shrimp scampi":
    order.append("shrimp scampi")
    total = 18.59

print("That will be $",total, ".")

#waiter is telling the customer to pick a type of soup.

soup = input("Pick a type of soup: Zuppa Toscana, Chicken Gnocchi or Pasta e Fagioli? ")

print(soup )
if soup.lower()== "zuppa toscana":
    order.append("zuppa toscana")
    total = 7.99

elif soup.lower()== "chicken gnocchi":
    order.append("chicken gnocchi")
    total = 8.99
elif soup.lower()== "pasta e fagioli":
    order.append("pasta e fagioli")
    total = 9.99

print("That will be $",total, ".")

#waiter is telling the customer to pick a type of drink.

drink=input("Pick a type of drink: Fountain Drinks, Sweet Ice Tea, or Regular Lemonade? ")
print(drink )
if drink.lower()== "fountain drinks":
    order.append("fountain drinks")
    total = 2.11

elif drink.lower()== "sweet ice tea":
    order.append("sweet ice tea")
    total = 3.55
elif drink.lower()== "regular lemonade":
    order.append("regular lemonade")
    total = 3.99

print("That will be $",total, ".")

#waiter is telling them to pick an icecream flavor
IceCream = input("Pick an Ice Cream Flavor: Chocolate, Strawberry or Vanilla? ")

print(IceCream )
if IceCream.lower()== "chocolate":
    order.append("chocolate")
    total = 1.55

elif IceCream.lower()== "strawberry":
    order.append("strawberry")
    total = 1.55
elif IceCream.lower()== "vanilla":
    order.append("vanilla")
    total = 1.55

print("That will be $", total, ".")
