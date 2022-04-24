'''
from tabulate import tabulate
print(tabulate([["1. Fettuccine Alfredo", "  $16.99", "4. Zuppa Toscana", "  $7.99", "7. Fountain Drinks", "$2.00"], ["2. Chicken Alfredo", "$20.99", "5. Chicken Gnocchi", "  $8.99", "8. Sweet Ice Tea", "$3.50"], ["3. Shrimp Scampa", "$21.99", "6. Pasta e Fagioli", "$9.99", "9. Regular Lemonade", "$3.99"]],   ["Pasta" , "  $", "Soups" , "  $", "Drinks", "  $" ], "fancy_grid"))
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

def SanrioCharacterSurvey():

  print('1) Hello Kitty')
  print('2) Kuromi')
  print('3) My Melody')
  print('4) Keroppi')
  print('5) Cinnamoroll')
'''
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

from tabulate import tabulate
print(tabulate([["1. Fettuccine Alfredo", "  $16.99", "4. Zuppa Toscana", "  $7.99", "7. Fountain Drinks", "$2.00", "Chocolate"], ["2. Chicken Alfredo", "$20.99", "5. Chicken Gnocchi", "  $8.99", "8. Sweet Ice Tea", "$3.50", "Strawberry"], ["3. Shrimp Scampa", "$21.99", "6. Pasta e Fagioli", "$9.99", "9. Regular Lemonade", "$3.99", "Vanilla"]],   ["Pasta" , "  $", "Soups" , "  $", "Drinks", "  $", "Ice Cream", "$" ], "fancy_grid"))
from tabulate import tabulate
IceCream = "Chocolate"
scoopsPrice = 1.50
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
