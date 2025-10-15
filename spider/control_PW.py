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
