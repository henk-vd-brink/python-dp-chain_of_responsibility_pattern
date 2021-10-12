
from .support_ticket import SupportTicket
from .strategies.base_ticket_ordering_strategy import TicketOrderingStrategy

class CustomerSupport:

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        ticket_list = self.processing_strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print("There are no tickets to process, number of tickets equals zero.")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)
            

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")