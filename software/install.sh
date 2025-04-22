#!/bin/bash
echo "Installing Eco-Note+ Dependencies..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip chromium-browser
pip3 install onnxruntime opencv-python numpy requests
echo "Installation complete."
