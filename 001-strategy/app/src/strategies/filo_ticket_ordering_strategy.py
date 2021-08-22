from .base_ticket_ordering_strategy import TicketOrderingStrategy
from typing import List
from ..support_ticket import SupportTicket

class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy