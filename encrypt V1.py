letters = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " "]
originallet = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " "]


def get_inputs():
    text = input("Enter your text: ")
    password = input("Enter your password: ")
    return [text, password]


def encrypt(letters):
    text, password = get_inputs()
    num = 0
    for i in password:
        num += originallet.index(i)
    for i in range(num):
        letters = letters[1:] + list(letters[0])
    result = ""
    for i in text:
        result += letters[originallet.index(i)]
    return result


def decrypte(letters):
    text, password = get_inputs()
    num = 0
    for i in password:
        num += originallet.index(i)
    for i in range(num):
        letters = letters[1:] + list(letters[0])
    result = ""
    for i in text:
        result += originallet[letters.index(i)]
    return result


if __name__ == "__main__":
    ok = "y"
    while ok == "y":
          choice = input("Encrypt or decrypte (e/d)")
          if choice == "e":
            print(encrypt(letters))
          elif choice == 'd':
            print(decrypte(letters))
          else:
            print("it\'s a wrong input")
          ok = input("Continue ? (y/n)")
          letters = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                       's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " "]
