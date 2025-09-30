"""
Tests for the website analyzer.
"""

import pytest
from pathlib import Path
from src.httrack_to_template.analyzer import WebsiteAnalyzer

def test_analyze_simple_html(tmp_path):
    html_content = """<!DOCTYPE html>
<html>
<head><title>Test Page</title></head>
<body>
    <h1>Welcome</h1>
    <nav><a href="about.html">About</a></nav>
</body>
</html>"""
    
    html_file = tmp_path / "test.html"
    html_file.write_text(html_content)
    
    analyzer = WebsiteAnalyzer()
    structure = analyzer.analyze(tmp_path)
    
    assert len(structure['pages']) == 1
    assert structure['pages'][0]['title'] == "Test Page"