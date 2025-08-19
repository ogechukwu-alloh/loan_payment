import pandas as pd

def periodic_payment(principal, annual_rate, num_of_years, compounding_frequency):
    num_of_payments = num_of_years * compounding_frequency
    rate_per_period = (annual_rate / 100.0) / compounding_frequency

    if rate_per_period == 0:
        return principal / num_of_payments

    growth_factor = (1 + rate_per_period) ** num_of_payments
    payment = principal * rate_per_period * growth_factor / (growth_factor - 1)
    return payment

def amortization_schedule(principal, annual_rate, num_of_years, compounding_frequency):
    num_of_payments = num_of_years * compounding_frequency
    payment = periodic_payment(principal, annual_rate, num_of_years, compounding_frequency)
    rate_per_period = (annual_rate / 100) / compounding_frequency

    schedule = []
    balance_to_pay = float(principal)

    for n in range(1, num_of_payments + 1):
        interest = balance_to_pay * rate_per_period
        principal_payment = payment - interest
        balance_to_pay = balance_to_pay - principal_payment
        balance_to_pay = max(balance_to_pay, 0)

        schedule.append({
            "Period": n,
            "Payment": round(payment, 2),
            "Interest": round(interest, 2),
            "Principal": round(principal_payment, 2),
            "Balance": round(balance_to_pay, 2)
        })

    return schedule


print("Choose a compounding frequency:")
print("1 - Annual")
print("2 - Semi-Annual")
print("4 - Quarterly")
print("12 - Monthly")

freq_map = {
    "monthly" : 12,
    "quarterly" : 4,
    "semi-annual" : 2,
    "yearly" : 1
}

try:
    freq_input = input("Enter a compounding frequency (monthly, quarterly, semi-annually, yearly): ").strip().lower()
    if freq_input not in freq_map:
        print("Invalid choice. Please enter monthly, quarterly, semi-annually, yearly: ")
        exit()
    compounding_frequency = freq_map[freq_input]

except Exception as e:
    print("Error", e)
    exit()

try:
    principal = float(input("Enter the loan amount: "))
except ValueError:
    print("Please enter only a numeric value.")
    exit()

try:
    annual_rate = float(input("Enter the annual interest rate in percentage: "))
except ValueError:
    print("Please enter only a numeric value.")
    exit()

try:
    num_of_years = int(input("Enter the loan repayment time (in years): "))
except ValueError:
    print("Please enter only a numeric value.")
    exit()

payment = periodic_payment(principal,annual_rate, num_of_years, compounding_frequency)
schedule = amortization_schedule(principal, annual_rate, num_of_years, compounding_frequency)

total_to_pay = payment * num_of_years * compounding_frequency # this is the principal plus interest
total_interest = total_to_pay - principal

print(f"Periodic payment: {payment: .2f}")
print(f"Total to pay over {num_of_years * compounding_frequency} installments: {total_to_pay:.2f}")
print(f"Total interest: {total_interest: .2f}")

print(schedule)



