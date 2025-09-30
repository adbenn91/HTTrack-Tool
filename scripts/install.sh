#!/bin/bash

echo "🚀 Installing HTTrack to Template..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required"
    exit 1
fi

python3 -m venv httrack_env
source httrack_env/bin/activate

pip install -e .

echo "✅ Installation complete!"
echo "💡 Activate: source httrack_env/bin/activate"
echo "🚀 Run: httrack2template --help"