print('Hello World')
cup_cake_file = open("CupcakeInvoices.csv")
for row in cup_cake_file:
  print(row)

cup_cake_file.seek(0)

for cup_cakes in cup_cake_file:
  cup_cakes = cup_cakes.rstrip('\n').split(',')
  for item in cup_cakes:
    if item == "Chocolate":
      print("Chocolate")
    elif item == "Vanilla":
      print("Vanilla")
    elif item == "Strawberry":
      print("Strawberry")


cup_cake_file.close()

cup_cake_file = open("CupcakeInvoices.csv", 'r')


for line in cup_cake_file:
    word = line.split(',')
    multiply_two = float(word[3])*float(word[4])
    print(multiply_two)

cup_cake_file.close()

total_sum = 0
cup_cake_file = open("CupcakeInvoices.csv", 'r')
for line in cup_cake_file:
    word = line.split(',')
    total_sum = total_sum + float(word[3])*float(word[4])

print(format(total_sum, '.2f'))

cup_cake_file.close()
