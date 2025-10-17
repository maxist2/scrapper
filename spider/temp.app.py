import control_PW
import Jumbo_SP

head = False
url = "https://www.jumbocolombia.com/arroz%20diana"
Browser = control_PW.iniciar_playwright(head)
Page = control_PW.crear_page(Browser, url)


producto = "arroz diana"

# Jumbo_SP.jubo_buscar(Page, producto)

print("ya")
try:
    Jumbo_SP.jumbo_rascador(Page)
    Page.locator()
    Jumbo_SP.jumbo_rascador(Page)
finally:
    Browser.close()

Browser.close()
