import streamlit as st


from app.streamlit.contracts.page import PageBase


class PageHome(PageBase):

    def __init__(self):
        st.set_page_config(layout="wide")
        super().__init__()

    def sidebar(self, *args, **kwargs):
        super().sidebar(*args, **kwargs)
        return

    def content(self, *args, **kwargs):
        super().content(*args, **kwargs)
        return

    def bottom(self, *args, **kwargs):
        super().bottom(*args, **kwargs)
        return

    def main(self, *args, **kwargs):
        super().main(*args, **kwargs)
        return


if __name__ == '__main__':
    PageHome().main()