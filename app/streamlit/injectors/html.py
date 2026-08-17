import streamlit as st


from app.streamlit.contracts.injector import ResourceInjector
from app.streamlit.infra.settings.base import AppAssets


class HTMLInjector(ResourceInjector):

    resource_type = AppAssets.HTML

    def __init__(self):
        super().__init__()

    def inject(self, content: str) -> None:
        html = f"""
            {content}
        """
        return st.html(body=html)
