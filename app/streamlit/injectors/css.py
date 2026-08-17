import streamlit as st


from app.streamlit.contracts.injector import ResourceInjector
from app.streamlit.infra.settings.base import AppAssets


class CSSInjector(ResourceInjector):

    resource_type = AppAssets.CSS

    def __init__(self):
        super().__init__()

    def inject(self, content: str) -> None:
        html = f"""
            <style>
                {content}
            </style>
        """
        return st.html(body=html)
