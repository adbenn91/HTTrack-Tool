#!/bin/bash

echo "🎬 Starting HTTrack to Template Demo..."

if [ -d "httrack_env" ]; then
    source httrack_env/bin/activate
fi

python examples/demo.py

echo "✅ Demo completed!"