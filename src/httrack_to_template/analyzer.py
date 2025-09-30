"""
Website structure analyzer for HTTrack mirrors.
"""
from pathlib import Path
from bs4 import BeautifulSoup

class WebsiteAnalyzer:
    """Analyzes HTTrack website structure and content."""

    def analyze(self, root_path):
        """Analyze the complete website structure."""
        root_path = Path(root_path)
        pages = []
        for html_file in root_path.rglob("*.html"):
            page_info = self._analyze_html_page(html_file, root_path)
            pages.append(page_info)
        assets = self._analyze_assets(root_path)
        return {"pages": pages, "assets": assets}

    def _analyze_html_page(self, file_path, root_path):
        soup = BeautifulSoup(file_path.read_text(encoding="utf-8"), "html.parser")
        return {
            "path": str(file_path.relative_to(root_path)),
            "title": self._extract_title(soup),
            "headers": self._extract_headers(soup),
            "navigation": self._extract_navigation(soup),
            "forms": self._extract_forms(soup),
            "images": self._extract_images(soup),
        }

    def _extract_title(self, soup):
        title_tag = soup.find("title")
        return title_tag.text.strip() if title_tag else ""

    def _extract_headers(self, soup):
        headers = []
        for tag in ["h1", "h2", "h3"]:
            headers.extend([h.get_text(strip=True) for h in soup.find_all(tag)])
        return headers

    def _extract_navigation(self, soup):
        nav = soup.find("nav")
        if nav:
            return [a.get("href") for a in nav.find_all("a", href=True)]
        # fallback: all top-level links
        return [a.get("href") for a in soup.find_all("a", href=True)]

    def _extract_forms(self, soup):
        forms = []
        for form in soup.find_all("form"):
            forms.append({
                "action": form.get("action"),
                "method": form.get("method", "get").lower(),
                "inputs": [inp.get("name") for inp in form.find_all("input") if inp.get("name")]
            })
        return forms

    def _extract_images(self, soup):
        return [img.get("src") for img in soup.find_all("img", src=True)]

    def _analyze_assets(self, root_path):
        assets = {"css": [], "js": [], "images": []}
        for ext, key in [("*.css", "css"), ("*.js", "js"), ("*.png", "images"), ("*.jpg", "images"), ("*.jpeg", "images"), ("*.gif", "images")]:
            for file in root_path.rglob(ext):
                assets[key].append(str(file.relative_to(root_path)))
        return assets