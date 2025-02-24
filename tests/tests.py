from playwright.sync_api import sync_playwright

def test_add_to_cart():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)  # Set True to run in background
        page = browser.new_page()

        page.goto("https://www.demoblaze.com/index.html#")
        link_samsung_galaxy = page.get_by_role("link", name="Samsung galaxy s6")

        # Click on the first product
        link_samsung_galaxy.click()

        page.wait_for_selector(".btn-success")
        page.click(".btn-success")

        page.wait_for_event("dialog").accept()

        page.click("#cartur")
        page.wait_for_selector(".success")

        cart_items = page.locator(".success").count()
        assert cart_items > 0, "Cart is empty, test failed!"

        print("Test Passed: Item successfully added to cart")
        browser.close()

if __name__ == "__main__":
    test_add_to_cart()

