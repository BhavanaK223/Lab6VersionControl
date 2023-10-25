password = input("Enter your password: ")
print("encoded password", end = ": ")
encoded = ''
for char in range(0, len(password)):
    encode = int(password[char]) + 3
    encoded = encoded + str(encode)
print(encoded)

password = input("Enter encoded password: ")
print("decoded password", end = ": ")
decoded = ''
for char in range(0, len(password)):
    decode = int(password[char]) + 3
    decoded = decoded + str(decode)
print(decoded)

