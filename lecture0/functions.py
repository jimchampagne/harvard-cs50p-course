def main():
  name = input("What's your full name? ").strip().title()
  return hello(name)

def hello(to="World"):
  return print(f"Hello, {to}!")

main()