import time
import random
import pyfiglet
import math

# ANSI escape codes for green, red, yellow text
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'

# Function to display the "WhatsApp" logo with figlet
def display_logo():
    logo = pyfiglet.figlet_format("WhatsApp", font="slant")
    print(f"{GREEN}{logo}{RESET}")

# Function to simulate a progress bar
def progress_bar(step, total_steps, process_name="Process"):
    progress = int(50 * (step / total_steps))
    bar = f"[{'#' * progress}{'.' * (50 - progress)}] {step}/{total_steps} {process_name} completed"
    print(f"{GREEN}{bar}{RESET}")

# Function to simulate logging output
def log_output(message, error=False):
    """Log output function with error handling"""
    if error:
        print(f"{RED}[ERROR] {message}{RESET}")
    else:
        print(f"{GREEN}[INFO] {message}{RESET}")
    time.sleep(random.uniform(1, 2))  # Simulate slight delay in logs

# New function: Simulate Instagram ID Input (for school project context)
def enter_instagram_id():
    print(f"{YELLOW}[INFO] Please enter the Instagram ID (for educational purposes only)...{RESET}")
    instagram_id = input("Enter Instagram username: ")  # Simulate input for Instagram username
    log_output(f"Instagram ID entered: {instagram_id}", error=False)
    return instagram_id

# Description: **Network Scanning** – The attacker scans the network to discover vulnerable devices or open ports.
def simulate_network_scanning():
    print(f"{YELLOW}[INFO] Scanning network for vulnerable devices and open ports...{RESET}")
    time.sleep(random.uniform(4, 6))  # Simulate network scanning delay

    open_ports = random.randint(1, 5)
    log_output(f"Found {open_ports} open ports on the target device.", error=False)

    time.sleep(random.uniform(2, 3))

# Description: **Exploiting Vulnerabilities** – Attacker exploits a system vulnerability (e.g., SQL Injection) to gain access.
def simulate_vulnerability_exploit():
    print(f"{YELLOW}[INFO] Exploiting system vulnerability (SQL Injection)...{RESET}")
    time.sleep(random.uniform(3, 5))  # Simulate exploit delay
    log_output(f"Exploit successful! Access gained to the target system.", error=False)
    time.sleep(random.uniform(2, 3))

# Description: **Password Cracking** – The attacker tries to crack a password via brute force or other methods.
def simulate_password_cracking():
    print(f"{YELLOW}[INFO] Starting password cracking attempt...{RESET}")
    time.sleep(random.uniform(2, 4))  # Simulate cracking delay

    attempts = 0
    while attempts < 10:  # Simulate 10 password attempts
        log_output(f"Trying password {attempts + 1}...", error=False)
        time.sleep(random.uniform(2, 3))  # Simulate time per attempt
        attempts += 1

    log_output(f"Password cracked successfully! Access to target account gained.", error=False)

# Description: **Simulate Phishing Attack** – The attacker sends a phishing email to steal credentials.
def simulate_phishing_attack(instagram_id):
    print(f"{YELLOW}[INFO] Sending phishing email to target Instagram account: {instagram_id}...{RESET}")
    time.sleep(random.uniform(3, 5))  # Simulate phishing delay

    log_output("Phishing email sent. Waiting for target to click link...", error=False)
    time.sleep(random.uniform(4, 6))

    # Simulating successful phishing response
    if random.random() > 0.2:  # 80% chance of success
        log_output(f"Target with Instagram ID {instagram_id} clicked the phishing link. Credentials stolen.", error=False)
    else:
        log_output("[ERROR] Phishing attack failed. Retrying...", error=True)
        time.sleep(random.uniform(4, 6))
        log_output("Phishing attack successful after retry.", error=False)

# Description: **Keylogger Activation** – The attacker installs a keylogger on the target device to capture keystrokes.
def simulate_keylogging():
    print(f"{YELLOW}[INFO] Activating keylogger on target device...{RESET}")
    time.sleep(random.uniform(3, 5))  # Simulate keylogger activation

    log_output("Keylogger is running... Capturing keystrokes...", error=False)
    time.sleep(random.uniform(6, 8))  # Simulate keylogging duration

    log_output("Keylog captured successfully. Credentials saved.", error=False)

# Description: **Privilege Escalation** – The attacker tries to gain elevated permissions on the target system.
def simulate_privilege_escalation():
    print(f"{YELLOW}[INFO] Attempting privilege escalation...{RESET}")
    time.sleep(random.uniform(2, 4))  # Simulate escalation attempt

    # Simulate success or failure of privilege escalation
    if random.random() > 0.3:  # 70% chance of success
        log_output("Privilege escalation successful. Gained administrator/root access.", error=False)
    else:
        log_output("[ERROR] Privilege escalation failed. Retrying...", error=True)
        time.sleep(random.uniform(4, 6))
        log_output("Privilege escalation successful after retry.", error=False)

# Description: **File Transfer Simulation** – The attacker transfers stolen files to an external location (fake cloud storage).
def simulate_file_transfer():
    file_name = random.choice(["chat_backup", "media_files", "contacts_export", "whatsapp_database", "whatsapp_vault"])
    file_size = random.randint(100, 700)  # In MB
    log_output(f"Starting file transfer: {file_name} ({file_size} MB)...", error=False)

    total_steps = math.ceil(file_size / 10)  # Simulating 10MB chunks for progress

    for step in range(1, total_steps + 1):
        time.sleep(random.uniform(3, 5))  # Simulate time per file chunk
        progress_bar(step, total_steps, process_name=f"Transfer {file_name}")
    
    log_output(f"File transfer of {file_name} completed successfully.", error=False)

# Description: **Cloud Data Upload** – The attacker uploads stolen data to a fake cloud service.
def simulate_data_transfer_to_cloud():
    log_output("Starting data transfer to Cyberphantomsyndicate Cloud...", error=False)
    time.sleep(random.uniform(3, 5))

    files = ["chat_backup.zip", "media_files.zip", "contacts_export.csv", "whatsapp_vault.tar.gz"]
    for file in files:
        log_output(f"Uploading {file}...", error=False)
        time.sleep(random.uniform(3, 6))  # Simulate file upload
        progress_bar(files.index(file) + 1, len(files), process_name=f"Uploading {file}")

    log_output("Data upload complete.", error=False)

# Description: ** Device Information Theft** – The attacker collects device-specific data.
def simulate_device_info_theft():
    print(f"{YELLOW}[INFO] Stealing device information (IP, MAC, OS version)...{RESET}")
    time.sleep(random.uniform(3, 5))  # Simulate info theft delay

    log_output("Device information successfully exfiltrated. IP, MAC, OS details saved.", error=False)

# Description: **Device Infection** – The attacker simulates infecting the device with malware.
def simulate_fake_device_infection():
    print(f"{YELLOW}[INFO] Simulating device infection with fake malware...{RESET}")
    time.sleep(random.uniform(3, 5))  # Simulate infection delay

    log_output("Device infected with fake malware. Executing payload...", error=False)
    time.sleep(random.uniform(3, 6))  # Simulate the execution of the malware payload
    log_output("Payload executed successfully. Device compromised.", error=False)

# Description: **Full Attack Sequence** – The attacker performs the full attack.
def simulate_full_attack():
    display_logo()

    # Step 1: Enter Instagram ID (for educational purposes)
    instagram_id = enter_instagram_id()

    # Step 2: Scan the network
    simulate_network_scanning()

    # Step 3: Exploit a vulnerability
    simulate_vulnerability_exploit()

    # Step 4: Crack passwords
    simulate_password_cracking()

    # Step 5: Conduct phishing attack with Instagram ID
    simulate_phishing_attack(instagram_id)

    # Step 6: Activate keylogger
    simulate_keylogging()

    # Step 7: Attempt privilege escalation
    simulate_privilege_escalation()

    # Step 8: Transfer stolen files
    simulate_file_transfer()

    # Step 9: Upload stolen data to cloud
    simulate_data_transfer_to_cloud()

    # Step 10: Steal device information
    simulate_device_info_theft()

    # Step 11: Simulate device infection
    simulate_fake_device_infection()

    # Final Message
    log_output("Attack complete. All steps executed successfully.", error=False)

# Run the full attack simulation
if __name__ == "__main__":
    simulate_full_attack()
