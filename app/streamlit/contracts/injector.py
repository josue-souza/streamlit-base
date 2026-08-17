from abc import ABC, abstractmethod
from pathlib import Path


from app.streamlit.infra.settings.base import AppAssets


class InjectorBase(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def inject(self, content: str) -> None:
        pass


class ResourceInjector(InjectorBase):

    resource_type: str

    def load_resource(self, filename: str) -> Path:
        return AppAssets.BASE / self.resource_type / filename

    def inject_file(self, file: str) -> None:
        content = file.read_text()
        self.inject(content)
