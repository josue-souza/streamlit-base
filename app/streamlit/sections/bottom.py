import streamlit as st


from datetime import datetime


from app.streamlit.contracts.section import SectionBase
from app.streamlit.injectors.injectables import Injectables


class Bottom(SectionBase):

    def __init__(self):
        super().__init__(Injectables())
    
    def render(self):
        with st.bottom:
            """
            Global content for bottom here!
            """
            st.caption(
                f'StreamlitBase - Josué Souza - {datetime.now().year}', 
                text_alignment='center'
                )
        return
