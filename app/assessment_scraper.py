from playwright.sync_api import sync_playwright
import re
import json


from discover_urls import discover_urls
assessment_urls = discover_urls()

def scrape_assessment(url):
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page(
            viewport={"width": 1400, "height": 900}
        )

        page.goto(url, wait_until="networkidle")

        try:
            page.get_by_text("Allow all cookies").click(timeout=3000)
        except:
            pass

        page.wait_for_timeout(2000)

        title = page.locator("h1").inner_text()

        description = page.locator("h1").locator("xpath=following::p[1]").inner_text()

        result = {
        "title": title,
        "description": description,
        "url": url
    }

        browser.close()

        return result

results = []

for url in assessment_urls:
    results.append(scrape_assessment(url))

with open("data/assessments.json", "w") as f:
    json.dump(results, f, indent=4)

print("Saved", len(results), "assessments!")