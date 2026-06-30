from playwright.sync_api import sync_playwright

url = "https://www.shl.com/products/assessments/personality-assessment/shl-occupational-personality-questionnaire-opq/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page(viewport={"width": 1400, "height": 900})

    page.goto(url, wait_until="networkidle")

    # Accept cookies if the popup exists
    try:
        page.get_by_text("Allow all cookies").click(timeout=3000)
    except:
        pass

    # Slowly scroll to the bottom
    for _ in range(15):
        page.mouse.wheel(0, 1500)
        page.wait_for_timeout(1000)

    print(page.title())
    print("=" * 100)

    print(page.locator("body").inner_text())

    browser.close()