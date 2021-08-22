from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass
from src import (   FIFOOrderingStrategy, 
                    FILOOrderingStrategy, 
                    RandomOrderingStrategy, 
                    TicketOrderingStrategy,
                    SupportTicket,
                    CustomerSupport)

def run():
    # create the application
    app = CustomerSupport(RandomOrderingStrategy())

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    # process the tickets
    app.process_tickets()