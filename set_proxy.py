#!/usr/bin/env python
# coding: utf-8

# In[6]:


import subprocess
import re
import winreg

def get_default_gateway():
    """
    Extracts the default gateway IP address using the 'ipconfig' command.

    Returns:
        str: Default Gateway IP address or None if not found.
    """
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

def set_proxy(enable, proxy_address, bypass_list="localhost;127.0.0.1"):
    """
    Configures the system proxy settings on Windows.

    Args:
        enable (int): 1 to enable the proxy, 0 to disable it.
        proxy_address (str): Proxy server address (e.g., "192.168.0.1:8080").
        bypass_list (str): Addresses to bypass the proxy (semicolon-separated).

    Returns:
        bool: True if the operation succeeds, False otherwise.
    """
    try:
        # Open the registry key for internet settings
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                            r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
                            0, winreg.KEY_SET_VALUE) as reg_key:
            # Enable or disable the proxy
            winreg.SetValueEx(reg_key, "ProxyEnable", 0, winreg.REG_DWORD, enable)

            if enable:
                # Set the proxy server address
                winreg.SetValueEx(reg_key, "ProxyServer", 0, winreg.REG_SZ, proxy_address)

                # Set the bypass list
                winreg.SetValueEx(reg_key, "ProxyOverride", 0, winreg.REG_SZ, bypass_list)

        print("Proxy settings updated successfully.")
        return True
    except Exception as e:
        print(f"Failed to update proxy settings: {e}")
        return False

# Example Usage
if __name__ == "__main__":
    gateway = get_default_gateway()
    if gateway:
        proxy_port = "8080"
        proxy_address = f"{gateway}:{proxy_port}"
        set_proxy(enable=1, proxy_address=proxy_address)
    else:
        print("Cannot set proxy as the default gateway was not found.")


# In[ ]:




