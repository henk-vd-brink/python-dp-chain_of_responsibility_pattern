from .base_ticket_ordering_strategy import TicketOrderingStrategy
from typing import List
from ..support_ticket import SupportTicket

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()