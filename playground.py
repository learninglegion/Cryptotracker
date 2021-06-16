ledger_entry = {}
money_spent = float(input("First, how much money did you spend on this crypto purchase?"))
def get_money_spent(m_spent):
    print("${:.2f}".format(m_spent)) # string output
    ledger_entry['money_spent'] = m_spent

get_money_spent(money_spent)