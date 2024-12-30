import socket

def resolve_domain(domain):
    try:
        # to get IPv4 and IPv6 addresses
        result = socket.getaddrinfo(domain, None)
        ip_addresses = [x[4][0] for x in result if ':' not in x[4][0]]  # IPv4 addresses
        ipv6_addresses = [x[4][0] for x in result if ':' in x[4][0]]  # IPv6 addresses
        return ip_addresses, ipv6_addresses
    except socket.gaierror:
        return None, None
