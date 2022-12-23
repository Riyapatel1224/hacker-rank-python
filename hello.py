def main():
    name = input("whats your name? ")
    hello(name)  # name to copied to another variable called "to"


def hello(to="world"):
    print("hello,", to)  # to will display the variable name


hello()