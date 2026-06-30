from playwright.sync_api import sync_playwright

URL = "https://www.shl.com/products/assessments/"

def discover_urls():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page(
            viewport={"width": 1400, "height": 900}
        )

        page.goto(URL, wait_until="networkidle")

        try:
            page.get_by_text("Allow all cookies").click(timeout=3000)
        except:
            pass

        page.wait_for_timeout(3000)

        links = page.locator("a").evaluate_all("""
            els => els.map(e => ({
                text: e.innerText,
                href: e.href
            }))
        """)

        assessment_links = []

        for link in links:
            href = link.get("href", "")

            if (
                "/products/assessments/" in href
                and href.count("/") > 6
                and href not in assessment_links
            ):
                assessment_links.append(href)

        browser.close()

        return assessment_links


if __name__ == "__main__":
    urls = discover_urls()

    for url in urls:
        print(url)