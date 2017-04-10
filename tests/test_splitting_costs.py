from decimal import Decimal as D

import pytest

from money_owed import split_costs


def test_splitting_costs_two_housemates_no_costs():
    housemates = ['Pete', 'Sumby']

    assert split_costs(housemates, []) is None


@pytest.mark.xfail
def test_splitting_costs_two_housemates_one_bill():
    housemates = ['Pete', 'Sumby']
    costs = [
        {
            'housemate': 'Pete',
            'cost': D('103.00'),
            'description': 'Council Tax'
        }
    ]

    transactions = [
        {
            'from': 'Sumby',
            'to': 'Pete',
            'amount': D('51.50')
        }
    ]
    assert split_costs(housemates, costs) == transactions


@pytest.mark.xfail
def test_splitting_costs_two_housemates_two_bills():
    housemates = ['Pete', 'Sumby']
    costs = [
        {
            'housemate': 'Pete',
            'cost': D('103.00'),
            'description': 'Council Tax'
        },
        {
            'housemate': 'Sumby',
            'cost': D('12.50'),
            'description': 'Thames Water'
        }
    ]

    transactions = [
        {
            'from': 'Sumby',
            'to': 'Pete',
            'amount': D('45.25')
        }
    ]
    assert split_costs(housemates, costs) == transactions


@pytest.mark.xfail
def test_splitting_costs_two_housemates_multiple_bills():
    housemates = ['Pete', 'Sumby']
    costs = [
        {
            'housemate': 'Pete',
            'cost': D('103.00'),
            'description': 'Council Tax'
        },
        {
            'housemate': 'Sumby',
            'cost': D('12.50'),
            'description': 'Thames Water'
        },
        {
            'housemate': 'Sumby',
            'cost': D('30.40'),
            'description': 'EDF'
        },
        {
            'housemate': 'Sumby',
            'cost': D('6.00'),
            'description': 'Netflix'
        },
        {
            'housemate': 'Pete',
            'cost': D('10.00'),
            'description': 'Spotify'
        }
    ]

    transactions = [
        {
            'from': 'Sumby',
            'to': 'Pete',
            'amount': D('56.50')
        }
    ]
    assert split_costs(housemates, costs) == transactions


@pytest.mark.xfail
def test_splitting_costs_rounding_behaviour():
    housemates = ['Pete', 'Sumby']
    costs = [
        {
            'housemate': 'Pete',
            'cost': D('9.99'),
            'description': 'Spotify'
        },
    ]

    transactions = [
        {
            'from': 'Sumby',
            'to': 'Pete',
            'amount': D('5.00')
        }
    ]
    assert split_costs(housemates, costs) == transactions


@pytest.mark.xfail
def test_splitting_costs_three_housemates_one_bill():
    housemates = ['Pete', 'Sumby', 'Alison']
    costs = [
        {
            'housemate': 'Pete',
            'cost': D('105.00'),
            'description': 'Council Tax'
        }
    ]

    transactions = [
        {
            'from': 'Sumby',
            'to': 'Pete',
            'amount': D('35.00')
        },
        {
            'from': 'Alison',
            'to': 'Pete',
            'amount': D('35.00')
        }
    ]
    assert split_costs(housemates, costs) == transactions


@pytest.mark.xfail
def test_splitting_costs_three_housemates_multiple_bills():
    housemates = ['Pete', 'Sumby', 'Alison']
    costs = [
        {
            'housemate': 'Pete',
            'cost': D('103.00'),
            'description': 'Council Tax'
        },
        {
            'housemate': 'Alison',
            'cost': D('52.00'),
            'description': 'Virgin Media'
        },
        {
            'housemate': 'Sumby',
            'cost': D('12.50'),
            'description': 'Thames Water'
        },
        {
            'housemate': 'Sumby',
            'cost': D('30.40'),
            'description': 'EDF'
        },
        {
            'housemate': 'Sumby',
            'cost': D('6.00'),
            'description': 'Netflix'
        },
        {
            'housemate': 'Pete',
            'cost': D('10.00'),
            'description': 'Spotify'
        }
    ]

    transactions = [
        {
            'from': 'Sumby',
            'to': 'Pete',
            'amount': D('22.40')
        },
        {
            'from': 'Alison',
            'to': 'Pete',
            'amount': D('19.30')
        }
    ]
    assert split_costs(housemates, costs) == transactions
