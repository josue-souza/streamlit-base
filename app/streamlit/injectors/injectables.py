from app.streamlit.injectors.html import HTMLInjector
from app.streamlit.injectors.css import CSSInjector
from app.streamlit.injectors.javascript import JavaScriptInjector


class Injectables:

    def __init__(self):
        self.html = HTMLInjector()
        self.css = CSSInjector()
        self.js = JavaScriptInjector()
