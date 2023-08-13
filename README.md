# SSH Brutus - SSH Brute Force Tool

![GitHub](https://img.shields.io/github/license/barisakyildiz/Brutus)
![GitHub Repo stars](https://img.shields.io/github/stars/barisakyildiz/Brutus?style=social)
![GitHub last commit](https://img.shields.io/github/barisakyildiz/Brutus/ssh-brutus)

SSH Brutus is a Python-based SSH brute force tool designed to test the security of SSH servers by attempting various passwords for a given username.

## Features

- Multi-threaded SSH brute force attacks
- User-configurable target IP address, port, username, and password file
- Colorful terminal output using Colorama
- Customizable output for successful and failed authentication attempts

## Installation

1. Clone this repository:
   git clone https://github.com/your-username/ssh-brutus.git
   cd ssh-brutus
2. Install the required Python packages:
   pip install paramiko colorama argparse pyfiglet
   
## Usage

Run the tool using the following command:

``` bash
python SSH-Cracker.py -t <target_ip> -p <port> -f <password_file> -u <username>

<target_ip>: Target's IP address or URL
<port>: Target SSH port (default is 22)
<password_file>: Name of the file containing the list of passwords to try
<username>: Username to use for authentication
```

Note: This tool is intended for educational and security testing purposes only. Unauthorized access to systems is illegal and unethical.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.
