import math

class LoanCalculator:
    def __init__(self, payment_type=None, principal=None, payment=None, periods=None, interest=None):
        self.payment_type = payment_type
        self.principal = principal
        self.payment = payment
        self.periods = periods
        self.interest = interest

    def calculate_periods(self):
        i = self.interest / (12 * 100)
        periods = math.log(self.payment / (self.payment - i * self.principal), 1 + i)
        return math.ceil(periods)

    def calculate_payment(self):
        i = self.interest / (12 * 100)
        payment = self.principal * (i * (1 + i) ** self.periods) / ((1 + i) ** self.periods - 1)
        return math.ceil(payment)

    def calculate_principal(self):
        i = self.interest / (12 * 100)
        principal = self.payment / ((i * (1 + i) ** self.periods) / ((1 + i) ** self.periods - 1))
        return round(principal)

    def convert_months_to_years_and_months(self, months):
        years = months // 12
        months_remaining = months % 12

        if years == 0:
            return f"{months_remaining} months"
        elif months_remaining == 0:
            return f"{years} year" if years == 1 else f"{years} years"
        else:
            return f"{years} years and {months_remaining} months"

    def calculate_annuity(self):
        i = self.interest / (12 * 100)
        annuity_payment = self.principal * (i * (1 + i) ** self.periods) / ((1 + i) ** self.periods - 1)
        total_payment = math.ceil(annuity_payment) * self.periods
        overpayment = total_payment - self.principal
        return math.ceil(annuity_payment), overpayment

    def calculate_differentiated(self):
        i = self.interest / (12 * 100)
        total_payment = 0
        for month in range(1, self.periods + 1):
            diff_payment = (self.principal / self.periods) + i * (self.principal - ((self.principal * (month - 1)) / self.periods))
            total_payment += math.ceil(diff_payment)
            print(f"Month {month}: payment is {math.ceil(diff_payment)}")

        over_payment = total_payment - self.principal
        print(f"\nOverpayment = {int(over_payment)}")

    def calculate_loan(self):
        if self.payment_type == "diff":
            if self.principal is not None and self.periods is not None and self.interest is not None:
                self.calculate_differentiated()
            else:
                print("Incorrect parameters.")
        elif self.payment_type == "annuity":
            if self.principal is not None and self.periods is not None and self.interest is not None:
                annuity_payment, overpayment = self.calculate_annuity()
                print(f"\nYour annuity payment = {annuity_payment}!")
                print(f"Overpayment = {int(overpayment)}")
            elif self.payment is not None and self.periods is not None and self.interest is not None:
                principal = self.calculate_principal()
                print(f"Your loan principal = {math.ceil(principal)}!")
            elif self.principal is not None and self.payment is not None and self.interest is not None:
                months = self.calculate_periods()
                formatted_duration = self.convert_months_to_years_and_months(months)
                overpayment = self.payment * months - self.principal
                print(f"It will take {formatted_duration} to repay this loan!")
                print(f"Overpayment = {int(overpayment)}")
            else:
                print("Incorrect parameters.")
        else:
            print("Incorrect parameters")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Loan calculator")
    parser.add_argument("--type", type=str, help="Type of payment (annuity or diff)")
    parser.add_argument("--payment", type=float, help="The annuity payment amount")
    parser.add_argument("--principal", type=float, help="The loan principal amount")
    parser.add_argument("--periods", type=int, help="The number of periods needed to repay the loan")
    parser.add_argument("--interest", type=float, help="The loan interest rate")

    args = parser.parse_args()

    if any(arg is not None and arg < 0 for arg in [args.payment, args.principal, args.periods, args.interest]):
        print("Incorrect parameters. Please provide non-negative values.")
        return

    calculator = LoanCalculator(args.type, args.principal, args.payment, args.periods, args.interest)
    print(calculator.calculate_loan())

if __name__ == "__main__":
    main()