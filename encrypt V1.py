letters = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]
originallet = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]
#,'(',')','_',"=","+","-",",","."
def gettext():
  text = input("enter yout text: ")
  password = input("enter a password: ")
  num = 0
  for i in password :
    indexed = originallet.index(i)
    num += indexed
  for i in range(num):
    fakenum = letters[0]
    letters.remove(fakenum)
    letters.append(fakenum)
  finaltext = ""
  for i in text :
    number = originallet.index(i)
    finaltext += letters[number]
  print(finaltext)

def getpass():
  entext = input("enter the encrypted text: ")
  enpass = input("enter the password: ")
  num = 0
  for i in enpass :
    indexed = originallet.index(i)
    num += indexed
  for i in range(num):
    fakenum = letters[0]
    letters.remove(fakenum)
    letters.append(fakenum)
  textindex = []
  for i in entext:
    heretext = letters.index(i)
    textindex.append(heretext)  
  for i in letters :
    if i == "a" :
      break
    removepoint = [i]
  for i in removepoint :
    letters.remove(i)
    letters.append(removepoint)
  finaltext = ""
  for i in textindex :
    fine = originallet[i]
    
    finaltext += fine
  print(finaltext)

ok = "y"
while ok == "y" :  
  choice = input("encrypt or decrypte (e/d)")

  if choice == "e" :
    gettext()
  elif choice == 'd' :
    getpass()
  else :
    print("its a wrong input")

  ok = input("do you want to continue?? (y/n)")
  letters = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]
