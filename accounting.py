melon_cost = 1.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )
