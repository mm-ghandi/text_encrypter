from random import *

letters = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]
originallet = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]

def encrypt():
    text = input("Enter your text: ")
    rand_n = randint(10,99)

    for i in range(rand_n) :
        fakenum = letters[0]
        letters.remove(fakenum)
        letters.append(fakenum)

    finaltext = ""
    for i in text :
        number = originallet.index(i)
        finaltext += letters[number]

    chars = ["!","@","#","$","%","^","&","*","(","0","<",">","?","/","|","~"]

    f_text_list = []
    for i in finaltext :
        f_text_list.append(i)

    for i in range(len(f_text_list)):
        char = chars[randint(0,len(chars)-1)]
        f_text_list.insert(i*2,char)

    f2_list = f_text_list[::-1]

    rand_s = str(rand_n)

    f2_list.insert(0,rand_s[0])
    f2_list.append(rand_s[1])


    f_text = ""

    for i in f2_list :
        f_text += i

    print(f_text)

def decrypt():    


    ramzide = input("Enter you encrypted text: ")
    num = ""
    num += ramzide[0]
    num += ramzide[len(ramzide)-1]
    ramz_list = []
    for i in ramzide :
        ramz_list.append(i)
    ramz_list.pop(0)
    ramz_list.pop(len(ramz_list)-1)

    chars = ["!","@","#","$","%","^","&","*","(","0","<",">","?","/","|","~"]
    for i in range(10):
        for i in chars:
            if i in ramz_list:
                ramz_list.remove(i)



    ramz_list = ramz_list[::-1]


    for i in range(int(num)) :
        fakenum = letters[0]
        letters.remove(fakenum)
        letters.append(fakenum)

    finaltext = ""
    for i in ramz_list :
        number = letters.index(i)
        finaltext += originallet[number]

    print(finaltext)

ok = "y"
while ok == "y" :  
  choice = input("encrypt or decrypte (e/d) " )

  if choice == "e" :
    encrypt()
  elif choice == 'd' :
    decrypt()
  else :
    print("its a wrong input")

  ok = input("do you want to continue?? (y/n)")
  letters = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]

