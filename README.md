# Integrity Assistant - Password-Protected Downloads

This repository contains the code for creating password-protected downloads for the Integrity Assistant website.

## Why Password Protection?

Password-protected ZIP files have several advantages:

1. They bypass many antivirus false positives
2. They add an additional layer of security
3. They create a more professional download experience

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Make sure you have 7-Zip installed (optional but recommended):
   - Windows: [Download from 7-zip.org](https://www.7-zip.org/download.html)
   - Mac: `brew install p7zip`
   - Linux: `sudo apt-get install p7zip-full` or equivalent for your distribution

## Creating Protected Downloads

### Option 1: Build from Scratch

Run the main build script to create the applications and password-protected zip files:

```bash
python main.py
```

### Option 2: Protect Existing Zip Files

If you already have the zip files and just want to password-protect them:

1. Place your zip files in the `downloads` directory
2. Run the protection script:

```bash
python protect_zips.py
```

## Default Password

The default password is: `integrity2025`

You can change this by modifying:
- The `ZIP_PASSWORD` variable in `main.py`
- The `PASSWORD` variable in `protect_zips.py`
- The password display in the HTML download page

## Web Integration

The `index.html` file has been updated to include instructions for extracting the password-protected zip files.

## Troubleshooting

If you encounter issues:

1. Make sure pyzipper is installed: `pip install pyzipper`
2. Try using 7-Zip directly if the Python script fails
3. Verify that the zip files exist in the correct directory 