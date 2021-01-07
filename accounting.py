the_file = open("customer-orders.txt")

melon_cost = 1.00

#iterate through each line in the file
for line in the_file:
    customer_info = line.split('|')

    #create objects to represent information taken from each line
    customer_name = customer_info[1]
    customer_expected = float(customer_info[2]) * melon_cost
    customer_paid = float(customer_info[3].rstrip())

    if customer_expected != customer_paid:
        print(f"{customer_name} paid ${customer_paid},",
            f"expected ${customer_expected:.2f}"
        )
    

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )
