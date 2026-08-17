import streamlit as st

from typing import Literal

from app.streamlit.contracts.component import ComponentBase


class PaginationComponent(ComponentBase):

    @classmethod
    def render(
        cls,
        iterable: list,
        key: str = "pagination",
        box_height: int | Literal["stretch", "content"] = "content",
    ):
        if not iterable:
            return

        cls._initialize_state(key)

        left_pag, center_pag, right_pag = st.columns(3)

        with center_pag:
            with st.container(border=True):

                top_buttons = cls._render_navigation(
                    key=key,
                    position="top",
                )

                cls._render_content(
                    iterable=iterable,
                    key=key,
                    box_height=box_height,
                )

                bottom_buttons = cls._render_navigation(
                    key=key,
                    position="bottom",
                )

                cls._handle_navigation(
                    key=key,
                    max_items=len(iterable),
                    top_buttons=top_buttons,
                    bottom_buttons=bottom_buttons,
                )

    @staticmethod
    def _initialize_state(key: str):
        if key not in st.session_state:
            st.session_state[key] = 0

    @staticmethod
    def _render_navigation(
        key: str,
        position: str,
    ):
        with st.container(horizontal=True):
            previous_btn = st.button(
                "Previous",
                key=f"{key}_{position}_previous",
                width="stretch",
                type='secondary'
            )

            st.space("stretch")

            next_btn = st.button(
                "Next",
                key=f"{key}_{position}_next",
                width="stretch",
                type='secondary'
            )

        return previous_btn, next_btn

    @staticmethod
    def _render_content(
        iterable: list,
        key: str,
        box_height: int | Literal["stretch", "content"],
    ):
        with st.container(height=box_height, border=False):
            iterable[st.session_state[key]]()

    @staticmethod
    def _handle_navigation(
        key: str,
        max_items: int,
        top_buttons: tuple,
        bottom_buttons: tuple,
    ):
        top_previous, top_next = top_buttons
        bottom_previous, bottom_next = bottom_buttons

        next_clicked = top_next or bottom_next
        previous_clicked = top_previous or bottom_previous

        max_idx = max_items - 1

        if next_clicked:
            if st.session_state[key] < max_idx:
                st.session_state[key] += 1
            else:
                st.session_state[key] = 0

        if previous_clicked:
            if st.session_state[key] > 0:
                st.session_state[key] -= 1
            else:
                st.session_state[key] = max_idx