from abc import ABC, abstractmethod


class BaseBuildChain(ABC):
    def __init__(self, *args, **kwargs):
        self._chain = self._build_chain()

    @abstractmethod
    def _build_chain(self):
        pass

    @property
    def chain(self):
        return self._chain
