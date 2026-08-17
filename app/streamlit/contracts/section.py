from abc import ABC, abstractmethod


from app.streamlit.injectors.injectables import Injectables


class SectionBase(ABC):

    def __init__(self, injectables: Injectables | None):
        self.injectables = injectables or Injectables()

    @abstractmethod
    def render(self, *args, **kwargs):
        pass
