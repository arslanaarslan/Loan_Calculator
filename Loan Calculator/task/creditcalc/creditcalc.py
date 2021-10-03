import math
import argparse


def interest_rate_calculation(i):
    return i / (12 * 100)


def periods_calculation(a, i, p):
    return math.ceil(math.log(a / (a - i * p), (1 + i)))


def payment_calculation(p, i, n):
    return math.ceil(p * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))


def payment_diff_calculation(p, i, n, m):
    return math.ceil((p / n) + (i * (p - (p * (m - 1) / n))))


def principal_calculation(a, i, n):
    return math.floor(a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))


parser = argparse.ArgumentParser(description="This programs calculate payments \\ "
                                             "Please provide information correctly.")

parser.add_argument("--type", choices=["annuity", "diff"], help="Incorrect parameters")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

selection = args.type

principal = 0
payment = 0
periods = 0
interest = 0

if args.principal is not None:
    principal = float(args.principal)

if args.payment is not None:
    payment = float(args.payment)

if args.periods is not None:
    periods = int(args.periods)

last_payment = 0

interest = 0

if args.interest is not None:
    interest = float(args.interest)

interest_rate = interest_rate_calculation(interest)

total = 0

if selection == "diff":
    if (principal <= 0 or principal is None
            or periods <= 0 or periods is None
            or interest <= 0 or interest is None):
        print("Incorrect parameters")
    else:
        for month in range(1, periods + 1):
            result = payment_diff_calculation(principal, interest_rate, periods, month)
            total += result
            print(f"Month {month}: payment is {result}")

        print()
        print(f"Overpayment = {round(total - principal)}")

elif selection == "annuity":
    if principal < 0 or principal is None \
            or periods < 0 or periods is None \
            or interest < 0 or interest is None \
            or principal < 0 or principal is None:
        print("Incorrect parameters")
    else:
        if periods > 0 and principal > 0:
            result = payment_calculation(principal, interest_rate, periods)
            print(f"Your annuity payment = {result}!")
            print(f"Overpayment = {round(result * periods - principal)}")
        elif periods > 0 and payment > 0:
            result = principal_calculation(payment, interest_rate, periods)
            print(f"Your loan principal = {result}!")
            print(f"Overpayment = {round(payment * periods - result)}")
        elif principal > 0 and payment > 0 and interest > 0:
            periods = periods_calculation(payment, interest_rate, principal)

            amount_of_years = math.floor(periods / 12)
            amount_of_months = periods - amount_of_years * 12

            if amount_of_years > 0 and amount_of_months > 0:
                if amount_of_years == 1 and amount_of_months == 1:
                    print(f"It will take {amount_of_years} year and {amount_of_months} month to repay the loan!")
                elif amount_of_years == 1:
                    print(f"It will take {amount_of_years} year and {amount_of_months} months to repay the loan!")
                elif amount_of_months == 1:
                    print(f"It will take {amount_of_years} years and {amount_of_months} month to repay the loan!")
                else:
                    print(f"It will take {amount_of_years} years and {amount_of_months} months to repay the loan!")

            elif amount_of_years > 0 and amount_of_months == 0:
                if amount_of_years > 1:
                    print(f"It will take {amount_of_years} years to repay the loan!")
                else:
                    print(f"It will take {amount_of_years} year to repay the loan!")
            else:
                if amount_of_months > 1:
                    print(f"It will take {amount_of_months} months to repay the loan!")
                else:
                    print(f"It will take {amount_of_months} month to repay the loan!")

            print(f"Overpayment = {round(payment * (amount_of_years * 12 + amount_of_months) - principal)}")
        else:
            print("Incorrect parameters")
else:
    print("Incorrect parameters")
