from fasthtml.common import *

cards = []

# Componentes
def Card(title:str, content:str):
    return Article(
        Header(title),
        f"{content}",
        cls="card"
    )

def Cards_container():
    return Div(
        *[Card(title, content) for title, content in cards],
        cls="card-container"
    ) 

def Card_form():
    return Form(
        Input(placeholder="Titulo", name="title"),
        Input(placeholder="Contenido", name="content"),
        Button("Agregar anecdota", type="submit"),
        action='/', method="post"
    )
def chester_profile():
    return Div(
        P("Hola, mi nombre es..."),
        H2("Chester"),
        Img(src="/static/chester.jpeg", alt="chester"),
        cls="chester-profile"
    )