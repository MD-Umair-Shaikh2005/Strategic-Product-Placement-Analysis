#!/usr/bin/env python
"""
Dataset Download Script
Downloads the product placement dataset from Kaggle and prepares it for analysis.
"""

import os
import subprocess
import requests
from pathlib import Path

def download_from_kaggle():
    """Download dataset from Kaggle using Kaggle API"""
    try:
        import kaggle
        print("📥 Downloading dataset from Kaggle...")
        
        # Ensure data directory exists
        data_dir = Path('data')
        data_dir.mkdir(exist_ok=True)
        
        # Download dataset
        kaggle.api.dataset_download_files(
            'amitvkulkarni/impact-of-product-positioning-on-sales',
            path=str(data_dir),
            unzip=True
        )
        
        print("✓ Dataset downloaded successfully!")
        
        # List files in data directory
        files = list(data_dir.glob('*.csv'))
        if files:
            print(f"✓ Found {len(files)} CSV file(s):")
            for file in files:
                print(f"  - {file.name}")
        
        return True
        
    except ImportError:
        print("✗ Kaggle API not installed.")
        print("  Install with: pip install kaggle")
        return False
    except Exception as e:
        print(f"✗ Error downloading dataset: {str(e)}")
        return False

def manual_download_info():
    """Print instructions for manual download"""
    print("\n" + "="*60)
    print("MANUAL DOWNLOAD INSTRUCTIONS")
    print("="*60)
    print("\n1. Visit: https://www.kaggle.com/datasets/amitvkulkarni/impact-of-product-positioning-on-sales")
    print("\n2. Click 'Download' button")
    print("\n3. Extract the CSV file to the 'data/' directory")
    print("\n4. Ensure file is named 'product_placement_data.csv'")
    print("\n5. Start the Flask app and upload via the web interface")
    print("="*60 + "\n")

if __name__ == '__main__':
    print("\n🔄 Product Placement Dataset Downloader\n")
    
    # Check if data already exists
    data_path = Path('data/product_placement_data.csv')
    if data_path.exists():
        print(f"✓ Dataset already exists at {data_path}")
    else:
        print("Dataset not found. Attempting to download...")
        if not download_from_kaggle():
            manual_download_info()
