import pytest
from term_deposit_calculator import calculate_final_balance

# Most of these test cases were confirmed using the
# Bendigo Bank Term Deposit Calculator:
# https://www.bendigobank.com.au/calculators/deposit-and-savings/


def test_monthly_cases():
    # Testing various uses of the MONTHLY payment term
    assert calculate_final_balance(10000, 1.1, "3y", "MONTHLY") == 10335
    assert calculate_final_balance(50000, 2.5, "4y", "MONTHLY") == 55253
    assert calculate_final_balance(250000, 5, "5y", "MONTHLY") == 320840

    assert calculate_final_balance(100000, 1.1, "3m", "MONTHLY") == 100275
    assert calculate_final_balance(100000, 1.1, "8m", "MONTHLY") == 100736
    assert calculate_final_balance(100000, 1.1, "2y3m", "MONTHLY") == 102505


def test_quarterly_cases():
    # Testing various uses of the QUARTERLY payment term
    assert calculate_final_balance(10000, 1.1, "3y", "QUARTERLY") == 10335
    assert calculate_final_balance(50000, 2.5, "4y", "QUARTERLY") == 55241
    assert calculate_final_balance(250000, 5, "5y", "QUARTERLY") == 320509

    assert calculate_final_balance(100000, 1.1, "3m", "QUARTERLY") == 100275
    assert calculate_final_balance(100000, 1.1, "8m", "QUARTERLY") == 100735
    assert calculate_final_balance(100000, 1.1, "2y3m", "QUARTERLY") == 102502


def test_annually_cases():
    # Testing various uses of the ANNUALLY payment term
    assert calculate_final_balance(10000, 1.1, "3y", "ANNUALLY") == 10334
    assert calculate_final_balance(50000, 2.5, "4y", "ANNUALLY") == 55191
    assert calculate_final_balance(250000, 5, "5y", "ANNUALLY") == 319070
    assert calculate_final_balance(100000, 1.1, "2y3m", "ANNUALLY") == 102492


def test_at_maturity_cases():
    # Testing various uses of the AT_MATURITY payment term
    assert calculate_final_balance(10000, 1.1, "3y", "AT_MATURITY") == 10330
    assert calculate_final_balance(50000, 2.5, "4y", "AT_MATURITY") == 55000
    assert calculate_final_balance(250000, 5, "5y", "AT_MATURITY") == 312500
    assert calculate_final_balance(100000, 1.1, "2y3m", "AT_MATURITY") == 102475


def test_negative_and_zero_value_cases():
    # Ensure that negative and zero inputs result in an error
    with pytest.raises(ValueError):
        calculate_final_balance(-10000, 1.1, "3y", "AT_MATURITY")
    with pytest.raises(ValueError):
        calculate_final_balance(10000, -1.1, "3y", "AT_MATURITY")
    with pytest.raises(ValueError):
        calculate_final_balance(10000, 1.1, "-3y", "AT_MATURITY")
    with pytest.raises(ValueError):
        calculate_final_balance(0, 1.1, "3y", "AT_MATURITY")
    with pytest.raises(ValueError):
        calculate_final_balance(10000, 0, "3y", "AT_MATURITY")
    with pytest.raises(ValueError):
        calculate_final_balance(10000, 1.1, "0y", "AT_MATURITY")


def test_invalid_quarterly_case():
    # should throw exception if quarterly payment term is passed for less than 3 months duration
    with pytest.raises(ValueError):
        calculate_final_balance(50000, 1.7, "2m", "QUARTERLY")


def test_invalid_annually_case():
    # should throw exception if anually payment term is passed for monthly term duration
    with pytest.raises(ValueError):
        calculate_final_balance(50000, 1.7, "5m", "ANNUALLY")


def test_invalid_payment_term():
    # should throw exception if an invalid value is passed to the payment term input
    with pytest.raises(ValueError):
        calculate_final_balance(50000, 1.7, "5m", "THIS_IS_INVALID")
