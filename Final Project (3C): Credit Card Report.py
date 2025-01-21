"""
Author: Marko 
Date: January 2025
Description: This script reads credit card data from the data.dat file and identifies if the card is expired or close to expired.
"""
from datetime import datetime

# Define the current date as January 2025
current_date = "202501"  

# Open the file and process each line
file = "data.dat"
try:
    with open(file, "r") as fh:
        eof = False
        first_line = True  # Flag to skip the header line
        while not eof:
            line = fh.readline().strip()
            eof = (line == "")
            if not eof:
                if first_line:
                    first_line = False  # Skip the header line
                    continue

                # Split the line into fields: GivenName, Surname, CCType, CCNumber, Exp-Mo, Exp-Yr
                [first, last, card, ccNum, month, year] = line.split(",")

                # Ensure the month is two digits 
                month = month.zfill(2)

                # Combine year and month to create a 6-digit expiry date 
                expiry_date = year + month

                # Determine if the card is expired or needs to be renewed immediately
                if expiry_date < current_date:
                    # Expired card
                    print(f"{first} {last}:     {card}        #{ccNum} {expiry_date} EXPIRED")
                elif expiry_date == current_date:
                    # Card needs renewal immediately
                    print(f"{first} {last}:     {card}        #{ccNum} {expiry_date} RENEW IMMEDIATELY")
    
    fh.close()
except OSError as err:
    print("OSError: ", err)
except EOFError as err2:
    print("EOFError: ", err2)
    fh.close()
