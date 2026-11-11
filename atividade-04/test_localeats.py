import re

from playwright.sync_api import Page, expect

URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"



def test_pagina_inicial_e_navegacao_para_meus_pedidos(page: Page):
    page.goto(URL_LOCALEATS)

    titulo = page.get_by_role(
        "heading", name="Descubra sabores"
    )
    expect(titulo).to_be_visible()
    page.get_by_role("link", name="Meus Pedidos").click()
    expect(page).to_have_url(re.compile(r"orders\.html"))
    expect(page.get_by_role("link", name="Explorar")).to_be_visible()
