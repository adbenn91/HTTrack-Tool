"""
Template generator for creating reusable templates from analysis.
"""

from pathlib import Path
import shutil

class TemplateGenerator:
    """Generates reusable templates from analyzed website structure."""
    
    def generate(self, structure, output_dir, template_name, config=None):
        """Generate the complete template."""
        output_path = Path(output_dir) / template_name
        output_path.mkdir(parents=True, exist_ok=True)
        
        self._generate_html_templates(structure, output_path)
        self._copy_assets(structure, output_path, config)

    def _generate_html_templates(self, structure, output_path):
        pages = structure.get("pages", [])
        for page in pages:
            html_content = self._build_html(page)
            page_path = output_path / page["path"]
            page_path.parent.mkdir(parents=True, exist_ok=True)
            page_path.write_text(html_content, encoding="utf-8")

    def _build_html(self, page):
        # Simple HTML template; you can expand this with Jinja2 if needed
        headers = "".join(f"<h2>{h}</h2>" for h in page["headers"])
        nav = "".join(f'<a href="{href}">{href}</a> ' for href in page["navigation"])
        images = "".join(f'<img src="{src}" />' for src in page["images"])
        forms = "".join(
            f'<form action="{f["action"]}" method="{f["method"]}">' +
            "".join(f'<input name="{inp}" />' for inp in f["inputs"]) +
            "</form>"
            for f in page["forms"]
        )
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>{page["title"]}</title>
</head>
<body>
    <nav>{nav}</nav>
    {headers}
    {images}
    {forms}
</body>
</html>
"""

    def _copy_assets(self, structure, output_path, config=None):
        # Copy CSS, JS, and images to the output template directory
        assets = structure.get("assets", {})
        for asset_type, files in assets.items():
            for rel_path in files:
                src = Path(config["input_dir"]) / rel_path if config and "input_dir" in config else rel_path
                dest = output_path / rel_path
                dest.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.copy2(src, dest)
                except Exception:
                    pass  # Ignore missing files for now