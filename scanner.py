import socket
import threading
import sys
import termcolor
import pyfiglet

# Generate banner
from termcolor import colored
banner = pyfiglet.figlet_format("Port Scann3r", font="slant")

# Add color to banner
colored_banner = colored(banner, color="green")

# Add author line to banner
author_line = colored("Written by MMMM", color="red", attrs=["bold"])
banner_with_author = "{}\n{}".format(colored_banner, author_line)

# Print banner
print(banner_with_author)


# Define function to scan port
def scan_port(ip, port):
    try:
        # Create socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout
        sock.settimeout(1)
        # Connect to the port
        result = sock.connect_ex((ip, port))
        if result == 0:
            # Print open port in green color
            print(termcolor.colored("[+] Port {} is open".format(port), 'yellow'))
        # Close the socket
        sock.close()
    except KeyboardInterrupt:
        sys.exit()
    except:
        pass

# Define function to scan ports
def scan(ip, start_port, end_port):
    # Print banner
    print(banner)
    print("[*] Scanning host: {} ...".format(ip))
    # Create threads for each port
    for port in range(start_port, end_port+1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        t.start()

# Define main function
def main():
    # Get input
    ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    # Scan ports
    scan(ip, start_port, end_port)


# Call main function
if __name__ == "__main__":
    main()
