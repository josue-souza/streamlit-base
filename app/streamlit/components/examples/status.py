import streamlit as st


from app.streamlit.contracts.component import ComponentBase
from app.streamlit.infra.repositories.status_message import StatusMessageRepo


class StatusComponent(ComponentBase):

    def __init__(self):
        super().__init__()

    @classmethod
    def success(
        cls, 
        message: StatusMessageRepo | str = StatusMessageRepo.SUCCESS
        ):
        st.success(body=message)

    @classmethod
    def warning(
        cls, 
        message: StatusMessageRepo | str = StatusMessageRepo.WARNING
        ):
        st.warning(body=message)

    @classmethod
    def error(
        cls, 
        message: StatusMessageRepo | str = StatusMessageRepo.ERROR
        ):
        st.error(body=message)

    def render(self):
        super().render()