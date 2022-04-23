from tabulate import tabulate

print(tabulate([["1. Fettuccine Alfredo", "  $16.99"], ["2. Chicken Alfredo", "$20.99"], ["3. Shrimp Scampi", "$21.99"]],   ["Pasta" , "  $", ], "fancy_grid"))

'''next line of code is for the table format in case i delete it again...
print(tabulate([["1. Fettuccine Alfredo", "  $16.99"], ["2. Chicken Alfredo", "$20.99"], ["3. Shrimp Scampi", "21.99"]],   ["Pasta" , "  $", ], "fancy_grid"))
'''
print(tabulate([["1. Zuppa Toscana", "  $8.99"], ["2. Chicken & Gnocchi", "$9.99"], ["3. Pasta e Fagioli", "$7.99"]],   ["Soups" , "  $", ], "fancy_grid")) 

print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],                 ["strings", "numbers"], "fancy_grid"))