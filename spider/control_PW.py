from playwright.sync_api import sync_playwright


def iniciar_playwright(head=False):
    # iniciar playwright
    playwright = sync_playwright().start()
    Browser = playwright.chromium.launch(headless=head)
    return Browser


def crear_page(Browser, url):
    Page = Browser.new_page()
    Page.goto(url)
    return Page


PATRON = r"(?i)\b(500[\s\-\.,_]*(g|gr|grs|gramos?)|0[\s\-\.,_]*5[\s\-\.,_]*(k|kg|kilo?s?)|½[\s\-\.,_]*(k|kg|kilo?s?)|1\/2[\s\-\.,_]*(k|kg|kilo?s?))\b"
