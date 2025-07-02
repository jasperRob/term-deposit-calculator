import pytest
from term_deposit_calculator import calculate_final_balance


def test_monthly_case():
    assert calculate_final_balance(10000, 1.1, "3y", "MONTHLY") == 10335


def test_quarterly_case():
    assert calculate_final_balance(10000, 1.1, "3y", "QUARTERLY") == 10335


def test_annually_case():
    assert calculate_final_balance(10000, 1.1, "3y", "ANNUALLY") == 10334


def test_at_maturity_case():
    assert calculate_final_balance(10000, 1.1, "3y", "AT_MATURITY") == 10330
