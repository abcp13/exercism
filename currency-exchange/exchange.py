def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    cambio= budget/exchange_rate
    print(cambio)
    return cambio

   



def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    resta = budget - exchanging_value
    print(resta)
    return resta
 

def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    bills = denomination * number_of_bills
    print(bills)
    return bills
 
 


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    billetes = int(budget/denomination)
    print(billetes)
    return billetes




def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    cambio = budget % denomination
    return cambio
    



def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    
    fee = exchange_rate + (exchange_rate * (spread / 100))
    total = exchange_money(budget,fee)

    money_in_bills = int(total / denomination)
    maximum = money_in_bills * denomination
    return maximum
    pass
    """
    new_rate = exchange_rate + (exchange_rate * (spread / 100)) 
    total_new_currency = exchange_money(budget, new_rate)
    bill_value_new_currency = int(total_new_currency / denomination)
    maximun_value_new_currency = bill_value_new_currency * denomination
    return maximun_value_new_currency


