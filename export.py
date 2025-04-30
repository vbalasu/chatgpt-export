from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com", wait_until="networkidle")

    page.evaluate("""
        banner = document.createElement('div');
        banner.textContent = 'Hello from Python!';
        banner.style.cssText = 'position:fixed; inset:0; display:grid; place-items:center; font:900 3rem/1 system-ui; color:white; background:rgba(0,0,0,.7);';
        document.body.append(banner);
    """)
    page.wait_for_timeout(0)
    page.pdf(path="page.pdf", format="Letter", print_background=True)
    browser.close()