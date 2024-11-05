from scapy.all import IP, ICMP, send

def send_pckg():
    pckg = IP(dst="receiver", ttl=1) / ICMP()
    send(pckg)

if __name__ == "__main__":
    send_pckg()