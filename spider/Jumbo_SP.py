import re
from control_PW import PATRON


def jubo_buscar(Page, producto):
    Page.wait_for_selector("#downshift-0-input")
    Page.fill("#downshift-0-input", "")
    Page.type("#downshift-0-input", producto)
    Page.press("#downshift-0-input", "Enter")
    return Page


def jumbo_rascador(Page):
    productos = []

    for x in range(28):
        print(x)
        Page.wait_for_selector(f"div[data-af-product-position='{1+x}']")
        producto = Page.locator(f"div[data-af-product-position='{1+x}']")

        nombre = producto.locator("div > h3 > span").inner_text()

        if nombre.matches(PATRON):
            print(nombre)
            precio = producto.locator("div > div > div > div > span").inner_text()
            print(precio)
            try:
                pre_des = producto.locator(
                    '//*[@id="items-price"]/div/span/div'
                ).inner_text()
                print(pre_des)
            except:
                pre_des = "sin descuento"
                print(pre_des)

            productos.append({"nombre": nombre, "precio": f"${precio}"})

    print(productos)
