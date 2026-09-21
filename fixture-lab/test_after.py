import pytest

from bank import BankAccount


@pytest.fixture
def bank_account():
    return BankAccount(100)


def test_deposit(bank_account):
    bank_account.deposit(50)

    assert bank_account.balance == 150


def test_withdraw(bank_account):
    bank_account.withdraw(30)

    assert bank_account.balance == 70