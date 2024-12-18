import time
from colorama import Fore, Back, Style, init

# Initialize colorama to reset styles automatically
init(autoreset=True)

# Function to print the custom ASCII logo
def print_custom_logo():
    logo = """
\e[1;77m__        ___           _                         _   _            _   
 \ \      / / |__   __ _| |_ ___  __ _ _ __  _ __ | | | | __ _  ___| | __ 
  \ \ /\ / /| '_ \ / _  | __/ __|/ _  | '_ \| '_ \| |_| |/ _  |/ __| |/ / 
   \ V  V / | | | | (_| | |_\__ \ (_| | |_) | |_) |  _  | (_| | (__|   < 
    \_/\_/  |_| |_|\__,_|\__|___/\__,_| .__/| .__/|_| |_|\__,_|\___|_|\_\   v3.5\e[0m
"""
    print(logo)

# Start message function (code input verification)
def startMessage():
    OO0O0OO0OOO0OO0O0 = input(Fore.YELLOW + "Enter Code: ")
    OOOO0OO000OO0OOOO = "CPS"
    if OOOO0OO000OO0OOOO != OO0O0OO0OOO0OO0O0:
        print(Fore.RED + '[X] wrong code')
        print(Fore.BLUE + '''
   1. Purchase code From Instagram 
   2. insta Id cyberphantomsyndicate
   3. Send message for code
   4. Next time come with code and use this tool
   5. Bye
        ''')

# Fake hacking process to simulate hacking
def fake_hack_process(phone_number):
    # Simulate the hacking process with fake steps
    print(f"Starting to hack WhatsApp account for number: {phone_number}")
    time.sleep(1)  # Simulate waiting time

    print("\nStep 1: Verifying the phone number...")
    time.sleep(2)
    print("Step 2: Attempting to bypass two-factor authentication (2FA)...")
    time.sleep(3)

    print("Step 3: Searching for linked contacts and data...")
    time.sleep(4)
    print("Step 4: Decrypting chat history...")
    time.sleep(5)

    print("\n[ALERT] Hacking complete! Access granted to WhatsApp account.")
    print("login... Done.")
    time.sleep(1)
    print("\n[INFO] WhatsApp account compromised successfully.")
    print(f"Accessed chat history and contacts of {phone_number}.")

# Main function to run the program
def main():
    # Print the custom ASCII logo
    print_custom_logo()

    print("Welcome to WhatsApp Hacking!")
    print("This is for educational purposes only.")

    # Start the message to verify the code
    startMessage()

    # Get the phone number from the user to simulate the hacking process
    phone_number = input("\nEnter the phone number to Hack (in the format +1XXX-XXX-XXXX): ")

    print("\nAttempting to hack WhatsApp account...")
    fake_hack_process(phone_number)

if __name__ == "__main__":
    main()
