"""
Environment Setup Verification Script

This script verifies that your environment is correctly set up
for the Master LLM Engineer program.
"""

import sys
import os
from typing import Dict, List, Tuple

def check_python_version() -> Tuple[bool, str]:
    """Check if Python version is 3.10 or higher"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 10:
        return True, f"✅ Python {version.major}.{version.minor}.{version.micro}"
    return False, f"❌ Python {version.major}.{version.minor}.{version.micro} (3.10+ required)"

def check_package(package_name: str, import_name: str = None) -> Tuple[bool, str]:
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        return True, f"✅ {package_name}"
    except ImportError:
        return False, f"❌ {package_name} (not installed)"

def check_packages() -> List[Tuple[bool, str]]:
    """Check all required packages"""
    packages = [
        ("openai", "openai"),
        ("anthropic", "anthropic"),
        ("langchain", "langchain"),
        ("chromadb", "chromadb"),
        ("faiss-cpu", "faiss"),
        ("fastapi", "fastapi"),
        ("streamlit", "streamlit"),
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("python-dotenv", "dotenv"),
        ("tiktoken", "tiktoken"),
    ]
    
    return [check_package(pkg, imp) for pkg, imp in packages]

def check_env_vars() -> List[Tuple[bool, str]]:
    """Check if environment variables are set"""
    from dotenv import load_dotenv
    load_dotenv()
    
    vars_to_check = [
        ("OPENAI_API_KEY", True),  # Required
        ("ANTHROPIC_API_KEY", False),  # Optional
        ("GOOGLE_API_KEY", False),  # Optional
        ("PINECONE_API_KEY", False),  # Optional
    ]
    
    results = []
    for var_name, required in vars_to_check:
        value = os.getenv(var_name)
        if value and value != f"your_{var_name.lower()}_here":
            results.append((True, f"✅ {var_name}"))
        elif required:
            results.append((False, f"❌ {var_name} (required)"))
        else:
            results.append((None, f"⚠️  {var_name} (optional)"))
    
    return results

def test_openai_connection() -> Tuple[bool, str]:
    """Test OpenAI API connection"""
    try:
        from openai import OpenAI
        client = OpenAI()
        
        # Simple test call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        
        return True, "✅ OpenAI API connection successful"
    except Exception as e:
        return False, f"❌ OpenAI API connection failed: {str(e)}"

def print_section(title: str):
    """Print a section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def main():
    """Run all verification checks"""
    print("\n" + "="*60)
    print("  Master LLM Engineer - Setup Verification")
    print("="*60)
    
    all_passed = True
    
    # Check Python version
    print_section("Python Version")
    passed, message = check_python_version()
    print(message)
    if not passed:
        all_passed = False
    
    # Check packages
    print_section("Required Packages")
    package_results = check_packages()
    for passed, message in package_results:
        print(message)
        if not passed:
            all_passed = False
    
    # Check environment variables
    print_section("Environment Variables")
    env_results = check_env_vars()
    for passed, message in env_results:
        print(message)
        if passed is False:
            all_passed = False
    
    # Test API connection (only if OpenAI key is set)
    if os.getenv("OPENAI_API_KEY") and os.getenv("OPENAI_API_KEY") != "your_openai_api_key_here":
        print_section("API Connection Test")
        passed, message = test_openai_connection()
        print(message)
        if not passed:
            all_passed = False
    
    # Final summary
    print_section("Summary")
    if all_passed:
        print("✅ All checks passed! You're ready to start.")
        print("\nNext steps:")
        print("1. Navigate to week-01-llm-foundations/")
        print("2. Read the README.md")
        print("3. Start learning!")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print("\nTroubleshooting:")
        print("1. Install missing packages: pip install -r requirements.txt")
        print("2. Set up environment variables in .env file")
        print("3. Verify API keys are correct")
        print("4. Run this script again")
    
    print("\n" + "="*60 + "\n")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
