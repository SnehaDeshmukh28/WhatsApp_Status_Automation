# WhatsApp Status Automation Script

This script automates posting a status on WhatsApp Web using Selenium.

## Features
- Automatically uploads a photo.
- Adds a custom caption.
- Posts the status.

## Prerequisites
1. Install [Google Chrome](https://www.google.com/chrome/) and [ChromeDriver](https://chromedriver.chromium.org/).
2. Install the required Python packages:
   ```bash
   pip install selenium pyperclip
   ```

## Usage
1. Update the placeholders in the script with your file paths:
   - `path/to/chromedriver` (ChromeDriver executable path)
   - `path/to/photo.jpg` (Photo to upload)
   - `Your caption here` (Caption text)
2. Run the script:
   ```bash
   python script_name.py
   ```

## Notes
- The script uses a user session directory (`path/to/user-data-dir`) for login persistence. Ensure you provide a valid path or login manually on the first run. 
- Ensure ChromeDriver matches your Chrome version.
