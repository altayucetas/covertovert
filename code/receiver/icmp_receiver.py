from scapy.all import sniff, IP, ICMP

def get_pckg(pckg):
    if pckg.haslayer(ICMP) and pckg[IP].ttl == 1:
        pckg.show()

def start_receiver():
    sniff(filter="icmp", prn=get_pckg)

if __name__ == "__main__":
    start_receiver()