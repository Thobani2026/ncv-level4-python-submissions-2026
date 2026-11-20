import random

def generate_minutes():
    """Generate and return random minutes between 30 and 180 inclusive."""
    minutes = random.randint(30, 180)
    return minutes

def calc_amount(machine_type, minutes):
    """Calculate amount BEFORE VAT."""
    # Convert minutes to hours - charge fractional hours proportionately
    hours_used = minutes / 60

    if machine_type == "A":
        initial_cost = 50.00
        hourly_rate = 30.00
    elif machine_type == "B":
        initial_cost = 62.50
        hourly_rate = 36.25
    elif machine_type == "C":
        initial_cost = 74.87
        hourly_rate = 40.50

    amount_before_vat = initial_cost + (hourly_rate * hours_used)
    return amount_before_vat

def calc_total_amount(amount):
    """Calculate VAT (14%) and total payable. Return both."""
    vat_amount = amount * 0.14
    total_payable = amount + vat_amount
    return vat_amount, total_payable

def display_summary(payments):
    """Calculate and display daily summary from payments list."""
    num_customers = len(payments)
    total_all = sum(payments)
    average = total_all / num_customers
    highest = max(payments)
    lowest = min(payments)

    print("\n--- DAILY SUMMARY ---")
    print(f"Number of customers processed: {num_customers}")
    print(f"Combined amount payable by all customers: R{total_all:.2f}")
    print(f"Average payment per customer: R{average:.2f}")
    print(f"Highest payment: R{highest:.2f}")
    print(f"Lowest payment: R{lowest:.2f}")

def process_customers():
    """Main function - process all customers."""
    num_customers = int(input("Enter number of customers to process: "))
    payments = []

    for i in range(num_customers):
        print(f"\n--- Customer {i + 1} ---")
        name = input("Enter customer's name: ")
        machine_type = input("Enter machine type (A/B/C): ")

        minutes = generate_minutes()
        amount_before_vat = calc_amount(machine_type, minutes)
        vat_amount, total_payable = calc_total_amount(amount_before_vat)

        payments.append(total_payable)

        # Display invoice
        print("\n--- INVOICE ---")
        print(f"Customer name: {name}")
        print(f"Machine type: {machine_type}")
        print(f"Minutes used: {minutes}")
        print(f"Amount before VAT: R{amount_before_vat:.2f}")
        print(f"VAT amount: R{vat_amount:.2f}")
        print(f"Total payable: R{total_payable:.2f}")

    display_summary(payments)

# Start the program
process_customers()