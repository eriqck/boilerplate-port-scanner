import socket

# common_ports dictionary containing port numbers and their respective service names
common_ports = {
    20: "ftp",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    69: "tftp",
    80: "http",
    110: "pop3",
    115: "sftp",
    135: "msrpc",
    137: "netbios-ns",
    138: "netbios-dgm",
    139: "netbios-ssn",
    143: "imap",
    161: "snmp",
    179: "bgp",
    194: "irc",
    389: "ldap",
    443: "https",
    445: "smb",
    636: "ldaps",
    993: "imaps",
    995: "pop3s",
}

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Validate target (URL or IP address)
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        return "Error: Invalid hostname"

    # Validate port range
    if not (0 <= port_range[0] <= 65535 and 0 <= port_range[1] <= 65535):
        return "Error: Invalid port range"

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        sock.close()
        if result == 0:
            open_ports.append(port)

    if verbose:
        output = f"Open ports for {target} ({ip_address})\n"
        output += "PORT     SERVICE\n"
        for port in open_ports:
            service_name = common_ports.get(port, "Unknown")
            output += f"{port:<9}{service_name}\n"
        return output
    else:
        return open_ports

# Test cases
print(get_open_ports("209.216.230.240", [440, 445])) # Example 1
print(get_open_ports("www.stackoverflow.com", [79, 82])) # Example 2
print(get_open_ports("scanme.nmap.org", [20, 80], True)) # Example with verbose mode
