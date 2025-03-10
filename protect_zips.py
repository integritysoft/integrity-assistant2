#!/usr/bin/env python3
"""
Utility script to password-protect existing zip files
"""

import os
import sys
import subprocess
import shutil

# Configuration
DOWNLOADS_DIR = "downloads"  # Directory containing the zip files
PASSWORD = "integrity2025"   # Password to use for protection

def protect_zip_with_7z(zip_path):
    """Password-protect a zip file using 7z"""
    print(f"Processing: {zip_path}")
    
    # Create a temporary filename
    temp_path = f"{zip_path}.protected"
    
    try:
        # Try to use 7z to create a password-protected zip
        result = subprocess.run(
            ["7z", "a", "-p"+PASSWORD, "-mem=AES256", temp_path, zip_path],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            # Success - replace the original with the protected version
            os.remove(zip_path)
            os.rename(temp_path, zip_path)
            print(f"✓ Successfully protected: {zip_path}")
            return True
        else:
            print(f"✗ Failed to protect with 7z: {result.stderr}")
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False

def protect_zip_with_pyzipper(zip_path):
    """Password-protect a zip file using pyzipper"""
    print(f"Processing: {zip_path}")
    
    try:
        # First, rename the original file
        temp_original = f"{zip_path}.original"
        os.rename(zip_path, temp_original)
        
        # Try to use pyzipper
        import pyzipper
        
        # Extract contents to a temporary directory
        temp_dir = f"{zip_path}.extracted"
        os.makedirs(temp_dir, exist_ok=True)
        
        # Extract original zip
        with pyzipper.ZipFile(temp_original, 'r') as zipf:
            zipf.extractall(temp_dir)
        
        # Create new password-protected zip
        with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
            zipf.setpassword(PASSWORD.encode())
            
            # Add all files from the extracted directory
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, temp_dir)
                    zipf.write(full_path, rel_path)
        
        # Clean up
        os.remove(temp_original)
        shutil.rmtree(temp_dir)
        
        print(f"✓ Successfully protected: {zip_path}")
        return True
    except ImportError:
        print("✗ pyzipper not installed. Install with: pip install pyzipper")
        # Restore original file
        if os.path.exists(temp_original):
            if os.path.exists(zip_path):
                os.remove(zip_path)
            os.rename(temp_original, zip_path)
        return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        # Restore original file
        if os.path.exists(temp_original):
            if os.path.exists(zip_path):
                os.remove(zip_path)
            os.rename(temp_original, zip_path)
        # Clean up temp directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        return False

def main():
    """Main function to protect all zip files in the downloads directory"""
    # Ensure downloads directory exists
    if not os.path.exists(DOWNLOADS_DIR):
        print(f"Error: Directory '{DOWNLOADS_DIR}' not found")
        return 1
    
    # Get all zip files
    zip_files = [f for f in os.listdir(DOWNLOADS_DIR) if f.endswith('.zip')]
    
    if not zip_files:
        print(f"No zip files found in '{DOWNLOADS_DIR}'")
        return 1
    
    print(f"Found {len(zip_files)} zip files to protect")
    
    # Try pyzipper first, fall back to 7z if needed
    success_count = 0
    for zip_file in zip_files:
        zip_path = os.path.join(DOWNLOADS_DIR, zip_file)
        
        # Try with pyzipper first
        try:
            import pyzipper
            if protect_zip_with_pyzipper(zip_path):
                success_count += 1
                continue
        except ImportError:
            print("pyzipper not available, trying 7z...")
        
        # Fall back to 7z
        if protect_zip_with_7z(zip_path):
            success_count += 1
    
    print(f"\nSummary: Protected {success_count} of {len(zip_files)} zip files")
    
    if success_count == len(zip_files):
        print("\nAll files protected successfully!")
        return 0
    else:
        print("\nSome files could not be protected. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 