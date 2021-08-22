import random
from .base_ticket_ordering_strategy import TicketOrderingStrategy
from typing import List
from ..support_ticket import SupportTicket

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy