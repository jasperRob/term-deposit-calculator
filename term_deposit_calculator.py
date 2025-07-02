#!/usr/bin/env python3
import argparse
import sys


def calculate_final_balance(
    deposit_amount: int,
    interest_rate: float,
    term_duration: str,
    interest_payment_term: str,
) -> int:
    return 0


def main():
    parser = argparse.ArgumentParser(
        prog="Term Deposit Calculator",
        description="Used to calculate the return on a term deposit",
    )
    parser.add_argument(
        "-d",
        type=int,
        help="The deposit amount",
        required=True,
    )
    parser.add_argument(
        "-i",
        help="The interest rate",
        type=float,
        required=True,
    )
    parser.add_argument(
        "-t",
        type=str,
        help="The investment term",
        required=True,
    )
    parser.add_argument(
        "-p",
        type=str,
        help="The interest payment term",
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
