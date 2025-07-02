#!/usr/bin/env python3
import argparse
import re
import sys


def get_duration_in_years(term_duration: str) -> float:
    match = re.fullmatch(r"(?:(\d+)y)?(?:(\d+)m)?", term_duration.strip())
    if not match:
        raise ValueError(f"Invalid duration: {term_duration}")

    if match.group(1):
        years = int(match.group(1))
    else:
        years = 0

    if match.group(2):
        months = int(match.group(2))
    else:
        months = 0

    if years <= 0 and months <= 0:
        raise ValueError(f"Invalid duration: {term_duration}")

    return years + (months / 12)


def calculate_final_balance(
    deposit_amount: int,
    interest_rate: float,
    term_duration: str,
    interest_payment_term: str,
) -> int:
    if deposit_amount <= 0:
        raise ValueError("value of 'deposit_amount' must be a positive number")
    if interest_rate <= 0:
        raise ValueError("value of 'interest_rate' must be a positive number")

    term_in_years = get_duration_in_years(term_duration)
    if interest_payment_term == "MONTHLY":
        num_compounding_periods = 12
    elif interest_payment_term == "QUARTERLY":
        if term_in_years < 0.25:
            raise ValueError(
                "'QUARTERLY' payment term cannot be used with term duration less than 3 months"
            )
        num_compounding_periods = 4
    elif interest_payment_term == "ANNUALLY":
        if term_in_years < 1:
            raise ValueError(
                "'ANNUALLY' payment term cannot be used with term duration less than 1 year"
            )
        num_compounding_periods = 1
    elif interest_payment_term == "AT_MATURITY":
        # Simply add interest accumulated over entire investment term
        return round(
            deposit_amount + (deposit_amount * (interest_rate / 100) * term_in_years)
        )
    else:
        raise ValueError(f"'{interest_payment_term}' is not a valid PaymentTerm value")

    # Compound Interest Formula: Future Value (FV) = PV [1 + (r ÷ n)] ^ (n × t)
    final_balance = deposit_amount * (
        (1 + ((interest_rate / 100.0) / num_compounding_periods))
        ** (num_compounding_periods * term_in_years)
    )
    # Balance rounded to nearest dollar
    return round(final_balance)


def main():
    parser = argparse.ArgumentParser(
        prog="Term Deposit Calculator",
        description="Used to calculate the return on a term deposit",
    )
    parser.add_argument(
        "-d",
        type=int,
        help="The deposit amount, Example: -d 10000",
        required=True,
    )
    parser.add_argument(
        "-i",
        help="The interest rate, Example: -i 1.1",
        type=float,
        required=True,
    )
    parser.add_argument(
        "-t",
        type=str,
        help="The investment term, Example: -t 1y6m | 3y | 7m",
        required=True,
    )
    parser.add_argument(
        "-p",
        type=str,
        help="The interest payment term, Example: -p MONTHLY | QUARTERLY | ANNUALLY | AT_MATURITY",
        required=True,
    )
    args = parser.parse_args()
    try:
        balance = calculate_final_balance(args.d, args.i, args.t, args.p)
        print(f"Final Balance: {balance}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
