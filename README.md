# AutoProxyConfig

**AutoProxyConfig** is a Python-based tool that dynamically detects the default gateway of your network and configures proxy settings on a Windows system. It is designed primarily for users who create proxy servers on their phones using apps like 'Android Proxy Server' or 'Every Proxy' to share their VPN connection. The tool resolves the issue where the server IP changes every time the hotspot restarts or is turned off and on again, ensuring a consistent proxy connection. It offers an automated solution, making it particularly useful for network administrators and developers looking to streamline their VPN proxy setup. 

## Features

- Automatically detects the default gateway IP address using the `ipconfig` command.
- Configures system-wide proxy settings in the Windows registry.
- Allows customization of proxy server address and bypass list.
- Simple and modular design for easy integration and enhancement.

## Prerequisites

- **Operating System**: Windows (tested on Windows 10 and later).
- **Python**: Python 3.6 or later.

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/itskhawer/AutoProxyConfig.git
   cd AutoProxyConfig
   ```

2. Ensure Python is installed and added to your system PATH.

3. Install any required dependencies (if applicable).

## Usage

1. Open the script in a text editor and modify the `proxy_port` variable if needed:
   ```python
   proxy_port = "8080"
   ```

2. Run the script using Python:
   ```bash
   python AutoProxyConfig.py
   ```

3. If successful, the proxy settings will be updated based on the detected default gateway.

## How It Works

1. **Default Gateway Detection**:
   - The script runs the `ipconfig` command and parses its output to locate the default gateway IP address.

2. **Proxy Configuration**:
   - The `set_proxy` function modifies the Windows registry to enable proxy settings, set the proxy server address, and define a bypass list.

## Script Overview

### Functions

1. `get_default_gateway()`
   - Extracts the default gateway IP address from the network configuration.
   - Returns the IP address as a string or `None` if not found.

2. `set_proxy(enable, proxy_address, bypass_list)`
   - Configures proxy settings in the Windows registry.
   - Parameters:
     - `enable`: 1 to enable the proxy, 0 to disable it.
     - `proxy_address`: The proxy server address (e.g., `192.168.0.1:8080`).
     - `bypass_list`: Addresses to bypass the proxy (e.g., `localhost;127.0.0.1`).

## Example

### Expected Output:

If the default gateway is `192.168.1.1` and `proxy_port` is `8080`, the script will set the proxy server as:
```
192.168.1.1:8080
```
The bypass list will include:
```
localhost;127.0.0.1
```

## Limitations

- The script is designed for Windows systems only.
- Requires administrative privileges to modify registry settings.
- Assumes a standard `ipconfig` output format.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Python Standard Library: `subprocess`, `re`, `winreg`.
- Inspired by the need for dynamic proxy configuration in network environments.

---

**Disclaimer**: Use this tool responsibly. Ensure you have the necessary permissions to modify system settings on your device.

