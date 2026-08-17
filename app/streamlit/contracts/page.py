import streamlit as st


from abc import ABC, abstractmethod


from app.streamlit.sections.sidebar import Sidebar
from app.streamlit.sections.content import Content
from app.streamlit.sections.bottom import Bottom
from app.streamlit.injectors.injectables import Injectables
from app.streamlit.infra.resources.html import HTMLResource
from app.streamlit.infra.resources.css import CSSResource
from app.streamlit.infra.resources.javascript import JavaScriptResource


class PageBase(ABC):

    def __init__(self, injectables: Injectables | None = None):
        self.injectables = injectables or Injectables()

    @abstractmethod
    def sidebar(self, *args, **kwargs):
        Sidebar().render()
        return

    @abstractmethod
    def content(self, *args, **kwargs):
        Content().render()
        return

    @abstractmethod
    def bottom(self, *args, **kwargs):
        Bottom().render()
        return

    @abstractmethod
    def main(self, *args, **kwargs):
        self._example()
        self.sidebar(*args, **kwargs)
        self.content(*args, **kwargs)
        self.bottom(*args, **kwargs)
        return

    def _example(self):
        self.injectables.html.inject_file(HTMLResource.EXAMPLE)
        self.injectables.css.inject_file(CSSResource.EXAMPLE)
        self.injectables.js.inject_file(JavaScriptResource.EXAMPLE)
