#!/usr/bin/env python3
"""
Demo script for HTTrack to Template tool.
"""

from pathlib import Path
from src.httrack_to_template.core import HTTrackToTemplate

def main():
    print("🎬 HTTrack to Template Demo")
    print("=" * 40)
    
    # Create demo website
    demo_dir = Path('demo_website')
    demo_dir.mkdir(exist_ok=True)
    
    index_html = """<!DOCTYPE html>
<html>
<head>
    <title>Demo Company</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
    </nav>
    <h1>Welcome to Demo Company</h1>
    <p>This is a demo website.</p>
</body>
</html>"""
    
    (demo_dir / 'index.html').write_text(index_html)
    (demo_dir / 'about.html').write_text(index_html.replace('Home', 'About'))
    
    css_content = "body { font-family: Arial; margin: 40px; }"
    (demo_dir / 'style.css').write_text(css_content)
    
    print(f"✅ Created demo website at: {demo_dir}")
    
    # Convert to template
    converter = HTTrackToTemplate()
    output_path = converter.convert(
        input_dir=demo_dir,
        output_dir='output_templates',
        template_name='demo_template'
    )
    
    print(f"✅ Generated template at: {output_path}")
    print("🎉 Demo completed successfully!")

if __name__ == '__main__':
    main()