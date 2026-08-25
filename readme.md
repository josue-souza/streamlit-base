# StreamlitBase

Base pessoal para desenvolvimento de aplicações com [Streamlit].

O objetivo deste projeto é fornecer uma estrutura inicial reutilizável para novos projetos Streamlit, centralizando decisões arquiteturais, organização de arquivos e recursos que são utilizados de forma recorrente.

A ideia é evitar reconstruir a mesma estrutura a cada novo projeto e manter uma forma consistente de trabalhar com Streamlit.

---

## Estrutura

```text
.
├── app
│   └── streamlit
│       ├── assets
│       │   ├── css
│       │   │   └── example.css
│       │   ├── html
│       │   │   └── example.html
│       │   ├── javascript
│       │   │   └── example.js
│       │   └── logo
│       │       ├── icon_image.png
│       │       └── image.png
│       ├── components
│       │   └── examples
│       │       ├── pagination.py
│       │       └── status.py
│       ├── contracts
│       │   ├── component.py
│       │   ├── injector.py
│       │   ├── page.py
│       │   └── section.py
│       ├── home.py
│       ├── infra
│       │   ├── repositories
│       │   │   └── status_message.py
│       │   ├── resources
│       │   │   ├── css.py
│       │   │   ├── html.py
│       │   │   └── javascript.py
│       │   └── settings
│       │       └── base.py
│       ├── __init__.py
│       ├── injectors
│       │   ├── css.py
│       │   ├── html.py
│       │   ├── injectables.py
│       │   └── javascript.py
│       ├── pages
│       │   └── example.py
│       └── sections
│           ├── bottom.py
│           ├── content.py
│           └── sidebar.py
├── docker
│   └── Dockerfile
├── readme.md
└── requirements.txt
```


JavaScript Injection — Considerações

O JavaScriptInjector possui uma responsabilidade limitada: ler o conteúdo de um arquivo JavaScript e injetá-lo na página. O injector não gerencia o lifecycle ou o estado do JavaScript executado.

Como o Streamlit pode reconstruir partes do DOM durante reruns e navegação entre páginas, scripts injetados devem considerar que elementos podem ser criados, removidos ou substituídos.

Ao criar scripts para injeção, recomenda-se:

tornar a inicialização idempotente;
verificar se os elementos necessários existem antes de utilizá-los;
evitar o registro repetido de event listeners;
não assumir que referências a elementos do DOM permanecerão válidas indefinidamente;
utilizar MutationObserver ou event delegation quando o comportamento precisar acompanhar elementos reconstruídos;
não utilizar variáveis JavaScript locais como mecanismo de persistência de estado da aplicação.


O JavaScriptInjector não modifica, encapsula ou gerencia o código JavaScript fornecido pelo usuário. A responsabilidade por compatibilidade com o lifecycle do DOM é do script injetado.




### EM CONSTRUCAO ###