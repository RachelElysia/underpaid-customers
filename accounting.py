
#this is a constant so it's capitalized
MELON_COST = 1.00

def print_payment_status(payment_file):
    payment_data = open(payment_file)
    #iterate through each line in the file
    for line in payment_data:
        customer_info = line.split('|')

        #create objects to represent information taken from each line
        customer_name = customer_info[1]
        customer_expected = float(customer_info[2]) * float(MELON_COST)
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
                pay_status = "underpaid"

            #overpaid additional statement, no one overpaid
            elif customer_paid > customer_expected:
                pay_status = "overpaid"
                difference = abs(difference)
                
            print(f"{customer_first_name} has {pay_status} for their melons by ${difference}.")

    #close file    
    payment_data.close()

print_payment_status("customer-orders.txt")