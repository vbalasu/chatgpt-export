from playwright.sync_api import sync_playwright
import subprocess, sys

def export_pdf(url, output_file="page.pdf"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

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
            path=output_file,
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
    return output_file

def run_export(url):
    # Run the export.py script as a separate process.
    # Use this to run from notebook environments
    result = subprocess.run(['python', 'export.py', url], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error:", result.stderr)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://chatgpt.com/share/6810cca4-ff2c-8001-9773-2ae4a3adf124"
    output_file = export_pdf(url)
    print(f"PDF exported to {output_file}")