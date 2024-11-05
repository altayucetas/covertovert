# CENG 435 Take Home Exam 1 Report
Group 60 <br/>
Group Members:
Nevzat Altay Yücetaş - 2540367 <br/>
Yiğit Alp Alakoç - 2580207
# About SCAPY

Scapy is a powerful Python-based network tool primarily used for network packet manipulation, packet generation, and network protocol analysis. It’s popular among cybersecurity professionals and network engineers because it allows for detailed inspection, creation, modification, and replaying of network packets, which is essential for tasks like network discovery, security testing, and protocol analysis.


# About this code

The packet reciever code starts the reciever first by calling the "sniff" function and filters the packages which comply with the ICMP protocol. Then the "get\_pckg" function calls the show function for any package complying with ICMP and has the TTL value of 1.

The packet sender code starts by creating a packet first with a destination IP of "reciever" and a TTL value of 1, which is then formatted to comply with the ICMP protocol. Then the package is sent by calling the "send" function.

This code is forked form the given repo: https://github.com/cengwins/covertovert

This code can be fond at the given repo: https://github.com/altayucetas/covertovert
