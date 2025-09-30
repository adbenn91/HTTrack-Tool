"""
Main HTTrack to Template converter class.
"""

from pathlib import Path
from .analyzer import WebsiteAnalyzer
from .generator import TemplateGenerator

class HTTrackToTemplate:
    """Main converter class that orchestrates the conversion process."""

    def __init__(self, config_file=None):
        self.config = self._load_config(config_file) if config_file else {}

    def _load_config(self, config_file):
        # Placeholder for config loading logic (e.g., YAML/JSON)
        return {}

    def convert(self, input_dir, output_dir, template_name="website_template"):
        analyzer = WebsiteAnalyzer()
        structure = analyzer.analyze(input_dir)
        generator = TemplateGenerator()
        config = {"input_dir": input_dir}
        generator.generate(structure, output_dir, template_name, config=config)