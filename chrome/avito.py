from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click()
    page.goto("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")
    page.locator("button").filter(has_text="Добавить в избранное").click()
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
