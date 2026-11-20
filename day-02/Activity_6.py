def amount_due(facility_code, hours):
    """Determine hourly rate and calculate amount due BEFORE VAT."""
    if facility_code == "squa":
        rate = 13.00
    elif facility_code == "swim":
        rate = 12.00
    elif facility_code == "gym":
        rate = 11.00
    elif facility_code == "wei":
        rate = 8.00

    amount = rate * hours
    return amount

def final_amount_due(amount):
    """Add 14% VAT and return final amount payable."""
    final_amount = amount * 1.14
    return final_amount

def display(name, final_amount):
    """Display name and final amount with R and two decimals."""
    print(f"Customer name: {name}")
    print(f"Amount payable: R{final_amount:.2f}")

def process_payment():
    """Prompt user, call other functions, display result."""
    name = input("Enter customer's name: ")
    facility_code = input("Enter facility code (squa/swim/gym/wei): ")
    hours = float(input("Enter number of hours: "))

    amount = amount_due(facility_code, hours)
    final_amount = final_amount_due(amount)
    display(name, final_amount)

# Start the program
process_payment()