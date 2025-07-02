# term-deposit-calculator

A Term Deposit Calculator CLI Tool built using Python

## Setup

With Python installed on your system, setup a virtual environment for package consistency:

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Execute the `term_deposit_calculator.py` script as an executable with the
following arguments:

- `-d` : deposit amount ($)
- `-i` : interest rate (%)
- `-t` : investment term - format `YyMm`
- `-p` : interest payment term (e.g, `MONTHLY`, `QUARTERLY`, `ANNUALLY`, `AT_MATURITY`)

Example:
Deposit Amount: $10,000
Interest Rate: 1.1%
Investment Term: 3 years
Interest Paid: AT_MATURITY

```sh
./term_deposit_calculator.py -d 10000 -i 1.1 -t 3y -p AT_MATURITY
```

Example:
Deposit Amount: $50,000
Interest Rate: 1.7%
Investment Term: 2 years and 6 months
Interest Paid: MONTHLY

```sh
./term_deposit_calculator.py -d 50000 -i 1.7 -t 2y6m -p MONTHLY
```

## Testing

Testing is performed using the pytest library:

```sh
pytest
```

## Cleanup

When finished using the CLI tool, you can exit the virtual environment by
running the deactivate command:

```sh
deactivate
```
