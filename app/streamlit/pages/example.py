import streamlit as st


from app.streamlit.contracts.page import PageBase
from app.streamlit.components.examples.status import StatusComponent
from app.streamlit.components.examples.pagination import PaginationComponent

class ExampleTest(PageBase):

    def __init__(self):
        super().__init__()

    def sidebar(self, *args, **kwargs):
        super().sidebar(*args, **kwargs)
        return

    def content(self, *args, **kwargs):
        super().content(*args, **kwargs)
        return

    def bottom(self, *args, **kwargs):
        with st.bottom:
            status = [
                StatusComponent.success,
                StatusComponent.warning,
                StatusComponent.error,
            ]

            PaginationComponent.render(iterable=status,)

        super().bottom(*args, **kwargs)
        return

    def main(self, *args, **kwargs):
        super().main(*args, **kwargs)
        return


if __name__ == '__main__':
    ExampleTest().main()