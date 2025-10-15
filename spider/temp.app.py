import control_PW
import time
import Jumbo_SP

head = True
url = "https://www.jumbocolombia.com/"
Browser = control_PW.iniciar_playwright(head)
Page = control_PW.crear_page(Browser, url)


producto = "arroz diana"

Jumbo_SP.jubo_buscar(Page, producto)
print("ya")
try:
    Jumbo_SP.jumbo_rascador(Page)
finally:
    Browser.close()
