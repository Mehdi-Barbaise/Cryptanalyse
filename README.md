# Cryptanalyse

This Repo contains a few scripts I made to solve challenges on Rootme, Tryhackme and Hackthebox.
(Disclaimer: My goal isn't to help you cheat, and there's no point cheating at these kinds of easy challenges!)

### crackapop.py ###
After analysing packets with Wireshark and found the challenge and the hash, we can provide them, as well as a wordlist, to crack the password.

Usage: 
$ python3 crackapop.py


### encodelist_base64.sh ###
A small script that simply encode a txt file in base64, line per line. The initial goal was to facilate my brute forces attempts in Burp Suite's Intruder.

Usage:
$ ./encodelist_base64.sh <wordlist_path>


### alt_progr_caesar_decode.py ###
The goal of this script was to crack progressive caesar cipher from TryHackMe's Room "Cipher's Secret Message".
I analyzed each step of the encryption process, and did the exact contrary.

Usage:
$ python3 alt_progr_caesar_decode.py
