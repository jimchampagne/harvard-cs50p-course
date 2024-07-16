# Ask user for their name
name = input("What's your full name? ").strip().title()

# Remove whitespace from str -> name.strip()
# Capitalize name -> name.capitalize()
# Title name (capitalize every first letter) -> name.title()
# Concatenate functions ->name.strip().title()

# Split users name into first and last name -> first, last = name.split(" ")

# Format string and say hello
print(f"hello, {name}!", sep=" ", end="\n")