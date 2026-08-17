import streamlit as st


from app.streamlit.contracts.section import SectionBase
from app.streamlit.infra.settings.base import AppAssets
from app.streamlit.injectors.injectables import Injectables


class Sidebar(SectionBase):

    def __init__(self):
        super().__init__(Injectables())
    
    def render(self):

        self._add_logo()

        with st.sidebar:
            """
            Global content for sidebar here!
            """
            pass
        return

    def _add_logo(self):
        return st.logo(
            image=str(AppAssets.IMAGE),
            link='http://localhost:8501/',
            icon_image=str(AppAssets.ICON_IMAGE),
        )
