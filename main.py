syll_list1 = ["Ai",
              "Bray",
              "Cray",
              "Dren",
              "Ell",
              "Fen",
              "Gray",
              "Hai",
              "Hen",
              "Jay",
              "Kay",
              "Lay",
              "May",
              "Nay",
              "Ren",
              "Pay",
              "Quin",
              "Ray",
              "Sky",
              "Tin",
              "Con",
              "Van",
              "Wren",
              "Xen",
              "Yin",
              "Zo"]
syll_list2 = ["lah", "ler","seigh","den","en","lon","deigh","dyl","iah","leah","ken","leigh","ryn","neigh","oah","ley","cen","reigh","syn","tyn","lou","ven","len","xton","yn","rinne"]
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def clear_sc():
    import platform
    import os
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def tragediegh(name_based:bool=False):
    from colorama import Fore,Back,Style
    if name_based == True:
        name = ""
        username = input("Enter your first and last name: ")
        username = username.split(" ")
        for index,name in enumerate(username):
            name = name.capitalize()
            username[index] = name[0]
        for letter in alpha:
            if letter == username[0]:
                tragedeigh_name_index1 = alpha.index(letter)
        for letter in alpha:
            if letter == username[1]:
                tragedeigh_name_index2 = alpha.index(letter)
        tragedeigh_name = syll_list1[tragedeigh_name_index1] + syll_list2[tragedeigh_name_index2]
        return tragedeigh_name
    else:
        import random as r
        tragedeigh_name = r.choice(syll_list1) + r.choice(syll_list2)
        return tragedeigh_name
    
def main():
    import colorama as rama
    while True:
        param = input("Would you like to generate a name based on your own? (y/n) ")
        param = True if param.capitalize() == "Y" else False
        print(rama.Fore.GREEN + "Your tragedeigh name is:",rama.Fore.RED + tragediegh(param)) if param == True else print(rama.Fore.GREEN + "Your tragedeigh name is:",rama.Fore.RED + tragediegh(param))
        input(rama.Fore.RESET + "Press Enter to continue.")
        clear_sc()
        if input("Would you like to quit? (y/n)").capitalize() == "Y":
            break
        else:
            clear_sc()

main()