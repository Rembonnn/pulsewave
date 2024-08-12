import secrets

# Generate a 32-byte secret key
ask_for_generation = input("Generate a 32-byte secret key? (y/n): ").lower()

if ask_for_generation == 'y':
    print(f"Generated 32-byte secret key: {secrets.token_hex(32)}")
    print("Save this key securely and use it in your application environment files.")
else:
    print("Key generation canceled.")