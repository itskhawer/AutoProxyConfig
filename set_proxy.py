import subprocess
import re
import winreg

def get_server_address():
    try:
        # Run 'ipconfig' to get network information
        result = subprocess.check_output("ipconfig", encoding='utf-8')

        # Split the result into lines to process each line
        lines = result.splitlines()

        for line in lines:
            # Check if the line contains 'Default Gateway'
            if "Default Gateway" in line:
                # Try to extract an IPv4 address from the same line
                match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    return match.group(1)

        print("Default Gateway not found in ipconfig output.")
        return None

    except subprocess.CalledProcessError as e:
        print(f"Error running ipconfig: {e}")
        return None


def get_server_address():
    try:
        # Run 'ipconfig' to get network information
        result = subprocess.check_output("ipconfig", encoding='utf-8')

        # Split the result into lines to process each line
        lines = result.splitlines()

        for i, line in enumerate(lines):
            # Check if the line contains 'Default Gateway'
            if "Default Gateway" in line:
                # Search for an IPv4 address on the same line
                match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    return match.group(1)

                # If no match is found, check the next line
                if i + 1 < len(lines):
                    match = re.search(r"(\d+\.\d+\.\d+\.\d+)", lines[i + 1])
                    if match:
                        return match.group(1)

        print("Default Gateway not found in ipconfig output.")
        return None

    except subprocess.CalledProcessError as e:
        print(f"Error running ipconfig: {e}")
        return None

# Example Usage
server_address = get_server_address()
port ="8080"
set_proxy(1, server_address+":"+port, "localhost;127.0.0.1")