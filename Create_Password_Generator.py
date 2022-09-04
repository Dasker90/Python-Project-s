import random
import time
import sys
print("--------------------------------------------------")
print(" ____    ____  ____       ____   ____  _____ _____")
print("|    \  /    ||    \     |    \ /    |/ ___// ___/")
print("|  D  )|  o  ||  _  |    |  o  )  o  (   \_(   \_ ")
print("|    / |     ||  |  |    |   _/|     |\__  |\__  |")
print("|    \ |  _  ||  |  |    |  |  |  _  |/  \ |/  \ |")
print("|  .  \|  |  ||  |  |    |  |  |  |  |\    |\    |")
print("|__|\_||__|__||__|__|    |__|  |__|__| \___| \___|")
print("--------------------------------------------------")
print("Hello! Let's generate a password")
print("--------------------------------------------------")
time.sleep(2)
input("Aby przejsc dalej nacisnij klawisz ENTER:")
time.sleep(2)
print("--------------------------------------------------")
### Define a list of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

### Prompt the user
passwordLength = int(input("How long would you like your password to be? "))

### Generate a random password
newPassword = []
for x in range(passwordLength):
    ### Append a random character to the password string
    newPassword.append(random.choice(characters))

### Join the whole list back into a string
finalPassword = ''.join(map(str, newPassword))
time.sleep(2)
print("--------------------------------------------------")
### Let the user know their new password
print("\n This is your new password: ", finalPassword)
print("--------------------------------------------------")
input("Aby zakonczyc nacisnij klawisz ENTER:")
time.sleep(2)
sys.exit()
