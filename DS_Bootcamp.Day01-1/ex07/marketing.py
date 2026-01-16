import sys

def not_seen_promo(clients, participans, recipients):
    return (clients|participans)-recipients

def not_clients(clients, participans, recipients):
    return participans - recipients-clients

def not_participants(clients, participans, recipients):
    return (clients|recipients)-participans

def func():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    clients_set=set(clients)
    participants_set=set(participants)
    recipients_set=set(recipients)

    task=sys.argv[1]

    if task == 'call_center':
        print(not_seen_promo(clients_set, participants_set, recipients_set))
    elif task == 'potential_clients':
        print(not_clients(clients_set, participants_set, recipients_set))
    elif task == 'loyalty_program':
        print(not_participants(clients_set, participants_set, recipients_set))
    else:
        raise ValueError("Invalid task name. Please use 'call_center', 'potential_clients', or 'loyalty_program'.")

if __name__ == '__main__':
    func()