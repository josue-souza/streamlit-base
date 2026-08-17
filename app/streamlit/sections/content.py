import streamlit as st


from app.streamlit.contracts.section import SectionBase
from app.streamlit.injectors.injectables import Injectables


class Content(SectionBase):

    def __init__(self):
        super().__init__(Injectables())
    
    def render(self):
        """
        Global content for content here!
        """
        return
