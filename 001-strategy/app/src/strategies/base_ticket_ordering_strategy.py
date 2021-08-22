from abc import ABC, abstractmethod
from typing import List
from ..support_ticket import SupportTicket

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass