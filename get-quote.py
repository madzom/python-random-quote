import random


def treain():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes)
    print("\n")
    print(quotes[0])
    print("\n")
    print(len(quotes))
    print(quotes[13])

    last = len(quotes) - 1
    rnd = random.randint(0, last)
    print(quotes[rnd])


if __name__ == "__main__":
    treain()
