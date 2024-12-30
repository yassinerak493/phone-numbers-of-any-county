from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your updated chromedriver executable
service = Service(executable_path=r'C:\path\to\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=service)

def check_whatsapp_registration(phone_number):
    driver.get('https://web.whatsapp.com/')
    
    # Wait for the QR code scan to be completed manually before proceeding
    # It's assumed that QR code is already scanned before running this script
    time.sleep(6)  # Wait for 10 seconds to ensure the WhatsApp Web is fully loaded
    
    try:
        # Wait for the new chat button to be present
        print("Waiting for new chat button...")
        new_chat_button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-icon="new-chat-outline"]'))
        )
        print("New chat button found.")
        
        # Click the new chat button
        new_chat_button.click()
        
        # Wait for the search input to be present
        print("Waiting for search input...")
        search_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'selectable-text.copyable-text.x15bjb6t.x1n2onr6'))
        )
        print("Search input found.")
        
        # Enter the phone number to search
        search_input.click()
        search_input.send_keys(phone_number)
        
        # Wait for 5 seconds to allow search results to appear
        time.sleep(5)
        
        # Check if the word "contact" or similar text is present in the search results
        try:
            body_text = driver.find_element(By.TAG_NAME, 'body').text
            if "contact" in body_text.lower():
                print(f"Search result found for {phone_number}.")
                print(f"{phone_number} is registered on WhatsApp.")
                return True
            else:
                print(f"No contact found for {phone_number}.")
                print(f"{phone_number} is not registered on WhatsApp.")
                return False
        except Exception as e:
            print(f"An error occurred while checking for contact text: {e}")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def verify_whatsapp_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            phone_number = line.strip()
            if check_whatsapp_registration(phone_number):
                outfile.write(phone_number + '\n')
            else:
                print(f"Skipping to next number...")

# Example usage
input_file = 'phone_numbers_216.txt'
output_file = 'valide_phone_numbers_216.txt'
verify_whatsapp_numbers(input_file, output_file)

# Close the browser after processing
driver.quit()
