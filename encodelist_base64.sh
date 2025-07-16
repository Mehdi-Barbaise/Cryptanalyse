#!/bin/bash

# Simply encode a wordlist in base64

#Function
base64_encode() {
	echo -n "$1" | base64
}

# Check if file is given as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <wordlist_file>"
    exit 1
fi

# Encode the wordlist
while IFS= read -r line; do
	encoded_line=$(base64_encode "$line")
	echo "$encoded_line" >> encoded_$1
done < "$1"
