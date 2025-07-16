# Cryptanalyse

This Repo contains a few scripts I made to solve challenges on Rootme, Tryhackme and Hackthebox.


### crackapop.py ###
After analysing packets with Wireshark and found the challenge and the hash, we can provide them, as well as a wordlist, to crack the password.

Usage: 
$ python3 crackapop.py


### encodelist_base64.sh ###
A small script that simply encode a txt file in base64, line per line. The initial goal was to facilate my brute forces attempts in Burp Suite's Intruder.

Usage:
$ ./encodelist_base64.sh <wordlist_path>
