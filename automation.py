from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

# Set up the Chrome WebDriver
def setup_driver(chrome_driver_path, user_data_dir=None):
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    if user_data_dir:
        options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Suppress unnecessary logs
    return webdriver.Chrome(service=service, options=options)

# Function to post a WhatsApp Status
def post_whatsapp_status(driver, photo_path, caption):
    driver.get("https://web.whatsapp.com")

    # Wait for WhatsApp Web to load
    print("Waiting for WhatsApp Web to load...")
    try:
        WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
        )
        print("WhatsApp Web loaded successfully.")
    except Exception as e:
        print(f"Error loading WhatsApp Web: {e}")
        driver.quit()
        return

    try:
        # Navigate to Status section
        print("Attempting to click the Status button.")
        status_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-icon='status-outline']"))
        )
        status_button.click()
        print("Status button clicked successfully.")
        time.sleep(3)

        # Add a new status
        print("Attempting to click the Add Status button.")
        add_status_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-icon='plus']"))
        )
        add_status_button.click()
        time.sleep(3)

        # Click on "Photos & Videos" button
        print("Attempting to click 'Photos & Videos' button.")
        photos_videos_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='status-v3-photo-video']"))
        )
        photos_videos_button.click()
        time.sleep(2)

        # Upload photo
        print("Uploading photo...")
        upload_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        upload_input.send_keys(photo_path)
        time.sleep(5)

        # Add caption
        print("Adding caption...")
        pyperclip.copy(caption)  # Copy caption to clipboard

        caption_area = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true']"))
        )
        caption_area.click()
        caption_area.send_keys(Keys.CONTROL, 'v')  # Paste caption
        time.sleep(2)

        # Send the status
        print("Posting the status...")
        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-icon='send']"))
        )
        send_button.click()
        print("Status posted successfully!")
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred while posting the status: {e}")
    finally:
        driver.quit()
        print("Script completed. Browser closed.")

# Main function
if __name__ == "__main__":
    # Specify the path to the ChromeDriver and other parameters
    chrome_driver_path = "path/to/chromedriver"  # Update this with the correct path
    user_data_dir = "path/to/user-data-dir"  # Optional: Provide the path for user session data
    photo_path = "path/to/photo.jpg"  # Update this with the correct photo path
    caption = "Your caption here"

    # Initialize the WebDriver
    driver = setup_driver(chrome_driver_path, user_data_dir)

    # Run the WhatsApp Status posting function
    post_whatsapp_status(driver, photo_path, caption)
