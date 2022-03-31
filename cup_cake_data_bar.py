total_sum_chocolate = 0
total_sum_vanilla = 0
total_sum_strawberry = 0

cup_cake_file = open("CupcakeInvoices.csv", 'r')
for line in cup_cake_file:
    word = line.split(',')
    if word[2] == "Chocolate":
      total_sum_chocolate = total_sum_chocolate + float(word[3])*float(word[4])
    elif word[2] == "Vanilla":
      total_sum_vanilla = total_sum_vanilla + float(word[3])*float(word[4])
    elif word[2] == "Strawberry":
        total_sum_strawberry = total_sum_strawberry + float(word[3])*float(word[4])

print(format(total_sum_chocolate, '.2f'))
print(format(total_sum_strawberry, '.2f'))
print(format(total_sum_vanilla, '.2f'))

cup_cake_file.close()