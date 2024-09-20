from fasthtml.common import *
from custom_css import custom_css
from components import *

app = FastHTML()

# Agregar carpeta static de imagenes
app.mount('/static', StaticFiles(directory='static'), name='static')

# Page layout
def side_bar():
    return Aside(
        chester_profile(),
        Div(
            H2("Tienes alguna travesura mia?"),
            Card_form(),
        ),
        cls="sidebar"
    )

def header():
    return Header(
        H2("Las aventuras de chester"),
        Div(
            Ul(
                Li("Home"),
                Li("About"),
                Li("Contact"),
                cls = "redes-sociales"
            )
        ),
        cls="header"
    )

def main():
    return Main(
        Cards_container()
    )

def homePage():
    return Html(
        Head(
            picolink,
            custom_css
        ),
        Body(
            Div(
                side_bar(),
                Div(
                    header(),
                    main(),
                    cls="content"
                ),
                cls="main-container"
            )
        )
    )

@app.get('/')
def home():
    return homePage()

@app.post('/')
def add_card(title:str, content:str):
    cards.append(Card(title, content))
    return Redirect('/')

serve()