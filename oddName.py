"""Nyan Soe"""


def main():
    name = input("Your name:")
    name = name.strip()
    while name == "":
        print("Name can not be blank")
        name = input("Your name:")
        name = name.strip()

    words = name.split()

    for word in words:
        count = 0
        for character in word:
            if count == 1:
                print(character)
            count += 1


main()
