import random 

otp = random.randint(100000,999999)
print("Your OTP is: ",otp)

print("-"*30)

entered_otp = int(input("Enter the OTP: "))

print("-"*30)

if entered_otp == otp:
    print("Verified")
else:
    print("Not verified")