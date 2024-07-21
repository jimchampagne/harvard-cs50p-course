for _ in [0, 1, 2]:
  print("meow")

# ------------------------------

for _ in range(3):
  print("meow")

# ------------------------------

print("meow\n" * 3, end="")

# ------------------------------

n = int(input("What is n? "))

for _ in range(n):
  print("meow")

# ------------------------------

while True:
  n = int(input("What is n? "))
  if n > 0:
    break

for _ in range(n):
  print("meow")

# ------------------------------

def main():
  number = get_number()
  meow(number)

def get_number():
  while True:
    n = int(input("What is n? "))
    if n > 0:
      return n

def meow(n):
  for _ in range(n):
    print("meow")

main()

# --------------------------------