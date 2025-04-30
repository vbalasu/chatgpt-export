from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://chatgpt.com/share/6810cca4-ff2c-8001-9773-2ae4a3adf124", wait_until="networkidle")

    page.evaluate("""
        (function() {
            var customStyles = `
                :not(.katex):not(.katex *) {
                    font-family: Arial, sans-serif !important;
                }
                :not(.katex) code:not(.katex *), :not(.katex) span:not(.katex *) {
                    font-family: Menlo, monospace !important;
                    white-space: pre-wrap !important;
                    overflow-wrap: break-word !important;
                }
                :not(.katex) .overflow-auto:not(.katex *), :not(.katex *) .overflow-auto {
                    overflow: visible !important;
                }
                :not(.katex) .h-full:not(.katex *), :not(.katex *) .h-full {
                    height: auto !important;
                }
                :not(.katex) #text:not(.katex *), :not(.katex *) #text {
                    white-space: pre-wrap !important;
                }
            `;
            var styleSheet = document.createElement('style');
            styleSheet.type = 'text/css';
            styleSheet.innerText = customStyles;
            document.head.appendChild(styleSheet);
            // Hide the "Skip to content" link
            document.querySelector('a[href="#main"]').style.display = 'none';
        })();
    """)
    page.wait_for_timeout(0)
    page.pdf(
        path="page.pdf",
        format="Letter",
        print_background=True,
        margin={
            "top": "0.5in",
            "right": "0.5in",
            "bottom": "0.5in",
            "left": "0.5in"
        }
    )
    browser.close()