from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="httrack-to-template",
    version="1.0.0",
    description="Convert HTTrack website mirrors into reusable templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/HTTrack-To-Template",
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="httrack, template, website, conversion",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8, <4",
    install_requires=[
        "beautifulsoup4>=4.9.3",
        "Pillow>=8.0.0",
        "Jinja2>=3.0.0",
        "click>=8.0.0"
    ],
    extras_require={
        "dev": ["pytest>=6.0", "black", "flake8"],
        "web": ["flask>=2.0.0"]
    },
    entry_points={
        "console_scripts": [
            "httrack2template=httrack_to_template.cli:main",
        ],
    },
)