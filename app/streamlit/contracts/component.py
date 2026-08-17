from abc import ABC, abstractmethod


from app.streamlit.injectors.injectables import Injectables


class ComponentBase(ABC):

    def __init__(self, injectables: Injectables | None):
        self.injectables = injectables or Injectables()

    @classmethod
    def render(self, *args, **kwargs):
        pass
