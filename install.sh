#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for Anaconda or Miniconda installation
if command_exists conda; then
    echo "Conda is already installed."
else
    echo "Conda is not installed. Proceeding to install Miniconda."

    # Set Miniconda installer URL
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
    INSTALLER="Miniconda3-latest-Linux-x86_64.sh"

    # Download Miniconda installer
    echo "Downloading Miniconda installer..."
    wget $MINICONDA_URL -O $INSTALLER

    # Install Miniconda
    echo "Installing Miniconda..."
    bash $INSTALLER -b -p $HOME/miniconda

    # Clean up the installer
    echo "Cleaning up..."
    rm $INSTALLER

    # Add Miniconda to PATH
    echo "Adding Miniconda to PATH..."
    export PATH="$HOME/miniconda/bin:$PATH"
    echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> ~/.bashrc

    # Initialize Conda
    echo "Initializing Conda..."
    source $HOME/miniconda/bin/conda init
fi

# Verify Conda installation
if command_exists conda; then
    echo "Conda installation completed successfully."
    conda --version
else
    echo "Conda installation failed. Please check manually."
    exit 1
fi

# Create YOLO environment
echo "Creating YOLO Conda environment..."
conda create -n yolo python=3.9 -y
conda activate yolo

# Install Python dependencies
echo "Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please provide the dependency file."
    exit 1
fi

# Download YOLO models
echo "Downloading YOLO models..."
if [ -f "urls.text" ]; then
    wget -i urls.text
else
    echo "urls.text not found. Please provide the file with download URLs."
    exit 1
fi

echo "Setup completed successfully."
