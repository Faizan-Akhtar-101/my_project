import random
import string

print("🔐 Password Generator")

# Step 1: User se password ki length input lena
length = int(input("Enter password length: "))

# Step 2: Characters ka pool banate hain
# ascii_letters = A-Z aur a-z
# digits = 0-9
# punctuation = special characters (!@#$%^&* etc.)
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Empty string banayi jisme password store hoga
password = ""

# Step 4: Loop chalega jitni length user ne di hai
for i in range(length):
    password += random.choice(characters)   # ek random character add hoga

# Step 5: Result print karo
print("Generated Password:", password)
