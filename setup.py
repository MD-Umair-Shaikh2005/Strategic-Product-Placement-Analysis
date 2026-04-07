#!/usr/bin/env python
"""
Quick Start Script
Initializes the project and guides through setup.
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")


def check_python_version():
    """Check if Python version is 3.8+"""
    if sys.version_info < (3, 8):
        print("✗ Python 3.8+ is required")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")


def check_dependencies():
    """Check if pip is available"""
    try:
        import pip
        print("✓ pip is available")
        return True
    except ImportError:
        print("✗ pip not found. Please install Python with pip.")
        return False


def create_venv():
    """Create virtual environment"""
    if Path('venv').exists():
        print("✓ Virtual environment already exists")
    else:
        print("📦 Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
        print("✓ Virtual environment created")


def install_requirements():
    """Install requirements"""
    print("\n📥 Installing requirements...")
    if sys.platform == 'win32':
        python = Path('venv/Scripts/python.exe')
    else:
        python = Path('venv/bin/python')
    
    subprocess.run([str(python), '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    print("✓ Requirements installed")


def setup_env_file():
    """Create .env file from example"""
    if not Path('.env').exists():
        print("\n⚙️  Creating .env file...")
        if Path('.env.example').exists():
            import shutil
            shutil.copy('.env.example', '.env')
            print("✓ .env file created from example")
        else:
            print("⚠️  .env.example not found, skipping")


def create_data_directory():
    """Ensure data directory exists"""
    Path('data').mkdir(exist_ok=True)
    print("✓ Data directory ready")


def print_next_steps():
    """Print next steps"""
    print_header("SETUP COMPLETE ✓")
    print("Next steps:\n")
    print("1. Activate virtual environment:")
    if sys.platform == 'win32':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("\n2. Download dataset:")
    print("   python download_dataset.py")
    print("   OR visit: https://www.kaggle.com/datasets/amitvkulkarni/impact-of-product-positioning-on-sales")
    
    print("\n3. Start the application:")
    print("   python app.py")
    
    print("\n4. Open browser and visit:")
    print("   http://localhost:5000")
    
    print("\n5. Upload your CSV file and explore the dashboard!")
    print("\n" + "="*60 + "\n")


def main():
    """Main setup script"""
    print_header("STRATEGIC PRODUCT PLACEMENT ANALYSIS")
    print("Project Setup & Quick Start\n")
    
    try:
        # Check prerequisites
        print("Checking prerequisites...")
        check_python_version()
        check_dependencies()
        
        # Setup project
        print("\n📋 Setting up project structure...")
        create_data_directory()
        create_venv()
        setup_env_file()
        
        # Install dependencies
        install_requirements()
        
        # Success
        print_next_steps()
        
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Setup failed: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user")
        sys.exit(1)


if __name__ == '__main__':
    main()
