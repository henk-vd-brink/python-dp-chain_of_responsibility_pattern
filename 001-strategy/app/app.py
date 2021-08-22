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
    app = CustomerSupport(RandomOrderingStrategy())

    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    app.process_tickets()