balance = 500

while balance > 0:  # Check if balance is more than 0
   print(f"Your balance is: ${balance}")      
   cash_out = int(input("Enter withdrawal amount: "))
   
   if cash_out <= balance:   # Check whether withdrawal amount is available from balance
    balance -= cash_out
    print(f"Withdrawal successful! New balance: ${balance}")
   else: 
    print("Insufficient funds! Try again.")    # Tells user that funds is unavailable

print("Your balance is empty. Thank you using the ATM!")

# The wordings I just copy from the canva slides :)


