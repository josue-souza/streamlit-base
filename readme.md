# StreamlitBase

Base pessoal para desenvolvimento de aplicações com Streamlit.

O objetivo deste projeto é fornecer uma estrutura inicial reutilizável para novos projetos Streamlit, centralizando decisões arquiteturais, organização de arquivos e recursos que são utilizados de forma recorrente.

A ideia é evitar reconstruir a mesma estrutura a cada novo projeto e manter uma forma consistente de trabalhar com Streamlit.

## Estrutura

```text
.
├── app
│   └── streamlit
│       ├── assets
│       │   ├── css
│       │   │   └── example.css
│       │   ├── html
│       │   │   └── example.html
│       │   ├── javascript
│       │   │   └── example.js
│       │   └── logo
│       │       ├── icon_image.png
│       │       └── image.png
│       ├── components
│       │   └── examples
│       │       ├── pagination.py
│       │       └── status.py
│       ├── contracts
│       │   ├── component.py
│       │   ├── injector.py
│       │   ├── page.py
│       │   └── section.py
│       ├── home.py
│       ├── infra
│       │   ├── repositories
│       │   │   └── status_message.py
│       │   ├── resources
│       │   │   ├── css.py
│       │   │   ├── html.py
│       │   │   └── javascript.py
│       │   └── settings
│       │       └── base.py
│       ├── __init__.py
│       ├── injectors
│       │   ├── css.py
│       │   ├── html.py
│       │   ├── injectables.py
│       │   └── javascript.py
│       ├── pages
│       │   └── example.py
│       └── sections
│           ├── bottom.py
│           ├── content.py
│           └── sidebar.py
├── docker
│   └── Dockerfile
├── readme.md
├── requirements.txt
└── scripts
    ├── init.sh
    ├── run.sh
    └── setup.sh
```

### Contracts

O diretório `contracts` concentra os contratos utilizados pela aplicação.

Os principais contratos são:

- `PageBase`: define a estrutura das páginas;
- `ComponentBase`: define o contrato dos componentes;
- `InjectorBase`: define o contrato dos injetores;
- `SectionBase`: define o contrato das seções.

Os contratos são utilizados como base para as implementações concretas da aplicação.

### Pages

O diretório `pages` utiliza o mecanismo de aplicações multipágina do Streamlit.

Cada arquivo `.py` dentro desse diretório representa uma página que será disponibilizada na navegação da aplicação.

As páginas devem implementar o contrato definido por `PageBase`.

### Sections

As páginas são divididas em três seções:

- `sidebar`;
- `content`;
- `bottom`.

Cada seção possui sua própria implementação no diretório `sections`.

Essa separação permite estabelecer uma estrutura comum para as páginas da aplicação e centralizar comportamentos que devem ser compartilhados entre elas.

### Components

O diretório `components` é responsável por organizar os componentes customizados da aplicação.

Os componentes devem seguir o contrato definido em `contracts/component.py`, permitindo que sejam implementados de forma padronizada e reutilizados entre diferentes páginas.

Exemplos de componentes podem ser encontrados em:

```text
app/streamlit/components/examples
```

### Injectors

O diretório `injectors` concentra os mecanismos responsáveis pela injeção de recursos externos na aplicação.

Atualmente são disponibilizados injetores para:

- CSS;
- HTML;
- JavaScript.

Os injetores utilizam o método `html()` do Streamlit para carregar e inserir os respectivos recursos na aplicação.

A classe `Injectables` centraliza os diferentes injetores e realiza sua composição com `PageBase`, disponibilizando-os para as páginas que necessitarem desses recursos.

### Assets

O diretório `assets` concentra os recursos estáticos utilizados pela aplicação.

```text
assets/
├── css/
├── html/
├── javascript/
└── logo/
```

### Infra

O diretório `infra` concentra recursos relacionados à infraestrutura da aplicação.

Atualmente, sua estrutura contempla:

- `repositories`: repositórios responsáveis pelo acesso e persistência de dados;
- `resources`: recursos utilizados pelos injetores;
- `settings`: configurações da aplicação.

## Criando uma nova página

Para criar uma nova página, basta implementar `PageBase`.

Exemplo:

```python
import streamlit as st

from app.streamlit.contracts.page import PageBase


class PageExample(PageBase):

    def __init__(self):
        st.set_page_config(layout="wide")
        super().__init__()

    def sidebar(self, *args, **kwargs):
        super().sidebar(*args, **kwargs)
        return

    def content(self, *args, **kwargs):
        super().content(*args, **kwargs)

        # Implementação específica da página
        st.write("Minha página")

        return

    def bottom(self, *args, **kwargs):
        super().bottom(*args, **kwargs)
        return

    def main(self, *args, **kwargs):
        super().main(*args, **kwargs)
        return


if __name__ == "__main__":
    PageExample().main()
```

## Inicialização do projeto

O StreamlitBase possui scripts para facilitar a preparação e execução do projeto.

### Inicialização do Git

O script `init.sh` permite remover o repositório Git existente e inicializar um novo repositório para o projeto.

```bash
./scripts/init.sh
```

### Configuração do ambiente

O script `setup.sh` cria o ambiente virtual Python, ativa a virtualenv e instala as dependências definidas em `requirements.txt`.

```bash
./scripts/setup.sh
```

### Executando a aplicação

Após configurar o ambiente, a aplicação pode ser iniciada através do script `run.sh`.

```bash
./scripts/run.sh
```

## Configuração do Streamlit

As configurações específicas do Streamlit ficam no diretório `.streamlit`.

O arquivo `config.toml` centraliza as configurações utilizadas pelo framework.

A documentação oficial das configurações está disponível em:

[Streamlit Configuration](https://docs.streamlit.io/develop/api-reference/configuration/config.toml)

### JavaScript Injection — Considerações

O `JavaScriptInjector` possui uma responsabilidade limitada: ler o conteúdo de um arquivo JavaScript e injetá-lo na página.

O injector não gerencia o lifecycle ou o estado do JavaScript executado.

Como o Streamlit pode reconstruir partes do DOM durante reruns e navegação entre páginas, scripts injetados devem considerar que elementos podem ser criados, removidos ou substituídos.

Ao criar scripts para injeção, recomenda-se:

- tornar a inicialização idempotente;
- verificar se os elementos necessários existem antes de utilizá-los;
- evitar o registro repetido de event listeners;
- não assumir que referências a elementos do DOM permanecerão válidas indefinidamente;
- utilizar `MutationObserver` ou event delegation quando o comportamento precisar acompanhar elementos reconstruídos;
- não utilizar variáveis JavaScript locais como mecanismo de persistência de estado da aplicação.

O `JavaScriptInjector` não modifica, encapsula ou gerencia o código JavaScript fornecido pelo usuário.

A responsabilidade por compatibilidade com o lifecycle do DOM é do script injetado.

## Requisitos

- Python
- Streamlit

As dependências Python utilizadas pelo projeto estão definidas em `requirements.txt`.