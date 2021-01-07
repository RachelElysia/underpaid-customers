the_file = open("customer-orders.txt")

melon_cost = 1.00

#iterate through each line in the file
for line in the_file:
    customer_info = line.split('|')

    #create objects to represent information taken from each line
    customer_name = customer_info[1]
    customer_expected = float(customer_info[2]) * float(melon_cost)
    customer_paid = float(customer_info[3].rstrip())
    customer_first_name = customer_name.split(" ")[0]
    difference = round((customer_expected - customer_paid), 2)
    pay_status = "Correct payment"

    #catch if customer did not pay correctly and print statement
    if customer_expected != customer_paid:
        print(f"{customer_name} paid ${customer_paid},",
            f"expected ${customer_expected:.2f}"
        )
    
    #underpaid additional statement
    if customer_paid < customer_expected:
        pay_status = "Underpaid"
        print(f"{customer_first_name} has underpaid for their melons by ${difference}.")

    #overpaid additional statement, no one overpaid
    elif customer_paid > customer_expected:
        pay_status = "Overpaid"
        difference = abs(difference)
        print(f"{customer_first_name} has overpaid for their melons by ${difference}.")
    