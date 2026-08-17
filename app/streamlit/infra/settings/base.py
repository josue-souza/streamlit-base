import os


from dotenv import load_dotenv
from pathlib import Path


load_dotenv()


class AppSecrets:
    pass


class AppStreamlit:
    pass


class AppAssets:
    BASE = Path('app/streamlit/assets')

    HTML = BASE / 'html'
    CSS = BASE / 'css'
    JAVASCRIPT = BASE / 'javascript'

    IMAGE = BASE / 'logo' / 'image.png'
    ICON_IMAGE = BASE / 'logo' / 'icon_image.png'