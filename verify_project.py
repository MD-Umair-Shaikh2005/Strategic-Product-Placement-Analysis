#!/usr/bin/env python
"""
Project Verification Checklist
Automated script to verify all project files are in place
"""

import os
from pathlib import Path


def check_file_exists(filepath, description=""):
    """Check if file exists"""
    status = "✅" if Path(filepath).exists() else "❌"
    desc = f" - {description}" if description else ""
    print(f"{status} {filepath}{desc}")
    return Path(filepath).exists()


def check_project():
    """Verify all project files"""
    print("\n" + "="*70)
    print("  PROJECT VERIFICATION CHECKLIST")
    print("="*70 + "\n")
    
    all_checks = []
    
    # Core Files
    print("🔍 Core Application Files:")
    all_checks.append(check_file_exists("app.py", "Main Flask application"))
    all_checks.append(check_file_exists("config.py", "Configuration settings"))
    all_checks.append(check_file_exists("requirements.txt", "Python dependencies"))
    
    # Scripts
    print("\n📚 Data Processing Scripts:")
    all_checks.append(check_file_exists("scripts/__init__.py", "Package initialization"))
    all_checks.append(check_file_exists("scripts/data_preparation.py", "Data cleaning module"))
    all_checks.append(check_file_exists("scripts/visualizations.py", "Visualization module"))
    
    # Templates
    print("\n🌐 HTML Templates:")
    all_checks.append(check_file_exists("templates/base.html", "Base template"))
    all_checks.append(check_file_exists("templates/index.html", "Home page"))
    all_checks.append(check_file_exists("templates/dashboard.html", "Dashboard page"))
    all_checks.append(check_file_exists("templates/story.html", "Story page"))
    all_checks.append(check_file_exists("templates/insights.html", "Insights page"))
    all_checks.append(check_file_exists("templates/error.html", "Error page"))
    
    # Static Assets
    print("\n🎨 Static Assets:")
    all_checks.append(check_file_exists("static/css/style.css", "Styling"))
    all_checks.append(check_file_exists("static/js/main.js", "JavaScript utilities"))
    
    # Utilities
    print("\n🔧 Setup & Utility Scripts:")
    all_checks.append(check_file_exists("setup.py", "Automated setup"))
    all_checks.append(check_file_exists("download_dataset.py", "Dataset downloader"))
    all_checks.append(check_file_exists("advanced_processing_example.py", "Advanced data processing"))
    
    # Documentation
    print("\n📖 Documentation:")
    all_checks.append(check_file_exists("README.md", "Main documentation"))
    all_checks.append(check_file_exists("EXECUTION_GUIDE.md", "Execution guide"))
    all_checks.append(check_file_exists("CHANGELOG.md", "Changelog"))
    all_checks.append(check_file_exists("PROJECT_SUMMARY.md", "Project summary"))
    
    # Configuration
    print("\n⚙️  Configuration Files:")
    all_checks.append(check_file_exists(".env.example", "Environment template"))
    all_checks.append(check_file_exists(".gitignore", "Git ignore patterns"))
    
    # Directories
    print("\n📁 Directories:")
    all_checks.append(check_file_exists("data", "Data directory") or check_dir_exists("data"))
    all_checks.append(check_file_exists("templates", "Templates directory") or check_dir_exists("templates"))
    all_checks.append(check_file_exists("static", "Static assets directory") or check_dir_exists("static"))
    all_checks.append(check_file_exists("scripts", "Scripts directory") or check_dir_exists("scripts"))
    
    # Summary
    print("\n" + "="*70)
    passed = sum(all_checks)
    total = len(all_checks)
    percentage = (passed / total * 100) if total > 0 else 0
    
    print(f"\n✅ VERIFICATION COMPLETE")
    print(f"Files Present: {passed}/{total} ({percentage:.1f}%)")
    
    if passed == total:
        print("\n🎉 ALL FILES PRESENT - PROJECT READY TO RUN!")
    else:
        print(f"\n⚠️  Missing {total - passed} file(s) - Check output above")
    
    print("="*70 + "\n")
    
    return passed == total


def check_dir_exists(dirpath):
    """Check if directory exists"""
    exists = Path(dirpath).is_dir()
    status = "✅" if exists else "❌"
    print(f"{status} {dirpath}/ (directory)")
    return exists


def print_next_steps():
    """Print next steps"""
    print("\n" + "="*70)
    print("  NEXT STEPS")
    print("="*70 + "\n")
    
    print("1. RUN SETUP (creates virtual environment and installs dependencies):")
    print("   $ python setup.py\n")
    
    print("2. ACTIVATE VIRTUAL ENVIRONMENT:")
    print("   $ venv\\Scripts\\activate\n")
    
    print("3. DOWNLOAD DATASET (optional, can upload via web interface):")
    print("   $ python download_dataset.py\n")
    
    print("4. START THE APPLICATION:")
    print("   $ python app.py\n")
    
    print("5. OPEN IN BROWSER:")
    print("   http://localhost:5000\n")
    
    print("6. UPLOAD YOUR CSV FILE and explore the dashboard!\n")
    
    print("="*70 + "\n")
    
    print("📖 For detailed instructions, see: EXECUTION_GUIDE.md")
    print("📖 For full documentation, see: README.md")
    print("📖 For project overview, see: PROJECT_SUMMARY.md")
    print("\n")


def quick_start_guide():
    """Print quick start guide"""
    print("\n" + "="*70)
    print("  QUICK START GUIDE")
    print("="*70 + "\n")
    
    print("⚡ FASTEST WAY TO GET RUNNING:\n")
    
    print(">>> python setup.py")
    print(">>> venv\\Scripts\\activate")
    print(">>> python app.py")
    print(">>> Open http://localhost:5000 in your browser\n")
    
    print("Then upload your CSV dataset and start exploring!\n")
    
    print("="*70 + "\n")


if __name__ == '__main__':
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Run verification
    print(f"📍 Project Location: {project_dir}\n")
    
    all_present = check_project()
    
    if all_present:
        quick_start_guide()
    
    print_next_steps()
