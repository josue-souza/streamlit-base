import streamlit as st


from app.streamlit.contracts.injector import ResourceInjector
from app.streamlit.infra.settings.base import AppAssets


class JavaScriptInjector(ResourceInjector):

    resource_type = AppAssets.JAVASCRIPT

    def __init__(self):
        super().__init__()

    def inject(self, content: str) -> None:

        html = f"""
            <script>
                {content}
            </script>
        """

        st.html(
            body=html,
            unsafe_allow_javascript=True,
        )
