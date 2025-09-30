"""
HTTrack to Template - Convert HTTrack website mirrors into reusable templates.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .core import HTTrackToTemplate
from .analyzer import WebsiteAnalyzer
from .generator import TemplateGenerator

__all__ = ["HTTrackToTemplate", "WebsiteAnalyzer", "TemplateGenerator"]