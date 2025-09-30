"""
Command-line interface for HTTrack to Template.
"""

import click
from .core import HTTrackToTemplate

@click.group()
def cli():
    """HTTrack to Template CLI."""
    pass

@cli.command()
@click.argument('input_dir', type=click.Path(exists=True, file_okay=False))
@click.argument('output_dir', type=click.Path())
@click.option('--name', default='website_template', help='Template name')
def convert(input_dir, output_dir, name):
    """Convert an HTTrack mirror to a reusable template."""
    click.echo(f"🔄 Converting {input_dir} to template '{name}' in {output_dir} ...")
    converter = HTTrackToTemplate()
    converter.convert(input_dir, output_dir, name)
    click.echo("✅ Conversion complete!")

@cli.command()
def demo():
    """Show a demo message."""
    click.echo("🎬 Demo: Use 'convert' to process your HTTrack website mirror.")

def main():
    cli()

if __name__ == '__main__':
    main()